import random
import tqdm
import time
import torch
import networkx as nx
import numpy as np
from typing import Union, List
from scipy.linalg import fractional_matrix_power, inv
from ..utils import getdevice
from .utils import process_graphs
from .ss_input import model_input, graphinput
from . import ss_sampler
from matplotlib import pyplot as plt

class BaseSampler:
    def __init__(self, name, graph, features, batch_size, negative_ratio=5, **kwargs):
        # super(BaseSampler, self).__init__()
        self.graph = graph
        self.features = features
        self.negative_ratio = negative_ratio
        self.batch_size = batch_size
        self.name = name
        if name in sampler_dict:  # graph sampler
            self.sampler = sampler_dict[name](graph, batch_size=self.batch_size)
        elif name in ss_sampler.sampler_dict:  # node sampler
            self.sampler = NodeSampler(
                ss_sampler.sampler_dict[name](None, None, None, None, None, empty=True),
                graph,
                batch_size=self.batch_size
            )

    def __iter__(self):
        return self.sampler.__iter__()

    def __len__(self):
        return self.sampler.__len__()


def compute_ppr(edge_index, alpha=0.2, self_loop=True):
    adj = torch.sparse_coo_tensor(edge_index, torch.ones(edge_index.shape[1])).to_dense()
    # print("adj:", adj.device)
    a = adj.cpu().numpy()
    if self_loop:
        a = a + np.eye(a.shape[0])  # A^ = A + I_n
    d = np.diag(np.sum(a, 1))  # D^ = Sigma A^_ii
    dinv = fractional_matrix_power(d, -0.5)  # D^(-1/2)
    at = np.matmul(np.matmul(dinv, a), dinv)  # A~ = D^(-1/2) x A^ x D^(-1/2)
    return alpha * inv((np.eye(a.shape[0]) - (1 - alpha) * at))  # a(I_n-(1-a)A~)^-1


def sample_subgraph(graph_data: List[graphinput], n_nodes=None,
                    max_graph_size=None, do_sample=True, permuted_nodes=None):
    """

    @param do_sample: if False, return original graph.
    @param graph_data: a list of N graphs, [anchor, ...], which share the same features and node sampling.
    @param n_nodes: number of nodes in any graph.
    @param max_graph_size: threshold of sampling.
    @param permuted_nodes: optional, provide a permutation
    @return: sub_feats of graph1, [sub_edges of grpah1, sub_edges of graph2...]
    """

    if n_nodes is None:
        n_nodes = len(graph_data[0].x)

    if max_graph_size is None:
        max_graph_size = n_nodes * 1 // 5

    # sample node list
    if do_sample:
        if permuted_nodes is None:
            permuted_nodes = torch.randperm(n_nodes)
    else:
        permuted_nodes = torch.arange(n_nodes)
        max_graph_size = int(1e9)

    map_idx = torch.argsort(permuted_nodes)
    sub_nodes = permuted_nodes[:max_graph_size]

    feats = graph_data[0].x

    sub_feats = feats[sub_nodes].to(getdevice())

    def sample_edges(edges):
        _sub_edges = map_idx[edges]  # permutation
        e_sample = (_sub_edges[0] < max_graph_size) * (_sub_edges[1] < max_graph_size)

        return _sub_edges[:, e_sample]

    sub_edges = [sample_edges(graph.edge_index) for graph in graph_data]
    return sub_feats, sub_edges, permuted_nodes


