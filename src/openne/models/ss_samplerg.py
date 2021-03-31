import random
import tqdm
import time
import torch
import networkx as nx
import numpy as np
from scipy.linalg import fractional_matrix_power, inv
from ..utils import getdevice
from .utils import process_graphs
from ss_input import model_input

class BaseSampler:
    def __init__(self, name, graph, features, batch_size, negative_ratio=5, **kwargs):
        # super(BaseSampler, self).__init__()
        self.graph = graph
        self.features = features
        self.negative_ratio = negative_ratio
        self.batch_size = batch_size
        self.name = name
        self.sampler = sampler_dict[name](graph, batch_size=self.batch_size)

    def __iter__(self):
        return self.sampler.__iter__()

    def __len__(self):
        return self.sampler.__len__()


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


def compute_ppr(edge_index, alpha=0.2, self_loop=True):
    adj = torch.sparse_coo_tensor(edge_index, torch.ones(edge_index.shape[1])).to_dense()
    print("adj:", adj.device)
    a = adj.cpu().numpy()
    if self_loop:
        a = a + np.eye(a.shape[0])  # A^ = A + I_n
    d = np.diag(np.sum(a, 1))  # D^ = Sigma A^_ii
    dinv = fractional_matrix_power(d, -0.5)  # D^(-1/2)
    at = np.matmul(np.matmul(dinv, a), dinv)  # A~ = D^(-1/2) x A^ x D^(-1/2)
    return alpha * inv((np.eye(a.shape[0]) - (1 - alpha) * at))  # a(I_n-(1-a)A~)^-1


def sample_subgraph(graphs, n_nodes, max_graph_size, do_sample=True):
    """

    @param do_sample: if False, return original graph.
    @param graphs: a list of two graphs, [anchor, diffusion], which share the same features and node sampling.
    @param n_nodes: number of nodes in any graph.
    @param max_graph_size: threshold of sampling.
    @return: (subfeats of graph1, subedges of grpah1, subedges of graph2)
    """
    # sample node list
    if do_sample:
        permuted_nodes = torch.randperm(n_nodes)
    else:
        permuted_nodes = torch.arange(n_nodes)
        max_graph_size = int(1e9)
    map_idx = torch.argsort(permuted_nodes)
    subnodes = permuted_nodes[:max_graph_size]

    anchor, diffusion = graphs
    feats, edges1, edges2 = anchor.x, anchor.edge_index, diffusion.edge_index

    subfeats = feats[subnodes].to(getdevice())

    def sample_edges(edges):
        subedges = map_idx[edges]  # permutation
        e_sample = (subedges[0] < max_graph_size) * (subedges[1] < max_graph_size)

        return subedges[:, e_sample]

    subedges1 = sample_edges(edges1)
    subedges2 = sample_edges(edges2)

    assert anchor.edge_index.max() < len(feats)
    assert diffusion.edge_index.max() < len(feats)

    return subfeats, subedges1, subedges2


