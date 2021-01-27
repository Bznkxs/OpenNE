from abc import ABC

from torch_geometric.data import DataLoader
from torch_geometric.datasets import TUDataset
from . import Adapter
from sklearn.model_selection import train_test_split
import numpy as np
import networkx as nx
from ..models.utils import process_graphs, torch_sparse_to_scipy_coo
import torch

class Graphs(Adapter, ABC):

    def __init__(self, dataset_name, **kwargs):
        super(Graphs, self).__init__(TUDataset, self.root_dir, name=dataset_name)
        for kw in set(kwargs):
            self.__setattr__(kw, kwargs.get(kw))
        self.num = len(self.data)

    def load_data(self):
        if not self.attributed():
            class Data:
                def __init__(self, x, edge_index, y):
                    self.x = x
                    self.edge_index = edge_index
                    self.y = y
            data = []
            for g in self.data:
                data.append(Data(torch.ones(int(torch.max(g.edge_index)) + 1, 1), g.edge_index, g.y))
            self.data = data
        adj, start_idx = process_graphs(self.data)
        self.set_g(nx.from_scipy_sparse_matrix(torch_sparse_to_scipy_coo(adj)))  # TODO: format conversion


        feat = torch.cat([g.x for g in self.data]).numpy()
        self.set_node_features(featurevectors=feat)

        self.set_node_label(torch.arange(start_idx[-1]).reshape([-1, 1]).tolist())
        self.start_idx = start_idx

    def labels(self):
        return self.data, np.arange(self.num).reshape([-1,1])

    def get_split_data(self, train_percent=None, validate_percent=None, validate_size=None, seed=None):
        """
        TODO: confirm X_train and X_test
        @param train_percent:
        @param validate_percent:
        @param validate_size:
        @param seed:
        @return:
        """
        train_idx, test_idx = train_test_split(np.arange(self.num), train_size=train_percent, random_state=seed, shuffle=False)
        train_idx = torch.from_numpy(train_idx)
        test_idx = torch.from_numpy(test_idx)
        X_train = train_idx.tolist()
        X_test = test_idx.tolist()
        Y_train = [self.data[int(i)].y.tolist() for i in train_idx]
        Y_test = [self.data[int(i)].y.tolist() for i in test_idx]
        return X_train, Y_train, None, None, X_test, Y_test




class MUTAG(Graphs):
    def __init__(self, **kwargs):
        super(MUTAG, self).__init__('MUTAG', **kwargs)
    @classmethod
    def weighted(cls):
        return True

    @classmethod
    def attributed(cls):
        return True

    @classmethod
    def directed(cls):
        return True

"""
PTC-MR, IMDB-BIN, IMDB-MULTI, REDDIT-BIN
"""

class PTC_MR(Graphs):
    def __init__(self, **kwargs):
        super(PTC_MR, self).__init__('PTC-MR', **kwargs)
    @classmethod
    def weighted(cls):
        return True

    @classmethod
    def attributed(cls):
        return True

    @classmethod
    def directed(cls):
        return True

class IMDB_BINARY(Graphs):
    def __init__(self, **kwargs):
        super(IMDB_BINARY, self).__init__('IMDB-BINARY', **kwargs)
    @classmethod
    def weighted(cls):
        return True

    @classmethod
    def attributed(cls):
        return False

    @classmethod
    def directed(cls):
        return True

class IMDB_MULTI(Graphs):
    def __init__(self, **kwargs):
        super(IMDB_MULTI, self).__init__('IMDB-MULTI', **kwargs)

    @classmethod
    def weighted(cls):
        return True

    @classmethod
    def attributed(cls):
        return False

    @classmethod
    def directed(cls):
        return True

class REDDIT_BINARY(Graphs):
    def __init__(self, **kwargs):
        super(REDDIT_BINARY, self).__init__('REDDIT-BINARY', **kwargs)
    @classmethod
    def weighted(cls):
        return True

    @classmethod
    def attributed(cls):
        return False

    @classmethod
    def directed(cls):
        return True
# todo: define other datasets in a similar manner




