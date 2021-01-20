import random
import tqdm
import time
import torch
import networkx as nx
import numpy as np
from scipy.linalg import fractional_matrix_power, inv
from torch.utils.data import Sampler
from .walker import Walker, BasicWalker

class BaseSampler(Sampler):
    def __init__(self, name, adj, features, batch_size, device, negative_ratio=5, **kwargs):
        # super(BaseSampler, self).__init__()
        self.adj = adj
        self.nnodes = self.adj.size()[0]
        self.nedges = self.adj._indices().size()[1]
        self.features = features
        self.negative_ratio = negative_ratio
        self.batch_size = batch_size
        self.name = name
        self.device = device
        self.sampler = sampler_dict[name](adj, self.nnodes, self.nedges, self.features, self.batch_size, self.device)
        '''
        if name not in sampler_dict:
            self.sampler = TripleGenerator(self.adj, self.nnodes, self.nedges, negative_ratio, name, **kwargs)
        else:
            self.sampler = sampler_dict[name](adj, self.nnodes, self.nedges, self.features, self.batch_size, self.device)
        '''
        super(BaseSampler, self).__init__(self.sampler)

    def __iter__(self):
        for idx in range(0, len(self.sampler), self.batch_size):
            yield self.sampler[idx:idx+self.batch_size]
        self.sampler.regenerate()

    def __len__(self):
        return (len(self.sampler) + self.batch_size - 1) // self.batch_size
    
    def sample(self):
        return self.sampler.sample()


def randwalk(dw, workers, silent, G, p, q, path_length, num_paths):
    if dw:
        walker = BasicWalker(G, workers=workers, silent=silent)
    else:
        walker = Walker(G, p=p, q=q, workers=workers, silent=silent)
    return walker.simulate_walks(num_walks=num_paths, walk_length=path_length)

class TripleGenerator(Sampler):
    def __init__(self, adj, nnodes, nedges, negative_ratio, name, **kwargs):
        # super().__init__()
        self.nnodes = nnodes
        self.nedges = nedges
        self.adj = adj
        self.adj_ind = self.adj._indices()
        self.anchor_name, self.pos_name, self.neg_name = name.split('-')
        self.negative_ratio = negative_ratio
        for i, j in kwargs.items():
            self.__setattr__(i, j)
        self.nodelist = [i for i in range(self.nnodes)]
        self.anchor = torch.zeros(1)
        self.positive = torch.zeros(1)
        self.negative = torch.zeros(1)
        self.samples = torch.zeros(1)
        self.g = nx.from_edgelist(self.adj_ind.t().numpy(), create_using=nx.DiGraph())

        self.generate()
        print("sampler length =", len(self.anchor),len(self.positive),len(self.negative))
        super(TripleGenerator, self).__init__(self)

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

class DGISampler():
    def __init__(self, adj, nnodes, nedges, features, batch_size, device):
        super(DGISampler, self).__init__()
        #self.anchor_name, self.pos_name, self.neg_name = name.split('-')
        self.sample_size = 2000
        self.adj = adj
        self.nnodes = nnodes
        self.nedges = nedges
        self.features = features
        self.anchor = self.adj.to_dense()
        self.positive = self.anchor
        self.batch_size = batch_size

    def augment(self):
        
        self.negative = np.random.permutation(np.arange(self.nnodes))
        
    
    def sample(self):
        self.augment()
        idx = np.random.randint(0, self.nnodes - self.sample_size + 1, 1)
        ba, bd, bf = [], [], []
        for i in idx:
            ba.append(self.anchor[i: i + self.sample_size, i: i + self.sample_size])
            bd.append(self.positive[i: i + self.sample_size, i: i + self.sample_size])
            bf.append(self.features[i: i + self.sample_size])

        
        ba = torch.stack(ba).squeeze()
        bd = torch.stack(bd).squeeze()
        bf = torch.stack(bf).squeeze()
        idx = np.random.permutation(self.sample_size)
        shuf_fts = bf[idx, :]
        return ba, bd, bf, shuf_fts

class DiffSampler():
    def __init__(self, adj, nnodes, nedges, features, batch_size, device):
        super(DiffSampler, self).__init__()
        #self.anchor_name, self.pos_name, self.neg_name = name.split('-')
        self.sample_size = 2000
        self.adj = adj
        self.nnodes = nnodes
        self.nedges = nedges
        self.features = features
        self.anchor = self.adj.to_dense()
        self.positive = self.adj.to_dense()
        self.batch_size = batch_size
        self.device = device
        self.positive = torch.FloatTensor(self.compute_ppr()).to(self.device)

    def augment(self):
        self.negative = np.random.permutation(np.arange(self.nnodes))
    
    def sample(self):
        self.augment()
        idx = np.random.randint(0, self.nnodes - self.sample_size + 1, 1)
        ba, bd, bf = [], [], []
        for i in idx:
            ba.append(self.anchor[i: i + self.sample_size, i: i + self.sample_size])
            bd.append(self.positive[i: i + self.sample_size, i: i + self.sample_size])
            bf.append(self.features[i: i + self.sample_size])

        
        ba = torch.stack(ba).squeeze()
        bd = torch.stack(bd).squeeze()
        bf = torch.stack(bf).squeeze()
        idx = np.random.permutation(self.sample_size)
        shuf_fts = bf[idx, :]
        return ba, bd, bf, shuf_fts
    
    def compute_ppr(self, alpha=0.2, self_loop=True):
        a = self.anchor.cpu().numpy()
        if self_loop:
            a = a + np.eye(a.shape[0])                                # A^ = A + I_n
        d = np.diag(np.sum(a, 1))                                     # D^ = Sigma A^_ii
        dinv = fractional_matrix_power(d, -0.5)                       # D^(-1/2)
        at = np.matmul(np.matmul(dinv, a), dinv)                      # A~ = D^(-1/2) x A^ x D^(-1/2)
        return alpha * inv((np.eye(a.shape[0]) - (1 - alpha) * at))   # a(I_n-(1-a)A~)^-1


available_anchors = ['node']
available_positives = ['neighbor', 'rand_walk']
available_negatives = ['random', 'except_neighbor']

sampler_dict = {
    "node-neighbor-random": NNRSampler,
    "dgi": DGISampler,
    "mvgrl": DiffSampler

}

'''
TO DO:
    ● node-random walk-random nodes (DeepWalk)
    ● node-neighborhood-except neighborhood (GAE)
    ● graph-node-permuted graph (DGI)
    ● graph-diffusion-permuted graph (MVGRL)
    ● node-random walk-except neighborhood
'''