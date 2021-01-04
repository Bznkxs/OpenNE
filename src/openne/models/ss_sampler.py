import torch
import networkx as nx
from torch.utils.data import Sampler
from .walker import Walker, BasicWalker

class BaseSampler(Sampler):
    def __init__(self, name, adj, batch_size):
        # super(BaseSampler, self).__init__()
        self.adj = adj
        self.nnodes = self.adj.size()[0]
        self.nedges = self.adj._indices().size()[1]
        self.batch_size = batch_size
        self.sampler = sampler_dict[name](adj, self.nnodes, self.nedges)

    def __iter__(self):
        batch = []
        for idx in self.sampler:
            batch.append(idx)
            if len(batch) == self.batch_size:
                yield batch
                batch = []

        if len(batch) > 0:
            yield batch

    def __len__(self):
        return (len(self.sampler) + self.batch_size - 1) // self.batch_size
torch.sparse.Tensor(1)

class TripleGenerator(Sampler):
    def __init__(self, adj, nnodes, nedges, name, **kwargs):
        # super().__init__()
        self.nnodes = nnodes
        self.nedges = nedges
        self.adj = adj
        self.adj_ind = self.adj._indices()
        self.anchor_name, self.pos_name, self.neg_name = name.split('-')
        for i, j in kwargs.items():
            self.__setattr__(i, j)
        self.anchor = []
        self.positive = []
        self.negative = []
        self.nodelist = [i for i in range(self.nnodes)]
        self.g = nx.from_edgelist(self.adj_ind.t().numpy(), create_using=nx.DiGraph())

        self.generate()

    def generate(self):
        if (self.anchor_name, self.pos_name) == ('node', 'neighbor'):  # specialize
            self.anchor = self.adj_ind[0]
            self.positive = self.adj_ind[1]
            self.gen_negative()
        elif self.anchor_name == 'node':

            self.gen_positive()
            self.gen_negative()

        # todo: deal with 'graph' condition

    def gen_positive(self):
        if self.pos_name == 'neighbor':
            self.positive = self.adj_ind[1]
        elif self.pos_name == 'rand_walk':
            dw = getattr(self, 'dw', True)
            workers = getattr(self, 'workers', 1)
            silent = getattr(self, 'silent', False)
            if dw:
                walker = BasicWalker(self.g, workers=workers, silent=silent)
            else:
                p = getattr(self, 'p', 0.5)
                q = getattr(self, 'q', 0.5)
                walker = Walker(self.g, p=p, q=q, workers=workers, silent=silent)

            path_length = getattr(self, 'path_length', 80)
            num_paths = getattr(self, 'num_paths', 10)
            sentences = walker.simulate_walks(num_walks=num_paths, walk_length=path_length)
            window = getattr(self, 'window', 10)

            # brute force
            # should optimize later on
            for sentence in sentences:
                for j in range(len(sentence)):
                    for k in range(max(0, j - window), min(len(sentence), j + window + 1)):
                        if k != j:
                            self.anchor.append(sentence[j])
                            self.positive.append(sentence[k])
            # generate anchor and positive

        # todo: deal with other conditions

    def gen_negative(self):  # called after self.anchor is created
        if self.neg_name == 'random':
            self.negative = torch.randint(high=self.nnodes, size=(self.nedges,)).tolist()
        elif self.neg_name == 'except_neighbor':
            #  generate adjacency list
            w1 = {}
            #  for each anchor, generate a random node that is not neighbor
            #  (using binary search)

            # pre-generate a rand list; especially useful for sparse graphs
            # for a graph with 50000 nodes and 100000 edges,
            # binary search is very rarely performed
            ys = torch.randint(0, self.nnodes, [len(self.anchor)]).numpy()
            for idx, x in enumerate(self.anchor):
                x = int(x)
                # try random node first
                y = ys[idx]
                if not self.g.has_edge(x, y):
                    self.negative.append(y)
                    continue

                # generate k-th node that is not neighbor
                if x not in w1:
                    w1[x] = sorted(self.g.neighbors(x))
                adj = w1[x]
                if len(adj) == self.nnodes:  # connected to all nodes
                    self.negative.append(-1)
                i = int(torch.randint(0, self.nnodes - len(adj), [1]))  # rand one out of neighborhood
                if i < adj[0]:
                    self.negative.append(i)
                elif i >= adj[-1] - len(adj) + 1:
                    self.negative.append(i + len(adj))
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
                    self.negative.append(i + l)

        # todo: deal with other conditions

    def __iter__(self):
        return iter(list(zip(self.anchor, self.positive, self.negative)))


class NNRSampler(TripleGenerator):
    def __init__(self, *args, **kwargs):
        super(NNRSampler, self).__init__(*args, name='node-neighbor-random', **kwargs)


available_anchors = ['node']
available_positives = ['neighbor', 'rand_walk']
available_negatives = ['random', 'except_neighbor']

sampler_dict = {
    "node-neighbor-random": NNRSampler
}

'''
TO DO:
    ● node-random walk-random nodes (DeepWalk)
    ● node-neighborhood-except neighborhood (GAE)
    ● graph-node-permuted nodes (DGI)
    ● node-random walk-except neighborhood
'''