# import torch
#
# # https://github.com/fanyun-sun/graph-classification/blob/master/diffpool/graph_sampler.py
# class GraphSampler(torch.utils.data.Dataset):
#     ''' Sample graphs and nodes in graph
#     '''
#     def __init__(self, G_list, features='default', normalize=True, assign_feat='default', max_num_nodes=0):
#         self.adj_all = []
#         self.len_all = []
#         self.feature_all = []
#         self.label_all = []
#
#         self.assign_feat_all = []
#
#         if max_num_nodes == 0:
#             self.max_num_nodes = max([G.number_of_nodes() for G in G_list])
#         else:
#             self.max_num_nodes = max_num_nodes
#
#         #if features == 'default':
#         self.feat_dim = G_list[0].node[0]['feat'].shape[0]
#
#         for G in G_list:
#             adj = np.array(nx.to_numpy_matrix(G))
#             if normalize:
#                 sqrt_deg = np.diag(1.0 / np.sqrt(np.sum(adj, axis=0, dtype=float).squeeze()))
#                 adj = np.matmul(np.matmul(sqrt_deg, adj), sqrt_deg)
#             self.adj_all.append(adj)
#             self.len_all.append(G.number_of_nodes())
#             self.label_all.append(G.graph['label'])
#             # feat matrix: max_num_nodes x feat_dim
#             if features == 'default':
#                 f = np.zeros((self.max_num_nodes, self.feat_dim), dtype=float)
#                 for i,u in enumerate(G.nodes()):
#                     f[i,:] = G.node[u]['feat']
#                 self.feature_all.append(f)
#             elif features == 'id':
#                 self.feature_all.append(np.identity(self.max_num_nodes))
#             elif features == 'deg-num':
#                 degs = np.sum(np.array(adj), 1)
#                 degs = np.expand_dims(np.pad(degs, [0, self.max_num_nodes - G.number_of_nodes()], 0),
#                                       axis=1)
#                 self.feature_all.append(degs)
#             elif features == 'deg':
#                 self.max_deg = 10
#                 degs = np.sum(np.array(adj), 1).astype(int)
#                 degs[degs>max_deg] = max_deg
#                 feat = np.zeros((len(degs), self.max_deg + 1))
#                 feat[np.arange(len(degs)), degs] = 1
#                 feat = np.pad(feat, ((0, self.max_num_nodes - G.number_of_nodes()), (0, 0)),
#                         'constant', constant_values=0)
#
#                 f = np.zeros((self.max_num_nodes, self.feat_dim), dtype=float)
#                 for i,u in enumerate(G.nodes()):
#                     f[i,:] = G.node[u]['feat']
#
#                 feat = np.concatenate((feat, f), axis=1)
#
#                 self.feature_all.append(feat)
#             elif features == 'struct':
#                 self.max_deg = 10
#                 degs = np.sum(np.array(adj), 1).astype(int)
#                 degs[degs>10] = 10
#                 feat = np.zeros((len(degs), self.max_deg + 1))
#                 feat[np.arange(len(degs)), degs] = 1
#                 degs = np.pad(feat, ((0, self.max_num_nodes - G.number_of_nodes()), (0, 0)),
#                         'constant', constant_values=0)
#
#                 clusterings = np.array(list(nx.clustering(G).values()))
#                 clusterings = np.expand_dims(np.pad(clusterings,
#                                                     [0, self.max_num_nodes - G.number_of_nodes()],
#                                                     'constant'),
#                                              axis=1)
#                 g_feat = np.hstack([degs, clusterings])
#                 if 'feat' in G.node[0]:
#                     node_feats = np.array([G.node[i]['feat'] for i in range(G.number_of_nodes())])
#                     node_feats = np.pad(node_feats, ((0, self.max_num_nodes - G.number_of_nodes()), (0, 0)),
#                                         'constant')
#                     g_feat = np.hstack([g_feat, node_feats])
#
#                 self.feature_all.append(g_feat)
#
#             if assign_feat == 'id':
#                 self.assign_feat_all.append(
#                         np.hstack((np.identity(self.max_num_nodes), self.feature_all[-1])) )
#             else:
#                 self.assign_feat_all.append(self.feature_all[-1])
#
#         self.feat_dim = self.feature_all[0].shape[1]
#         self.assign_feat_dim = self.assign_feat_all[0].shape[1]
#
#     def __len__(self):
#         return len(self.adj_all)
#
#     def __getitem__(self, idx):
#         adj = self.adj_all[idx]
#         num_nodes = adj.shape[0]
#         adj_padded = np.zeros((self.max_num_nodes, self.max_num_nodes))
#         adj_padded[:num_nodes, :num_nodes] = adj
#
#         # use all nodes for aggregation (baseline)
#
#         return {'adj':adj_padded,
#                 'feats':self.feature_all[idx].copy(),
#                 'label':self.label_all[idx],
#                 'num_nodes': num_nodes,
#                 'assign_feats':self.assign_feat_all[idx].copy()}