# https://github.com/Shen-Lab/GraphCL/blob/master/unsupervised_TU/aug.py
def augment_subgraph(graph_data: graphinput, max_graph_size=None):
    n_nodes = len(graph_data.x)
    if max_graph_size is None:
        max_graph_size = n_nodes * 1 // 5
    sub_nodes = [torch.randint(n_nodes, [1]).item()]
    selected = torch.zeros(n_nodes, dtype=torch.bool)
    visited = torch.zeros(n_nodes, dtype=torch.bool)
    edge_index = graph_data.edge_index
    candidate_nodes: List = edge_index[1, edge_index[0] == sub_nodes[0]].tolist()
    selected[sub_nodes] = True
    visited[candidate_nodes] = True
    visited[sub_nodes] = True
    cnt = 0
    while len(sub_nodes) <= max_graph_size:
        cnt += 1
        if cnt > n_nodes:
            break
        if len(candidate_nodes) == 0:
            break
        idx = torch.randint(len(candidate_nodes), [1]).item()
        sample_node = candidate_nodes[idx]
        selected[sample_node] = True
        candidate_nodes[idx] = candidate_nodes[-1]
        candidate_nodes.pop(-1)
        sub_nodes.append(sample_node)
        new_candidates = edge_index[1, edge_index[0] == sample_node]
        new_candidates = new_candidates[visited[new_candidates] == False].tolist()
        visited[new_candidates] = True
        candidate_nodes.extend(new_candidates)
    sub_size = len(sub_nodes)
    permuted_nodes = sub_nodes + [i for i in range(n_nodes) if not selected[i]]
    # print("__", sub_size, max_graph_size)
    sub_feats, sub_edges, _ = sample_subgraph([graph_data], n_nodes, sub_size, permuted_nodes=torch.tensor(permuted_nodes))
    # print("__", n_nodes, sub_size, sub_nodes, sub_edges[0].shape, flush=True)
    return sub_feats, sub_edges[0]


def drop_edges(graph: graphinput, max_edge_size=None):
    """
    @param graph: input graph
    @param max_edge_size: threshold (0.8*n_edges by default)
    @return: feats & edges
    """
    n_edges = graph.edge_index.shape[1]
    if max_edge_size is None:
        max_edge_size = n_edges * 4 // 5
    keep_edges = torch.randperm(n_edges)[:max_edge_size]
    # torch.multinomial(torch.arange(n_edges), max_edge_size,
    #                               replacement=True)
    sub_edges = graph.edge_index[:, keep_edges]
    return graph.x, sub_edges


def drop_nodes(graph: graphinput, max_graph_size=None):
    """
    @param graph: input graph
    @param max_graph_size: threshold
    @return: feats & edges
    """
    n_nodes = len(graph.x)
    if max_graph_size is None:
        max_graph_size = n_nodes * 4 // 5
    subfeats, sub_edges, _ = sample_subgraph([graph], max_graph_size=max_graph_size)
    return subfeats, sub_edges[0]


def mask_attribute(graph: graphinput, mask_size=None,
                   mask_using: Union[None, torch.Tensor] = None):
    n_nodes = len(graph.x)
    if mask_size is None:
        mask_size = n_nodes * 1 // 5
    mask = torch.randperm(n_nodes)[:mask_size]
    # torch.multinomial(torch.arange(n_nodes), mask_size,
    #                         replacement=True)
    #print(mask)
    feats = torch.clone(graph.x)
    if mask_using is None:
        feats[mask] = torch.randn_like(graph.x[mask]) * .5 + .5
    else:
        feats[mask] = mask_using
    return feats, graph.edge_index


# def hard_sample_slicer(graphs: List[graphinput], max_graph_size=5000):
#     num_graphs = len(graphs)
#     iter_head = 0
#     accum_len = 0
#     slice_head = 0
#     ret = []
#     while iter_head <= num_graphs:
#         curlen = len(graphs[iter_head].x)
#         if iter_head == num_graphs or (accum_len > 0 and accum_len + curlen > max_graph_size):
#             i = slice(slice_head, iter_head)
#             ret.append(i)
#             accum_len = 0
#             slice_head = iter_head
#         if iter_head < num_graphs:
#             if curlen <= max_graph_size:
#                 accum_len += curlen
#             else:
#
#         iter_head += 1
#     # print("from sample slicer: ", ret)
#     return ret

class _Sampler:
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
        # print("from sample slicer: ", ret)
        return ret