class GraphSampler:
    def __init__(self, graphs, batch_size):
        # self.anchor_name, self.pos_name, self.neg_name = name.split('-')
        self.sample_size = 2000
        self.graphs = graphs
        self.anchor = self.graphs  # densere aut non densere, illa quaestio
        self.num_graphs = len(graphs)
        self.graphs_diff = []
        self.get_diffused_graphs()
        self.batch_size = batch_size  # use this!
        print("sampler batch size =", self.batch_size)
        self.cache = None
        self.sample_subgraph = True

    def get_diffused_graphs(self):
        """
        generate graphs_diff
        @return: null
        """
        raise NotImplementedError

    def get_negative_indices_and_features(self, f_pos, e_anchor, e_diff):
        """

        @param f_pos:
        @param e_anchor:
        @param e_diff:
        @return: f_neg, e_neg, e_negdiff
        """
        raise NotImplementedError

    def sample(self):
        """
        Performs: random pairing and sampling
        Returns values needed for generating (anchor, pos, neg)
        @return: f_pos, f_neg, e_anchor, e_diff, e_neg, e_diffneg, slices
        """
        g_anchor, g_diff = self.anchor, self.graphs_diff
        f_pos, e_anchor, e_diff, = [], [], []
        # sample subgraphs
        for i in range(self.num_graphs):
            f1, e1, e2 = sample_subgraph([g_anchor[i], g_diff[i]], len(g_anchor[i].x), self.sample_size, self.sample_subgraph)
            f_pos.append(f1)
            e_anchor.append(e1)
            e_diff.append(e2)

        # get negative
        f_neg, e_neg, e_diffneg = self.get_negative_indices_and_features(f_pos, e_anchor, e_diff)

        # get slices
        slices = self.sample_slicer(f_pos)
        return f_pos, f_neg, e_anchor, e_diff, e_neg, e_diffneg, slices

    def get_sample(self):
        if self.cache is None:
            self.cache = self.sample()
        return self.cache

    def sample_slicer(self, f_pos):
        iter_step = self.batch_size

        iter_head = 0
        accum_len = 0
        slice_head = 0
        ret = []
        while iter_head <= self.num_graphs:
            if iter_head == self.num_graphs or (accum_len > 0 and accum_len + len(f_pos[iter_head]) > iter_step):
                i = slice(slice_head, iter_head)
                ret.append(i)
                accum_len = 0
                slice_head = iter_head
            if iter_head < self.num_graphs:
                accum_len += len(f_pos[iter_head])
            iter_head += 1
        return ret

    @classmethod
    def process_graphs(cls, f_pos, f_neg, e_anchor, e_diff, e_neg, e_diffneg):
        """

        @param f_pos:
        @param f_neg:
        @param e_anchor:
        @param e_diff:
        @param e_neg:
        @param e_diffneg:
        @return: generate adj, add, adn, adnd, start_idx, start_idd, start_idn, start_idnd for a batch of graphs
        """
        # graph_pos = graphinput(f_pos[i], None, e_anchor[i], None)
        # graph_neg = graphinput(f_neg[i], None, e_neg[i], None)
        # graph_diff = graphinput(f_pos[i], None, e_diff[i], None)
        # graph_diffneg = graphinput(f_neg[i], None, e_diffneg[i], None)
        raise NotImplementedError

    def __iter__(self):
        """
        create batch samples
        @return:
        """
        f_pos, f_neg, e_anchor, e_diff, e_neg, e_diffneg, slices = self.get_sample()
        for i in slices:  # for each batch
            f_pos_d = f_pos[i]
            adj, add, adn, adnd, start_idx, start_idd, start_idn, start_idnd \
                = self.process_graphs(f_pos[i], f_neg[i], e_anchor[i], e_diff[i], e_neg[i], e_diffneg[i])
            bx = model_input(model_input.GRAPHS, adj, start_idx, f_pos[i])
            bpos = model_input(model_input.NODES, add, start_idd, f_pos[i])
            bneg = model_input(model_input.NODES, adnd, start_idnd, f_neg[i])

            bx_r = model_input(model_input.GRAPHS, add, start_idd, f_pos[i])
            bpos_r = model_input(model_input.NODES, adj, start_idx, f_pos[i])
            bneg_r = model_input(model_input.NODES, adn, start_idn, f_neg[i])

            yield bx, bpos, bneg
            yield bx_r, bpos_r, bneg_r
        self.cache = None

    def __len__(self):
        """

        @return: number of batches = len(slices) * 2
        """
        _, _, _, _, _, _, slices = self.get_sample()
        return len(slices) * 2


class DGISampler(GraphSampler):
    def get_diffused_graphs(self):
        self.graphs_diff = self.anchor

    @classmethod
    def process_graphs(cls, f_pos, f_neg, e_anchor, e_diff, e_neg, e_diffneg):
        g_anchor, g_neg = [], []
        for i in range(len(f_pos)):
            g_anchor.append(graphinput(f_pos[i], None, e_anchor[i]))
            # g_diff = g_anchor
            g_neg.append(graphinput(f_neg[i], None, e_anchor[i]))
            # g_negdiff = g_neg
        adj, start_idx = process_graphs(g_anchor, getdevice())
        adn, start_idn = process_graphs(g_neg, getdevice())
        return adj, adj, adn, adn, start_idx, start_idx, start_idn, start_idn

    def get_negative_indices_and_features(self, f_pos, e_anchor, e_diff):
        f_neg = []
        for f in f_pos:
            rp = np.random.permutation(len(f))
            f_neg.append(f[rp])
        return f_neg, e_anchor, e_diff


class DiffSampler(GraphSampler):
    def get_diffused_graphs(self):
        self.graphs_diff = []
        for g in self.graphs:
            t = torch.FloatTensor(compute_ppr(g.edge_index))
            # convert t into sparse
            idx = torch.nonzero(t).t()
            val = t[idx[0], idx[1]]
            self.graphs_diff.append(graphinput(g.x, None, idx, val))

    def get_negative_indices_and_features(self, f_pos, e_anchor, e_diff):
        f_neg, e_neg, e_negdiff = [], [], []
        for i in range(self.num_graphs):
            negidx = np.random.randint(0, len(self.graphs) - 2)
            if negidx == i:
                negidx += 1
            f_neg.append(f_pos[negidx])
            e_neg.append(e_anchor[negidx])
            e_negdiff.append(e_diff[negidx])
        return f_neg, e_neg, e_negdiff

    @classmethod
    def process_graphs(cls, f_pos, f_neg, e_anchor, e_diff, e_neg, e_diffneg):
        g_anchor, g_diff, g_neg, g_negdiff = [], [], [], []
        for i in range(len(f_pos)):
            g_anchor.append(graphinput(f_pos[i], None, e_anchor[i]))
            g_diff.append(graphinput(f_pos[i], None, e_diff[i]))
            g_neg.append(graphinput(f_neg[i], None, e_neg[i]))
            g_negdiff.append(graphinput(f_neg[i], None, e_diffneg[i]))
        adj, start_idx = process_graphs(g_anchor, getdevice())
        add, start_idd = process_graphs(g_diff, getdevice())
        adn, start_idn = process_graphs(g_neg, getdevice())
        adnd, start_idnd = process_graphs(g_negdiff, getdevice())
        return adj, add, adn, adnd, start_idx, start_idd, start_idn, start_idnd


sampler_dict = {
    "dgi": DGISampler,
    "mvgrl": DiffSampler
}