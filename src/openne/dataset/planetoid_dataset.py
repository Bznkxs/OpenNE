from abc import ABC
from torch_geometric.datasets import Planetoid
import torch_geometric.datasets as datasets
import torch_geometric.transforms as T
from .dataset import *

class TorchGeometricAttributed(NetResources, ABC):
    def __init__(self, name, adapterclass):
        self.name = name
        self.dataset = adapterclass(self.root_dir, name, T.TargetIndegree())
        super(TorchGeometricAttributed, self).__init__(name, None, {'filename': name})
        # edge_attr, edge_index, test_mask, train_mask, val_mask, x, y

    def download(self):
        pass

    def process(self):
        self.G = nx.from_edgelist(self.dataset[0]['edge_index'].t().numpy())
        self.set_node_features(self.dataset[0]['x'].numpy())
        self.set_node_label(self.dataset[0]['y'].numpy())
        self.set_node_features(self.dataset[0]['edge_index'].t().numpy(), self.dataset[0]['edge_attr'].numpy())

    def read(self):
        self.process()

    @classmethod
    def attributed(cls):
        return True

class Cora(TorchGeometricAttributed):
    def __init__(self):
        super(Cora, self).__init__('cora', Planetoid)

    @classmethod
    def weighted(cls):
        return False

    @classmethod
    def directed(cls):
        return False

class CiteSeer(TorchGeometricAttributed):
    def __init__(self):
        super(CiteSeer, self).__init__('citeseer', Planetoid)

    @classmethod
    def weighted(cls):
        return False

    @classmethod
    def directed(cls):
        return False

class PubMed(TorchGeometricAttributed):
    def __init__(self):
        super(PubMed, self).__init__('citeseer', Planetoid)

    @classmethod
    def weighted(cls):
        return False

    @classmethod
    def directed(cls):
        return False

class RedditAdapter(datasets.Reddit):
    def __init__(self, path, dataset, transform):
        super(RedditAdapter, self).__init__(path, transform)

class Reddit(TorchGeometricAttributed):
    def __init__(self):
        super(Reddit, self).__init__('reddit', RedditAdapter)

    @classmethod
    def weighted(cls):
        return False

    @classmethod
    def directed(cls):
        return False