class NodeSampler(_Sampler):
    def __init__(self, node_sampler: ss_sampler.TripleGenerator, graphs, batch_size):
        # self.anchor_name, self.pos_name, self.neg_name = name.split('-')
        self.node_sampler = node_sampler
        self.sample_size = 5000
        self.graphs = graphs
        self.anchor = self.graphs  # densere aut non densere, illa quaestio
        self.num_graphs = len(graphs)
        self.graphs_diff = []
        self.batch_size = batch_size  # use this!
        # print("sampler batch size =", self.batch_size)
        self.cache = None
        self.sample_subgraph = True

    def sample(self):
        """
        Performs: random pairing and sampling
        Returns values needed for generating (anchor, pos, neg)
        @return: f_pos, f_neg, e_anchor, e_diff, e_neg, e_diffneg, slices
        """
        g_anchor = self.anchor
        feats, edges = [], []
        list_graphs = list(range(self.num_graphs))
        random.shuffle(list_graphs)
        # sample subgraphs
        for i in list_graphs:
            f1, (e1,), _ = sample_subgraph([g_anchor[i]], len(g_anchor[i].x), self.sample_size, self.sample_subgraph)

            feats.append(f1)
            edges.append(e1)

        # get slices
        slices = self.sample_slicer(feats)
        return feats, edges, slices

    def get_sample(self):
        if self.cache is None:
            self.cache = self.sample()
        return self.cache



    @classmethod
    def process_graphs(cls, feats, edges):
        graphs = []
        for i in range(len(feats)):
            graphs.append(graphinput(feats[i], None, edges[i]))
            # g_negdiff = g_neg
        adj, start_idx = process_graphs(graphs, getdevice())
        return adj, start_idx

    def __iter__(self):
        """
        create batch samples
        @return:
        """
        feats, edges, slices = self.get_sample()
        # print(slices)
        for i in slices:  # for each batch
            # print("*slice", i)
            f_pos_d = feats[i]
            adj, start_idx = self.process_graphs(feats[i], edges[i])
            self.node_sampler.adapt(adj.to('cpu'))
            # print("*shape", adj.shape)
            anchor_nodes, pos_nodes, neg_nodes = self.node_sampler[:]
            # print("*indices", len(anchor_nodes), len(pos_nodes), len(neg_nodes))
            # print(anchor_nodes[::197])
            # print(pos_nodes[::197])
            # print(neg_nodes[::197])
            bx = model_input(model_input.NODES, adj, start_idx, f_pos_d, actual_indices=anchor_nodes)
            bpos = model_input(model_input.NODES, adj, start_idx, f_pos_d, actual_indices=pos_nodes)
            bneg = model_input(model_input.NODES, adj, start_idx, f_pos_d, actual_indices=neg_nodes)
            yield [[bx, bpos, bneg]]
        self.cache = None

    def __len__(self):
        """

        @return: number of batches = len(slices) * 2
        """
        _, _, slices = self.get_sample()
        return len(slices)


class GraphSampler(_Sampler):
    def __init__(self, graphs, batch_size):
        # self.anchor_name, self.pos_name, self.neg_name = name.split('-')
        self.sample_size = 5000
        self.graphs = graphs
        self.anchor = self.graphs  # densere aut non densere, illa quaestio
        self.num_graphs = len(graphs)
        self.graphs_diff = []
        self.get_diffused_graphs()
        self.batch_size = batch_size  # use this!
        # print("sampler batch size =", self.batch_size)
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
        # random shuffle anchor and diff
        idx = np.random.permutation(self.num_graphs)
        #g_anchor = [g_anchor[int(i)] for i in idx]
        #g_diff = [g_diff[int(i)] for i in idx]
        # sample subgraphs
        for i in range(self.num_graphs):
            f1, (e1, e2), _ = sample_subgraph([g_anchor[i], g_diff[i]], len(g_anchor[i].x), self.sample_size,
                                           self.sample_subgraph)
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

            #yield bx, bpos, bneg
            #yield bx_r, bpos_r, bneg_r
            yield [[bx, bpos, bneg]]
            yield [[bx_r, bpos_r, bneg_r]]
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
        if self.num_graphs == 1:
            for f in f_pos:
                rp = np.random.permutation(len(f))
                f_neg.append(f[rp])
        else:
            f_neg = f_pos
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
        '''
        f_neg, e_neg, e_negdiff = [], [], []
        for i in range(self.num_graphs):
            if len(self.graphs) == 1:
                negidx = i
            else:
                negidx = np.random.randint(0, len(self.graphs) - 2)
                if negidx == i:
                    negidx += 1
            f_neg.append(f_pos[negidx])
            e_neg.append(e_anchor[negidx])
            e_negdiff.append(e_diff[negidx])
        '''
        f_neg, e_neg, e_negdiff = [], [], []
        if self.num_graphs == 1:
            for f in f_pos:
                rp = np.random.permutation(len(f))
                f_neg.append(f[rp])
        else:
            f_neg = [f for f in f_pos]
        e_neg = [e for e in e_anchor]
        e_negdiff = [e for e in e_diff]
            
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
        add, start_idd = process_graphs(g_diff, getdevice(), normalize=False)
        adn, start_idn = process_graphs(g_neg, getdevice())
        adnd, start_idnd = process_graphs(g_negdiff, getdevice(), normalize=False)
        return adj, add, adn, adnd, start_idx, start_idd, start_idn, start_idnd

