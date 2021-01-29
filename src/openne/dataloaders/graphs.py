from abc import ABC

from . import Adapter
from sklearn.model_selection import train_test_split
import numpy as np
import networkx as nx
from ..models.utils import process_graphs, torch_sparse_to_scipy_coo
import torch


##################### following from torch_geometric (to avoid tedious installation) ###################

import re
import copy
import logging
import os.path as osp

import torch.utils.data

import os
import errno


def makedirs(path):
    try:
        os.makedirs(osp.expanduser(osp.normpath(path)))
    except OSError as e:
        if e.errno != errno.EEXIST and osp.isdir(path):
            raise e


def to_list(x):
    if not isinstance(x, (tuple, list)):
        x = [x]
    return x


def files_exist(files):
    return len(files) != 0 and all(osp.exists(f) for f in files)


def __repr__(obj):
    if obj is None:
        return 'None'
    return re.sub('(<.*?)\\s.*(>)', r'\1\2', obj.__repr__())


class Dataset(torch.utils.data.Dataset):
    r"""Dataset base class for creating graph datasets.
    See `here <https://pytorch-geometric.readthedocs.io/en/latest/notes/
    create_dataset.html>`__ for the accompanying tutorial.

    Args:
        root (string, optional): Root directory where the dataset should be
            saved. (optional: :obj:`None`)
        transform (callable, optional): A function/transform that takes in an
            :obj:`torch_geometric.data.Data` object and returns a transformed
            version. The data object will be transformed before every access.
            (default: :obj:`None`)
        pre_transform (callable, optional): A function/transform that takes in
            an :obj:`torch_geometric.data.Data` object and returns a
            transformed version. The data object will be transformed before
            being saved to disk. (default: :obj:`None`)
        pre_filter (callable, optional): A function that takes in an
            :obj:`torch_geometric.data.Data` object and returns a boolean
            value, indicating whether the data object should be included in the
            final dataset. (default: :obj:`None`)
    """
    @property
    def raw_file_names(self):
        r"""The name of the files to find in the :obj:`self.raw_dir` folder in
        order to skip the download."""
        raise NotImplementedError

    @property
    def processed_file_names(self):
        r"""The name of the files to find in the :obj:`self.processed_dir`
        folder in order to skip the processing."""
        raise NotImplementedError

    def download(self):
        r"""Downloads the dataset to the :obj:`self.raw_dir` folder."""
        raise NotImplementedError

    def process(self):
        r"""Processes the dataset to the :obj:`self.processed_dir` folder."""
        raise NotImplementedError

    def len(self):
        raise NotImplementedError

    def get(self, idx):
        r"""Gets the data object at index :obj:`idx`."""
        raise NotImplementedError

    def __init__(self, root=None, transform=None, pre_transform=None,
                 pre_filter=None):
        super(Dataset, self).__init__()

        if isinstance(root, str):
            root = osp.expanduser(osp.normpath(root))

        self.root = root
        self.transform = transform
        self.pre_transform = pre_transform
        self.pre_filter = pre_filter
        self.__indices__ = None

        if 'download' in self.__class__.__dict__.keys():
            self._download()

        if 'process' in self.__class__.__dict__.keys():
            self._process()

    def indices(self):
        if self.__indices__ is not None:
            return self.__indices__
        else:
            return range(len(self))

    @property
    def raw_dir(self):
        return osp.join(self.root, 'raw')

    @property
    def processed_dir(self):
        return osp.join(self.root, 'processed')

    @property
    def num_node_features(self):
        r"""Returns the number of features per node in the dataset."""
        return self[0].num_node_features

    @property
    def num_features(self):
        r"""Alias for :py:attr:`~num_node_features`."""
        return self.num_node_features

    @property
    def num_edge_features(self):
        r"""Returns the number of features per edge in the dataset."""
        return self[0].num_edge_features

    @property
    def raw_paths(self):
        r"""The filepaths to find in order to skip the download."""
        files = to_list(self.raw_file_names)
        return [osp.join(self.raw_dir, f) for f in files]

    @property
    def processed_paths(self):
        r"""The filepaths to find in the :obj:`self.processed_dir`
        folder in order to skip the processing."""
        files = to_list(self.processed_file_names)
        return [osp.join(self.processed_dir, f) for f in files]

    def _download(self):
        if files_exist(self.raw_paths):  # pragma: no cover
            return

        makedirs(self.raw_dir)
        self.download()

    def _process(self):
        f = osp.join(self.processed_dir, 'pre_transform.pt')
        if osp.exists(f) and torch.load(f) != __repr__(self.pre_transform):
            logging.warning(
                'The `pre_transform` argument differs from the one used in '
                'the pre-processed version of this dataset. If you really '
                'want to make use of another pre-processing technique, make '
                'sure to delete `{}` first.'.format(self.processed_dir))
        f = osp.join(self.processed_dir, 'pre_filter.pt')
        if osp.exists(f) and torch.load(f) != __repr__(self.pre_filter):
            logging.warning(
                'The `pre_filter` argument differs from the one used in the '
                'pre-processed version of this dataset. If you really want to '
                'make use of another pre-fitering technique, make sure to '
                'delete `{}` first.'.format(self.processed_dir))

        if files_exist(self.processed_paths):  # pragma: no cover
            return

        print('Processing...')

        makedirs(self.processed_dir)
        self.process()

        path = osp.join(self.processed_dir, 'pre_transform.pt')
        torch.save(__repr__(self.pre_transform), path)
        path = osp.join(self.processed_dir, 'pre_filter.pt')
        torch.save(__repr__(self.pre_filter), path)

        print('Done!')

    def __len__(self):
        r"""The number of examples in the dataset."""
        if self.__indices__ is not None:
            return len(self.__indices__)
        return self.len()

    def __getitem__(self, idx):
        r"""Gets the data object at index :obj:`idx` and transforms it (in case
        a :obj:`self.transform` is given).
        In case :obj:`idx` is a slicing object, *e.g.*, :obj:`[2:5]`, a list, a
        tuple, a  LongTensor or a BoolTensor, will return a subset of the
        dataset at the specified indices."""
        if isinstance(idx, int):
            data = self.get(self.indices()[idx])
            data = data if self.transform is None else self.transform(data)
            return data
        else:
            return self.index_select(idx)

    def index_select(self, idx):
        indices = self.indices()

        if isinstance(idx, slice):
            indices = indices[idx]
        elif torch.is_tensor(idx):
            if idx.dtype == torch.long:
                if len(idx.shape) == 0:
                    idx = idx.unsqueeze(0)
                return self.index_select(idx.tolist())
            elif idx.dtype == torch.bool or idx.dtype == torch.uint8:
                return self.index_select(
                    idx.nonzero(as_tuple=False).flatten().tolist())
        elif isinstance(idx, list) or isinstance(idx, tuple):
            indices = [indices[i] for i in idx]
        else:
            raise IndexError(
                'Only integers, slices (`:`), list, tuples, and long or bool '
                'tensors are valid indices (got {}).'.format(
                    type(idx).__name__))

        dataset = copy.copy(self)
        dataset.__indices__ = indices
        return dataset

    def shuffle(self, return_perm=False):
        r"""Randomly shuffles the examples in the dataset.

        Args:
            return_perm (bool, optional): If set to :obj:`True`, will
                additionally return the random permutation used to shuffle the
                dataset. (default: :obj:`False`)
        """
        perm = torch.randperm(len(self))
        dataset = self.index_select(perm)
        return (dataset, perm) if return_perm is True else dataset

    def __repr__(self):  # pragma: no cover
        return f'{self.__class__.__name__}({len(self)})'

