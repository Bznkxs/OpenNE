import random
import tqdm
import time
import torch
import networkx as nx
import scipy.sparse as sp
from torch.utils.data import Sampler
from .walker import Walker, BasicWalker
from .utils import scipy_coo_to_torch_sparse, getdevice
class BaseSampler(Sampler):
    def __init__(self, name, graph, batch_size, negative_ratio=5, **kwargs):
        self.adj = scipy_coo_to_torch_sparse(
            sp.coo_matrix(graph.adjmat(weighted=False, directed=True, sparse=True)))
        self.nnodes = self.adj.size()[0]
        self.nedges = self.adj._indices().size()[1]
        self.batch_size = batch_size
        if name not in sampler_dict:
            self.sampler = TripleGenerator(graph, self.adj, self.nnodes, self.nedges, negative_ratio, name, **kwargs)
        else:
            self.sampler = sampler_dict[name](graph, self.adj, self.nnodes, self.nedges, negative_ratio, **kwargs)
        super(BaseSampler, self).__init__(self.sampler)

    def __iter__(self):
        for idx in range(0, len(self.sampler), self.batch_size):
            yield self.sampler[idx:idx+self.batch_size]
        self.sampler.regenerate()

    def __len__(self):
        return (len(self.sampler) + self.batch_size - 1) // self.batch_size


def randwalk(dw, workers, silent, G, p, q, path_length, num_paths):
    if dw:
        walker = BasicWalker(G, workers=workers, silent=silent)
    else:
        walker = Walker(G, p=p, q=q, workers=workers, silent=silent)
    return walker.simulate_walks(num_walks=num_paths, walk_length=path_length)