def draw_graph_from_feat_edge(feats, edges, layout=None):
    g = nx.DiGraph()
    g.add_nodes_from(torch.arange(len(feats)).tolist())
    g.add_edges_from(edges.t().tolist())
    if layout is None:
        layout = nx.spring_layout(g)
    nx.draw_networkx(g, pos=layout)
    return layout


class AugmentationSampler(DGISampler):

    @classmethod
    def process_graphs(cls, f_pos, f_neg, e_anchor, e_diff, e_neg, e_diffneg):
        g_anchor, g_diff, g_neg, g_negdiff = [], [], [], []
        aug_methods = [mask_attribute, augment_subgraph, drop_edges, drop_nodes]
        f_aug1, f_aug2 = aug_methods[torch.randint(len(aug_methods), [1]).data], aug_methods[torch.randint(len(aug_methods), [1]).data]
        #print(f_aug1, f_aug2)
        for i in range(len(f_pos)):
            g_p = graphinput(f_pos[i], None, e_anchor[i])
            g_n = graphinput(f_neg[i], None, e_neg[i])
            f_a, e_a = f_aug1(g_p)
            f_d, e_d = f_aug2(g_p)
            f_n, e_n = f_aug1(g_n)
            f_dn, e_dn = f_aug2(g_n)

            g_anchor.append(graphinput(f_a, None, e_a))
            g_diff.append(graphinput(f_d, None, e_d))
            g_neg.append(graphinput(f_n, None, e_n))
            g_negdiff.append(graphinput(f_dn, None, e_dn))

        return g_anchor, g_diff, g_neg, g_negdiff

    def get_negative_indices_and_features(self, f_pos, e_anchor, e_diff):
        '''
        f_neg, e_neg, e_negdiff = [], [], []
        for i in range(self.num_graphs):
            if len(self.graphs) == 1:
                negidx = i
            else:
                negidx = np.random.randint(0, len(self.graphs) - 2)
                if negidx == i:
                    negidx += 1
            f_neg.append(f_pos[negidx])
            e_neg.append(e_anchor[negidx])
            e_negdiff.append(e_diff[negidx])
        '''
        f_neg, e_neg, e_negdiff = [], [], []
        if self.num_graphs == 1:
            for f in f_pos:
                rp = np.random.permutation(len(f))
                f_neg.append(f[rp])
        else:
            f_neg = [f for f in f_pos]
        e_neg = [e for e in e_anchor]
        e_negdiff = [e for e in e_diff]
            
        return f_neg, e_neg, e_negdiff

    def __iter__(self):
        """
        create batch samples
        @return:
        """
        f_pos, f_neg, e_anchor, e_diff, e_neg, e_diffneg, slices = self.get_sample()
        for i in slices:  # for each batch
            g_anchor, g_diff, g_neg, g_negdiff = \
                self.process_graphs(f_pos[i], f_neg[i], e_anchor[i],
                                    e_diff[i], e_neg[i], e_diffneg[i])
            # plt.subplot(231)
            # pos = draw_graph_from_feat_edge(f_pos[i][0], e_anchor[i][0])
            # plt.subplot(232)
            # draw_graph_from_feat_edge(g_anchor[0].x, g_anchor[0].edge_index, pos)
            # plt.subplot(233)
            # draw_graph_from_feat_edge(g_diff[0].x, g_diff[0].edge_index, pos)
            # plt.subplot(234)
            # pos = draw_graph_from_feat_edge(f_neg[i][0], e_neg[i][0])
            # plt.subplot(235)
            # draw_graph_from_feat_edge(g_neg[0].x, g_neg[0].edge_index, pos)
            # plt.subplot(236)
            # draw_graph_from_feat_edge(g_negdiff[0].x, g_negdiff[0].edge_index, pos)
            # plt.show()
            f_p = [g.x for g in g_anchor]
            f_d = [g.x for g in g_diff]
            f_n = [g.x for g in g_neg]
            f_nd = [g.x for g in g_negdiff]
            adj, start_idx = process_graphs(g_anchor, getdevice())
            add, start_idd = process_graphs(g_diff, getdevice())
            adn, start_idn = process_graphs(g_neg, getdevice())
            adnd, start_idnd = process_graphs(g_negdiff, getdevice())
            idx = range(len(f_p))
            #start_idx, start_idd, start_idn, start_idnd = idx, idx, idx, idx
            bx = model_input(model_input.GRAPHS, adj, start_idx, f_p)
            bpos = model_input(model_input.GRAPHS, add, start_idd, f_d)
            bneg = model_input(model_input.GRAPHS, adnd, start_idnd, f_nd)

            bx_r = model_input(model_input.GRAPHS, add, start_idd, f_d)
            bpos_r = model_input(model_input.GRAPHS, adj, start_idx, f_p)
            bneg_r = model_input(model_input.GRAPHS, adn, start_idn, f_n)

            yield [[bx, bpos, bneg]]
            yield [[bx_r, bpos_r, bneg_r]]
        self.cache = None