import copy
from itertools import repeat, product


class InMemoryDataset(Dataset):
    r"""Dataset base class for creating graph datasets which fit completely
    into CPU memory.
    See `here <https://pytorch-geometric.readthedocs.io/en/latest/notes/
    create_dataset.html#creating-in-memory-datasets>`__ for the accompanying
    tutorial.

    Args:
        root (string, optional): Root directory where the dataset should be
            saved. (default: :obj:`None`)
        transform (callable, optional): A function/transform that takes in an
            :obj:`torch_geometric.data.Data` object and returns a transformed
            version. The data object will be transformed before every access.
            (default: :obj:`None`)
        pre_transform (callable, optional): A function/transform that takes in
            an :obj:`torch_geometric.data.Data` object and returns a
            transformed version. The data object will be transformed before
            being saved to disk. (default: :obj:`None`)
        pre_filter (callable, optional): A function that takes in an
            :obj:`torch_geometric.data.Data` object and returns a boolean
            value, indicating whether the data object should be included in the
            final dataset. (default: :obj:`None`)
    """
    @property
    def raw_file_names(self):
        r"""The name of the files to find in the :obj:`self.raw_dir` folder in
        order to skip the download."""
        raise NotImplementedError

    @property
    def processed_file_names(self):
        r"""The name of the files to find in the :obj:`self.processed_dir`
        folder in order to skip the processing."""
        raise NotImplementedError

    def download(self):
        r"""Downloads the dataset to the :obj:`self.raw_dir` folder."""
        raise NotImplementedError

    def process(self):
        r"""Processes the dataset to the :obj:`self.processed_dir` folder."""
        raise NotImplementedError

    def __init__(self, root=None, transform=None, pre_transform=None,
                 pre_filter=None):
        super(InMemoryDataset, self).__init__(root, transform, pre_transform,
                                              pre_filter)
        self.data, self.slices = None, None
        self.__data_list__ = None

    @property
    def num_classes(self):
        r"""The number of classes in the dataset."""
        y = self.data.y
        return y.max().item() + 1 if y.dim() == 1 else y.size(1)

    def len(self):
        for item in self.slices.values():
            return len(item) - 1
        return 0

    def get(self, idx):
        if hasattr(self, '__data_list__'):
            if self.__data_list__ is None:
                self.__data_list__ = self.len() * [None]
            else:
                data = self.__data_list__[idx]
                if data is not None:
                    return copy.copy(data)

        data = self.data.__class__()
        if hasattr(self.data, '__num_nodes__'):
            data.num_nodes = self.data.__num_nodes__[idx]

        for key in self.data.keys:
            item, slices = self.data[key], self.slices[key]
            start, end = slices[idx].item(), slices[idx + 1].item()
            if torch.is_tensor(item):
                s = list(repeat(slice(None), item.dim()))
                s[self.data.__cat_dim__(key, item)] = slice(start, end)
            elif start + 1 == end:
                s = slices[start]
            else:
                s = slice(start, end)
            data[key] = item[s]

        if hasattr(self, '__data_list__'):
            self.__data_list__[idx] = copy.copy(data)

        return data

    @staticmethod
    def collate(data_list):
        r"""Collates a python list of data objects to the internal storage
        format of :class:`torch_geometric.data.InMemoryDataset`."""
        keys = data_list[0].keys
        data = data_list[0].__class__()

        for key in keys:
            data[key] = []
        slices = {key: [0] for key in keys}

        for item, key in product(data_list, keys):
            data[key].append(item[key])
            if torch.is_tensor(item[key]):
                s = slices[key][-1] + item[key].size(
                    item.__cat_dim__(key, item[key]))
            else:
                s = slices[key][-1] + 1
            slices[key].append(s)

        if hasattr(data_list[0], '__num_nodes__'):
            data.__num_nodes__ = []
            for item in data_list:
                data.__num_nodes__.append(item.num_nodes)

        for key in keys:
            item = data_list[0][key]
            if torch.is_tensor(item) and len(data_list) > 1:
                data[key] = torch.cat(data[key],
                                      dim=data.__cat_dim__(key, item))
            elif torch.is_tensor(item):  # Don't duplicate attributes...
                data[key] = data[key][0]
            elif isinstance(item, int) or isinstance(item, float):
                data[key] = torch.tensor(data[key])

            slices[key] = torch.tensor(slices[key], dtype=torch.long)

        return data, slices

    def copy(self, idx=None):
        if idx is None:
            data_list = [self.get(i) for i in range(len(self))]
        else:
            data_list = [self.get(i) for i in idx]
        dataset = copy.copy(self)
        dataset.__indices__ = None
        dataset.__data_list == data_list
        dataset.data, dataset.slices = self.collate(data_list)
        return dataset
