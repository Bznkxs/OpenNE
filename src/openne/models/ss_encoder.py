from collections import Iterable
import torch
import time
import torch.nn as nn
import torch.nn.functional as F
from .inits import glorot
from . import layers

# for one graph
class Encoder(nn.Module):
    def __init__(self, name, dimensions, supports, features, dropout, readout, **kwargs):
        super(Encoder, self).__init__()
        self.dimensions = dimensions
        self.supports = supports  # a list; usually supports[0]=adj?
        self.layers = nn.ModuleList()
        self.features = features  # none if name=="none"
        if features is not None:
            self.features = features
        self.nnodes = self.supports[0].size()[0]
        self.sigm = nn.Sigmoid()
        self.name = name.lower()
        self.readout = readout
        print("encoder =", name)
        if name == 'none':
            self.embedding = nn.Embedding(self.nnodes, self.dimensions[-1])
        else:
            if 'act' in kwargs:
                kwargs.pop('act')
            for i in range(1, len(self.dimensions)-1):
                self.layers.append(layer_dict[name](self.dimensions[i-1], self.dimensions[i], self.supports, dropout, act=F.relu, **kwargs))
            self.layers.append(layer_dict[name](self.dimensions[-2], self.dimensions[-1], self.supports, dropout, act=lambda x: x, **kwargs))
        self.full_embeddings = None
        self.register_buffer("arange", torch.arange(self.nnodes))



    def embed(self, x):
        print([(n, i.shape, i.device) for n,i in self.named_parameters(recurse=True)])
        print(self.features.device)
        if self.name == 'none':
            return self.embedding(x)
        else:
            return self.features[x]

    def reset(self):
        self.full_embeddings = None

    def forward(self, x):
        """
        x: batch input of indices
        special input: -1 which indicates graph
        """
        print(x.device)
        def _forward(x):
            hx = self.embed(x)
            if self.name != 'none':
                for layer in self.layers:
                    hx = layer(hx)
            return hx

        if hasattr(x, "__getitem__") and x[0] == -1:  # must always be graph
            wsize = x.size()[0]
            x = self.arange
            if self.full_embeddings is not None:
                hx = self.full_embeddings
            else:
                hx = _forward(x)
                self.full_embeddings = hx
            hx = self.readout(hx).repeat(wsize, 1)
        else:  # encoding of a list of nodes
            if self.full_embeddings is not None:
                hx = self.full_embeddings[x]

            else:
                indices = x
                if requires_full_embeddings[self.name] or len(x) > self.nnodes:
                    #  these encoders require a full feature matrix
                    #  (since they need to calculate output reprs with neighboring features)
                    #  and so we must send all nodes into these layers
                    x = self.arange
                    if self.name == "none":
                        return self.embed(x)[indices]
                    self.full_embeddings = _forward(x)
                    hx = self.full_embeddings[indices]
                else:  # these encoders do not depend on other nodes to calculate repr
                    hx = _forward(x)
        return hx

        # # stage 1: status mark
        # graph = (x[0] == -1)  # assume -1 denotes graph
        # need_calculation = (self.name != 'none' and self.full_embeddings is None)
        # wsize = x.size()[0]
        #
        # # stage 2: transform input
        # indices = x
        # full_forward = False
        # if graph or need_calculation and (requires_full_embeddings[self.name] or len(x) >= self.nnodes):  # full forward
        #     #  these encoders require a full feature matrix
        #     #  (since they need to calculate output reprs with neighboring features)
        #     #  and so we must send all nodes into these layers
        #     full_forward = True
        #     x = torch.arange(self.nnodes)
        #
        # # stage 3: get embeddings
        # if not need_calculation:
        #     if self.full_embeddings is not None:
        #         hx = self.full_embeddings[x]
        #     else:
        #         hx = self.embed(x)
        # else:
        #     hx = self.embed(x)
        #     for layer in self.layers:
        #         hx = layer(hx)
        #     if full_forward:  # update full embeddings
        #         self.full_embeddings = hx
        #
        # # stage 4: restore input indices (including graph)
        # if graph:
        #     hx = self.readout(hx).repeat(wsize, 1)
        # elif full_forward:
        #     hx = hx[indices]
        # return hx





"Layers"

layer_dict = {
    "linear": layers.Linear,
    "gcn": layers.GraphConvolution,
    "gat": layers.GAT,
    "gin": layers.GIN
}

requires_full_embeddings = {
    "none": False,
    "linear": False,
    "gcn": True,
    "gat": True,
    "gin": True
}