class GCASampler(DGISampler):

    @classmethod
    def process_graphs(cls, f_pos, f_neg, e_anchor, e_diff, e_neg, e_diffneg):
        g_anchor, g_diff = [], []
        aug_methods = [drop_edges, mask_attribute]
        f_aug1, f_aug2 = aug_methods[0], aug_methods[1]
        for i in range(len(f_pos)):
            g_p = graphinput(f_pos[i], None, e_anchor[i])
            f_a, e_a = f_aug1(g_p)
            f_d, e_d = f_aug2(g_p)

            g_anchor.append(graphinput(f_a, None, e_a))
            g_diff.append(graphinput(f_d, None, e_d))

        return g_anchor, g_diff  # adj, add, adj, add, start_idx, start_idd, start_idx, start_idd
    
    def get_negative_indices_and_features(self, f_pos, e_anchor, e_diff):
        return f_pos, e_anchor, e_diff

    def __iter__(self):
        """
        create batch samples
        @return:
        """
        f_pos, f_neg, e_anchor, e_diff, e_neg, e_diffneg, slices = self.get_sample()
        for i in slices:  # for each batch

            # adj, add, adn, adnd, start_idx, start_idd, start_idn, start_idnd \
            g_anchor, g_diff = self.process_graphs(f_pos[i], f_neg[i], e_anchor[i], e_diff[i], e_neg[i], e_diffneg[i])
            f_p = [g.x for g in g_anchor]

            adj, start_idx = process_graphs(g_anchor, getdevice())
            add, start_idd = process_graphs(g_diff, getdevice())
            adn = adj
            adnd = add
            start_idn = start_idx
            start_idnd = start_idd
            anchor_nodes = torch.arange(len(adj))#.repeat(20)
            neg_nodes = torch.randint(high=len(adj) - 1, size=(len(anchor_nodes),))
            neg_nodes[neg_nodes >= anchor_nodes] += 1
            idx = torch.arange(len(adj)+1)
            start_idx, start_idd, start_idn, start_idnd = idx, idx, idx, idx

            bx = model_input(model_input.NODES, adj, start_idx, f_p, actual_indices=anchor_nodes)
            bpos = model_input(model_input.NODES, add, start_idd, f_p, actual_indices=anchor_nodes)
            bneg = model_input(model_input.NODES, adnd, start_idnd, f_p, actual_indices=anchor_nodes)

            bx_r = model_input(model_input.NODES, add, start_idd, f_p, actual_indices=anchor_nodes)
            bpos_r = model_input(model_input.NODES, adj, start_idx, f_p, actual_indices=anchor_nodes)
            bneg_r = model_input(model_input.NODES, adn, start_idn, f_p, actual_indices=anchor_nodes)

            yield [[bx, bpos, bneg]]
            yield [[bx, bpos, bneg_r]]
            yield [[bx_r, bpos_r, bneg]]
            yield [[bx_r, bpos_r, bneg_r]]
        self.cache = None

    def __len__(self):
        """

        @return: number of batches = len(slices) * 2
        """
        _, _, _, _, _, _, slices = self.get_sample()
        return len(slices) * 4


sampler_dict = {
    "dgi": DGISampler,
    "mvgrl": DiffSampler,
    "aug": AugmentationSampler,
    "gca": GCASampler
}
