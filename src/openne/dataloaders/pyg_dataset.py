from abc import ABC

from torch_geometric.datasets import CitationFull as pyg_CitationFull, \
    WikiCS as pyg_WikiCS, Coauthor as pyg_Coauthor, Amazon as pyg_Amazon
from . import Adapter
from sklearn.model_selection import train_test_split
import numpy as np
import networkx as nx
from ..models.utils import process_graphs, torch_sparse_to_scipy_coo, getdevice
import torch
from tqdm import tqdm


class PyG(Adapter, ABC):
    def __init__(self, dataset_class, dataset_args, **kwargs):
        # print("Init dataset.")
        super().__init__(dataset_class, self.root_dir, **dataset_args)
        # print("tesatad tinI.")
        for kw in set(kwargs):
            self.__setattr__(kw, kwargs.get(kw))
        # self.num = len(self.data)

    def load_data(self):
        self.debug("Load data.", flush=True)
        if not self.attributed():
            self.debug("Not self.attributed(): set attribute as 1", flush=True)
        self.data = self.data[0]
        new_graph = nx.DiGraph()
        new_graph.add_nodes_from(np.arange(len(self.data.x)))
        new_graph.add_edges_from(self.data.edge_index.t().numpy())
        self.set_g(new_graph)
        # print("g set (?)")

        feat = self.data.x.numpy()

        # print("feat set")

        self.set_node_features(featurevectors=feat)

        # print("node features set")

        self.set_node_label(torch.arange(len(self.data.x)).reshape([-1, 1]).tolist())

        # print("node label set")

        # print("loaddata() finished.")



class DBLP(PyG):
    def __init__(self, **kwargs):
        super().__init__(pyg_CitationFull, {'name':'dblp'}, **kwargs)
    @classmethod
    def weighted(cls):
        return False

    @classmethod
    def attributed(cls):
        return True

    @classmethod
    def directed(cls):
        return True


class Coauthor_CS(PyG):
    def __init__(self, **kwargs):
        super().__init__(pyg_Coauthor, {'name':'cs'}, **kwargs)

    @classmethod
    def weighted(cls):
        return False

    @classmethod
    def attributed(cls):
        return True

    @classmethod
    def directed(cls):
        return True

class Coauthor_Phy(PyG):
    def __init__(self, **kwargs):
        super().__init__(pyg_Coauthor, {'name':'physics'}, **kwargs)

    @classmethod
    def weighted(cls):
        return False

    @classmethod
    def attributed(cls):
        return True

    @classmethod
    def directed(cls):
        return True

class WikiCS(PyG):
    def __init__(self, **kwargs):
        super().__init__(pyg_WikiCS, {}, **kwargs)

    @classmethod
    def weighted(cls):
        return False

    @classmethod
    def attributed(cls):
        return True

    @classmethod
    def directed(cls):
        return True

class Amazon_Computers(PyG):
    def __init__(self, **kwargs):
        super().__init__(pyg_Amazon, {'name':'computers'}, **kwargs)

    @classmethod
    def weighted(cls):
        return False

    @classmethod
    def attributed(cls):
        return True

    @classmethod
    def directed(cls):
        return True


class Amazon_Photo(PyG):
    def __init__(self, **kwargs):
        super().__init__(pyg_Amazon, {'name':'photo'}, **kwargs)

    @classmethod
    def weighted(cls):
        return False

    @classmethod
    def attributed(cls):
        return True

    @classmethod
    def directed(cls):
        return True
