import random
import tqdm
import time
import torch
import networkx as nx
import numpy as np
from scipy.linalg import fractional_matrix_power, inv
from torch.utils.data import Sampler
from .walker import Walker, BasicWalker

class BaseSampler:
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
        self.sampler = sampler_dict[name](adj, self.nnodes, self.nedges, self.features, batch_size=self.batch_size, device=self.device)

    def sample(self):
        return self.sampler.sample()


def randwalk(dw, workers, silent, G, p, q, path_length, num_paths):
    if dw:
        walker = BasicWalker(G, workers=workers, silent=silent)
    else:
        walker = Walker(G, p=p, q=q, workers=workers, silent=silent)
    return walker.simulate_walks(num_walks=num_paths, walk_length=path_length)


class graphinput:
    def __init__(self, x, y, edge_idx, edge_weight=None):
        """

        @param x:
        @param y:
        @param edge_idx:
        @param edge_weight: None (all 1) by default
        """
        self.x = x
        self.y = y
        self.edge_idx = edge_idx
        self.edge_weight = edge_weight

class GraphSampler:
    def __init__(self, graphs, batch_size, device):
        #self.anchor_name, self.pos_name, self.neg_name = name.split('-')
        self.sample_size = 2000
        self.graphs = graphs
        self.anchor = self.graphs  # densere aut non densere, illa quaestio
        self.positive = []
        self.get_positive()
        self.batch_size = batch_size
        self.device = device

    def get_positive(self):
        self.positive = self.anchor

    def augment(self):
        self.negative = [np.random.permutation(np.arange(graph.x.shape[0])) for graph in self.graphs]


    def sample(self):
        #  self.augment()  # seems to have no effect

        # sample
        # we wish to get ba, bd, bf, shuf_fts: batch anchors, batch diffusions, batch features, batch shuffled features
        ba, bd, bf, shuf_fts = [], [], [], []
        def get_submat(graph, i):
            r = i + self.sample_size
            eidx = graph.edge_idx
            eidx = eidx[:, (eidx[0] >= i) * (eidx[0] < r) * (eidx[1] >= i) * (eidx[1] < r)]
            return eidx
        for i, graph in enumerate(self.graphs):
            pos = self.positive[i]
            if graph.x.shape[0] < self.sample_size + 1:
                idx = [0]
            else:
                idx = np.random.randint(0, graph.x.shape[0] - self.sample_size + 1, 1)

            for i in idx:
                # get a sub-adjmat
                r = i + self.sample_size
                x = graph.x[i: r]
                eidx = get_submat(graph, i)
                eidxd = get_submat(pos, i)
                ba.append(graphinput(x, None, eidx))
                bd.append(graphinput(x, None, eidxd))
                bf.append(x)
                rp = np.random.permutation(self.sample_size)
                shuf_fts.append(x[rp, :])
        return ba, bd, bf, shuf_fts

class DGISampler(GraphSampler):
    def get_positive(self):
        self.positive = self.anchor


class DiffSampler(GraphSampler):
    def get_positive(self):
        t = torch.FloatTensor(self.compute_ppr())
        # convert t into sparse
        idx = torch.nonzero(t).t()
        val = t[idx[0], idx[1]]
        self.positive = graphinput(self.graphs.x, None, idx, val)

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