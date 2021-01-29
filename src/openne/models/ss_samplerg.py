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
    def __init__(self, name, graph, features, batch_size, device, negative_ratio=5, **kwargs):
        # super(BaseSampler, self).__init__()
        self.graph = graph
        self.features = features
        self.negative_ratio = negative_ratio
        self.batch_size = batch_size
        self.name = name
        self.device = device
        self.sampler = sampler_dict[name](graph, batch_size=self.batch_size, device=self.device)

    def sample(self):
        return self.sampler.sample()


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
        self.edge_index = edge_idx
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
            eidx = graph.edge_index
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
                rp = np.random.permutation(min(self.sample_size, len(x)))
                shuf_fts.append(x[rp, :])
        return ba, bd, bf, shuf_fts

class DGISampler(GraphSampler):
    def get_positive(self):
        self.positive = self.anchor


class DiffSampler(GraphSampler):
    def get_positive(self):
        def compute_ppr(edge_index, alpha=0.2, self_loop=True):
            adj = torch.sparse_coo_tensor(edge_index, torch.ones(edge_index.shape[1])).to_dense()

            a = adj.cpu().numpy()
            if self_loop:
                a = a + np.eye(a.shape[0])                                # A^ = A + I_n
            d = np.diag(np.sum(a, 1))                                     # D^ = Sigma A^_ii
            dinv = fractional_matrix_power(d, -0.5)                       # D^(-1/2)
            at = np.matmul(np.matmul(dinv, a), dinv)                      # A~ = D^(-1/2) x A^ x D^(-1/2)
            return alpha * inv((np.eye(a.shape[0]) - (1 - alpha) * at))   # a(I_n-(1-a)A~)^-1

        self.positive = []
        for g in self.graphs:
            t = torch.FloatTensor(compute_ppr(g.edge_index))
            # convert t into sparse
            idx = torch.nonzero(t).t()
            val = t[idx[0], idx[1]]
            self.positive.append(graphinput(g.x, None, idx, val))



    def sample(self):
        #  self.augment()  # seems to have no effect
        # ba, bdiff, bfeat, bneg, bnegdiff, bnegfeat
        # sample
        ba, bdiff, bfeat, bneg, bnegdiff, bnegfeat = [], [], [], [], [], []

        def get_submat(graph, i):
            r = i + self.sample_size
            eidx = graph.edge_index
            eidx = eidx[:, (eidx[0] >= i) * (eidx[0] < r) * (eidx[1] >= i) * (eidx[1] < r)]
            return eidx
        old_graphs = self.graphs
        # self.graphs = self.graphs[torch.randperm(len(self.graphs))]
        for i, graph in enumerate(self.graphs):
            # get ba, bdiff, bfeat, bneg, bnegdiff, bnegfeat
            pos = self.positive[i]
            # get a negative graph (a random graph)
            negidx = np.random.randint(0, len(self.graphs) - 2)
            if negidx == i:
                negidx += 1
            neg = self.graphs[negidx]
            negdiff = self.positive[negidx]
            if graph.x.shape[0] < self.sample_size + 1:
                idx = [0]
            else:
                idx = np.random.randint(0, graph.x.shape[0] - self.sample_size + 1, 1)

            for i in idx:
                # get a sub-adjmat
                r = i + self.sample_size
                x = graph.x[i: r]
                nx = neg.x[i:r]
                eidx = get_submat(graph, i)
                eidxd = get_submat(pos, i)
                eidxn = get_submat(neg, i)
                eidxnd = get_submat(negdiff, i)
                ba.append(graphinput(x, None, eidx))
                bdiff.append(graphinput(x, None, eidxd))
                bneg.append(graphinput(nx, None, eidxn))
                bnegdiff.append(graphinput(nx, None, eidxnd))
                bfeat.append(x)
                bnegfeat.append(nx)
        self.graphs = old_graphs
        return ba, bdiff, bfeat, bneg, bnegdiff, bnegfeat


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