# triple generator for **one graph**
class TripleGenerator(Sampler):
    def __init__(self, graph, adj, nnodes, nedges, negative_ratio, name, **kwargs):
        self.anchor_name, self.pos_name, self.neg_name = name.lower().split('-')
        self.negative_ratio = 1  # negative_ratio
        if kwargs.get('empty', False):
            super(TripleGenerator, self).__init__(self)
            return
        self.nnodes = nnodes
        self.nedges = nedges
        self.graph = graph
        self.adj = adj  # should be a sparse matrix
        self.adj_ind = self.adj._indices()
        for i, j in kwargs.items():
            self.__setattr__(i, j)
        self.anchor = torch.zeros(1)
        self.positive = torch.zeros(1)
        self.negative = torch.zeros(1)
        self.samples = torch.zeros(1)
        self.nodelist = [i for i in range(self.nnodes)]
        self.adjlist = {i: graph.G.neighbors(i) for i in range(self.nnodes)}
        self.generate()
        print("sampler length =", len(self.anchor),len(self.positive),len(self.negative))
        super(TripleGenerator, self).__init__(self)

    def adapt(self, adj):
        self.adj = adj
        self.adj_ind = self.adj._indices()
        self.nnodes = adj.shape[0]
        self.nedges = adj._nnz()
        self.graph = adj  # nx.DiGraph(adj)
        self.adjlist = {i: [] for i in range(self.nnodes)}
        for i in range(adj._nnz()):
            x, y = adj._indices()[0, i].item(), adj._indices()[1, i].item()
            self.adjlist[x].append(y)
        self.nodelist = [i for i in range(self.nnodes)]
        self.generate()

    def generate(self):
        if (self.anchor_name, self.pos_name) == ('node', 'neighbor'):  # specialize
            self.anchor = self.adj_ind[0]
            self.positive = self.adj_ind[1]
            self.gen_node_negative()
        elif self.anchor_name == 'node':

            self.gen_node_positive()
            self.gen_node_negative()

        # todo: deal with 'graph' condition
        elif self.anchor_name == 'graph':
            self.gen_graph_positive()
            self.gen_graph_negative()

        self.samples = torch.stack((self.anchor, self.positive, self.negative)).t()

    def regenerate(self):

        if self.anchor_name == "node":
            self.gen_node_negative(False)
        else:
            self.gen_graph_negative()
        self.samples = torch.stack((self.anchor, self.positive, self.negative)).t()

    def gen_node_positive(self):
        print("generating anchors and graphs_diff samples...")
        if self.pos_name == 'neighbor':
            self.positive = self.adj_ind[1]
        elif self.pos_name == 'rand_walk':
            dw = getattr(self, 'dw', True)
            workers = getattr(self, 'workers', 1)
            silent = getattr(self, 'silent', False)
            p = getattr(self, 'p', 0.5)
            q = getattr(self, 'q', 0.5)
            path_length = getattr(self, 'path_length', 50)
            num_paths = getattr(self, 'num_paths', 5)
            window = getattr(self, 'window', 5)
            print(path_length, num_paths, window)
            sentences = randwalk(dw, workers, silent, self.graph, p, q, path_length, num_paths)
            print(f"{len(sentences)} sentences created")

            anchor = []
            positive = []
            mode = 1

            if mode == 1:
                # brute force
                # should optimize later on
                t = time.time()
                for sentence in tqdm.tqdm(sentences):
                    for j in range(len(sentence)):
                        for k in range(max(0, j - window), min(len(sentence), j + window + 1)):
                            if k != j:
                                anchor.append(sentence[j])
                                positive.append(sentence[k])
                # deduplicate
                # items = set(zip(anchor, graphs_diff))
                # anchor, graphs_diff = zip(*items)
                self.anchor = torch.tensor(anchor)
                self.positive = torch.tensor(positive)
                print("mode 1: time used =", time.time() - t)


            else:
                # simplify 1
                t = time.time()
                for sentence in tqdm.tqdm(sentences):
                    s = torch.tensor(sentence)
                    # deal with full windows
                    j1 = torch.arange(0, len(s) - window)
                    k1 = torch.arange(1, window+1)
                    k1 = (j1.reshape((-1,1)) + k1).reshape(-1)
                    j1 = j1.repeat_interleave(window)

                    j2 = torch.arange(window, len(s))
                    k2 = torch.arange(-window, 0)
                    k2 = (j2.reshape((-1,1)) + k2).reshape(-1)
                    j2 = j2.repeat_interleave(window)

                    anchor.append(s[j1])
                    positive.append(s[k1])
                    anchor.append(s[j2])
                    positive.append(s[k2])

                anchor = torch.cat(anchor).tolist()
                positive = torch.cat(positive).tolist()
                # items = set(zip(anchor, graphs_diff))
                # anchor, graphs_diff = zip(*items)
                self.anchor = torch.tensor(anchor)
                self.positive = torch.tensor(positive)
                print("mode 2: time used =", time.time() - t)



        print(f"anchors and graphs_diff samples of len {len(self.anchor)} generated")
            # generate anchor and graphs_diff

        # todo: deal with other conditions
    def gen_graph_positive(self):
        print("generating anchors and graphs_diff samples:")
        if self.pos_name == "node":
            self.anchor = [-1] * self.nnodes
            self.positive = list(range(self.nnodes))
        print(f"anchors and graphs_diff samples of len {len(self.anchor)} generated")

    def gen_node_negative(self, repeat=True):  # called after self.anchor is created
        if repeat:
            print(f"repeating {self.negative_ratio} times...")
            self.anchor = self.anchor.repeat(self.negative_ratio)
            self.positive = self.positive.repeat(self.negative_ratio)
            print(f"generating negative samples with {self.neg_name}...")
        if self.neg_name == 'random':
            self.negative = torch.randint(high=self.nnodes, size=(len(self.anchor),))
        elif self.neg_name == 'except_neighbor':  # anchor must be node
            #  generate adjacency list
            w1 = {}
            #  for each anchor, generate a random node that is not neighbor
            #  (using binary search)

            # pre-generate a rand list; especially useful for sparse graphs
            # for a graph with 50000 nodes and 100000 edges,
            # binary search is very rarely performed
            ys = torch.randint(0, self.nnodes, [len(self.anchor)])
            for idx, x in tqdm.tqdm(enumerate(self.anchor), total=len(self.anchor)):
                x = int(x)
                # try random node first
                y = ys[idx]
                if not self.adj[x, y]:
                    continue

                # generate k-th node that is not neighbor
                if x not in w1:
                    w1[x] = sorted(self.adjlist[x])
                adj = w1[x]
                if len(adj) == self.nnodes:  # connected to all nodes
                    ys[idx] = -1
                i = int(torch.randint(0, self.nnodes - len(adj), [1]))  # rand one out of neighborhood
                if i < adj[0]:
                    ys[idx] = i
                elif i >= adj[-1] - len(adj) + 1:
                    ys[idx] = i + len(adj)
                else:
                    # binary search to get i-th element out of neighborhood
                    l = 0
                    r = len(adj) - 1
                    while l < r:
                        mid = (l + r) // 2
                        if adj[mid] - mid > i:
                            r = mid - 1
                        else:
                            l = mid + 1
                    ys[idx] = i + l
            self.negative = ys
        if repeat:
            print("negative samples generated")
        # todo: deal with other conditions
    def gen_graph_negative(self):
        print("generating negative samples...")
        if self.neg_name == 'permuted':
            self.negative = self.positive[torch.randperm(len(self.positive))]
        elif self.neg_name == 'nodes_in_other_graph':
            self.negative = torch.tensor([self.nnodes] * self.nnodes)
        print("negative samples generated")

    def __iter__(self):
        return self.samples

    def __getitem__(self, item):
        return self.anchor[item].to(getdevice()), self.positive[item].to(getdevice()), self.negative[item].to(getdevice())

    def __len__(self):
        return len(self.anchor)

class NNRSampler(TripleGenerator):
    def __init__(self, *args, **kwargs):
        super(NNRSampler, self).__init__(*args, name='node-neighbor-random', **kwargs)

class NNESampler(TripleGenerator):
    def __init__(self, *args, **kwargs):
        super(NNESampler, self).__init__(*args, name='node-neighbor-except_neighbor', **kwargs)

class NRRSampler(TripleGenerator):
    def __init__(self, *args, **kwargs):
        super(NRRSampler, self).__init__(*args, name='node-rand_walk-random', **kwargs)

class NRESampler(TripleGenerator):
    def __init__(self, *args, **kwargs):
        super(NRESampler, self).__init__(*args, name='node-rand_walk-except_neighbor', **kwargs)

available_anchors = ['node']
available_positives = ['neighbor', 'rand_walk']
available_negatives = ['random', 'except_neighbor']

sampler_dict = {
    "node-neighbor-random": NNRSampler,
    "node-neighbor-except_neighbor": NNESampler,
    "node-rand_walk-random": NRRSampler,
    "node-rand_walk-except_neighbor": NRESampler,
}

'''
TO DO:
    ● node-random walk-random nodes (DeepWalk)
    ● node-neighborhood-except neighborhood (GAE)
    ● graph-node-permuted nodes (DGI)
    ● node-random walk-except neighborhood
'''