import os
import shutil

import torch
from torch_geometric.data import InMemoryDataset, download_url, extract_zip
from torch_geometric.io import read_tu_data


class TUDataset(InMemoryDataset):
    r"""A variety of graph kernel benchmark datasets, *.e.g.* "IMDB-BINARY",
    "REDDIT-BINARY" or "PROTEINS", collected from the `TU Dortmund University
    <https://chrsmrrs.github.io/datasets>`_.
    In addition, this dataset wrapper provides `cleaned dataset versions
    <https://github.com/nd7141/graph_datasets>`_ as motivated by the
    `"Understanding Isomorphism Bias in Graph Data Sets"
    <https://arxiv.org/abs/1910.12091>`_ paper, containing only non-isomorphic
    graphs.

    .. note::
        Some datasets may not come with any node labels.
        You can then either make use of the argument :obj:`use_node_attr`
        to load additional continuous node attributes (if present) or provide
        synthetic node features using transforms such as
        like :class:`torch_geometric.transforms.Constant` or
        :class:`torch_geometric.transforms.OneHotDegree`.

    Args:
        root (string): Root directory where the dataset should be saved.
        name (string): The `name
            <https://chrsmrrs.github.io/datasets/docs/datasets/>`_ of the
            dataset.
        transform (callable, optional): A function/transform that takes in an
            :obj:`torch_geometric.data.Data` object and returns a transformed
            version. The data object will be transformed before every access.
            (default: :obj:`None`)
        pre_transform (callable, optional): A function/transform that takes in
            an :obj:`torch_geometric.data.Data` object and returns a
            transformed version. The data object will be transformed before
            being saved to disk. (default: :obj:`None`)
        pre_filter (callable, optional): A function that takes in an
            :obj:`torch_geometric.data.Data` object and returns a boolean
            value, indicating whether the data object should be included in the
            final dataset. (default: :obj:`None`)
        use_node_attr (bool, optional): If :obj:`True`, the dataset will
            contain additional continuous node attributes (if present).
            (default: :obj:`False`)
        use_edge_attr (bool, optional): If :obj:`True`, the dataset will
            contain additional continuous edge attributes (if present).
            (default: :obj:`False`)
        cleaned: (bool, optional): If :obj:`True`, the dataset will
            contain only non-isomorphic graphs. (default: :obj:`False`)
    """

    url = 'https://www.chrsmrrs.com/graphkerneldatasets'
    cleaned_url = ('https://raw.githubusercontent.com/nd7141/'
                   'graph_datasets/master/datasets')

    def __init__(self, root, name, transform=None, pre_transform=None,
                 pre_filter=None, use_node_attr=False, use_edge_attr=False,
                 cleaned=False):
        self.name = name
        self.cleaned = cleaned
        super(TUDataset, self).__init__(root, transform, pre_transform,
                                        pre_filter)
        self.data, self.slices = torch.load(self.processed_paths[0])
        if self.data.x is not None and not use_node_attr:
            num_node_attributes = self.num_node_attributes
            self.data.x = self.data.x[:, num_node_attributes:]
        if self.data.edge_attr is not None and not use_edge_attr:
            num_edge_attributes = self.num_edge_attributes
            self.data.edge_attr = self.data.edge_attr[:, num_edge_attributes:]

    @property
    def raw_dir(self):
        name = 'raw{}'.format('_cleaned' if self.cleaned else '')
        return osp.join(self.root, self.name, name)

    @property
    def processed_dir(self):
        name = 'processed{}'.format('_cleaned' if self.cleaned else '')
        return osp.join(self.root, self.name, name)

    @property
    def num_node_labels(self):
        if self.data.x is None:
            return 0
        for i in range(self.data.x.size(1)):
            x = self.data.x[:, i:]
            if ((x == 0) | (x == 1)).all() and (x.sum(dim=1) == 1).all():
                return self.data.x.size(1) - i
        return 0

    @property
    def num_node_attributes(self):
        if self.data.x is None:
            return 0
        return self.data.x.size(1) - self.num_node_labels

    @property
    def num_edge_labels(self):
        if self.data.edge_attr is None:
            return 0
        for i in range(self.data.edge_attr.size(1)):
            if self.data.edge_attr[:, i:].sum() == self.data.edge_attr.size(0):
                return self.data.edge_attr.size(1) - i
        return 0

    @property
    def num_edge_attributes(self):
        if self.data.edge_attr is None:
            return 0
        return self.data.edge_attr.size(1) - self.num_edge_labels

    @property
    def raw_file_names(self):
        names = ['A', 'graph_indicator']
        return ['{}_{}.txt'.format(self.name, name) for name in names]

    @property
    def processed_file_names(self):
        return 'data.pt'

    def download(self):
        url = self.cleaned_url if self.cleaned else self.url
        folder = osp.join(self.root, self.name)
        path = download_url('{}/{}.zip'.format(url, self.name), folder)
        extract_zip(path, folder)
        os.unlink(path)
        shutil.rmtree(self.raw_dir)
        os.rename(osp.join(folder, self.name), self.raw_dir)

    def process(self):
        self.data, self.slices = read_tu_data(self.raw_dir, self.name)

        if self.pre_filter is not None:
            data_list = [self.get(idx) for idx in range(len(self))]
            data_list = [data for data in data_list if self.pre_filter(data)]
            self.data, self.slices = self.collate(data_list)

        if self.pre_transform is not None:
            data_list = [self.get(idx) for idx in range(len(self))]
            data_list = [self.pre_transform(data) for data in data_list]
            self.data, self.slices = self.collate(data_list)

        torch.save((self.data, self.slices), self.processed_paths[0])

    def __repr__(self):
        return '{}({})'.format(self.name, len(self))

############################ above from torch_geometric ##############################













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
        return self.data, [g.y.tolist() for g in self.data]

    def get_split_data(self, train_percent=None, validate_percent=None, validate_size=None, seed=None):
        """
        TODO: confirm X_train and X_test
        @param train_percent:
        @param validate_percent:
        @param validate_size:
        @param seed:
        @return:
        """
        train_idx, test_idx = train_test_split(np.arange(self.num), train_size=train_percent, random_state=seed, shuffle=True)
        train_idx = torch.from_numpy(train_idx)
        test_idx = torch.from_numpy(test_idx)
        X_train = train_idx.tolist()
        X_test = test_idx.tolist()
        Y_train = [self.data[int(i)].y.tolist() for i in train_idx]
        Y_test = [self.data[int(i)].y.tolist() for i in test_idx]
        # print("TRAIN", Y_train)
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