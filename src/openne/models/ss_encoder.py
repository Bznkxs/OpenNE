from collections import Iterable
import torch
import time
import torch.nn as nn
import torch.nn.functional as F
from . import layers

# for one graph
class Encoder(nn.Module):
    def __init__(self, name, dimensions, supports, features, dropout, readout):
        super(Encoder, self).__init__()
        self.dimensions = dimensions
        self.supports = supports  # a list; usually supports[0]=adj?
        self.layers = nn.ModuleList()
        self.features = features  # none if name=="none"
        if features is not None:
            self.features = torch.cat(
                (features, torch.rand(1, features.size()[1])))  # +1 rand feature for rand nodes
        self.nnodes = self.supports[0].size()[0]
        self.sigm = nn.Sigmoid()
        self.name = name
        self.readout = readout

        if name == 'none':
            self.embedding = nn.Embedding(self.nnodes + 1, self.dimensions[-1])
        else:
            for i in range(1, len(self.dimensions)-1):
                self.layers.append(layer_dict[name](self.dimensions[i-1], self.dimensions[i], self.supports, dropout, act=F.relu))
            self.layers.append(layer_dict[name](self.dimensions[-2], self.dimensions[-1], self.supports, dropout, act=lambda x: x))
        self.full_embeddings = None

    def embed(self, x):
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
        print("forward")
        t0 = time.time()
        def _forward(x):
            hx = self.embed(x)
            if self.name != 'none':
                for layer in self.layers:
                    hx = layer(hx)
            return hx

        if hasattr(x, "__getitem__") and x[0] == -1:  # must always be graph
            wsize = x.size()[0]
            x = torch.arange(self.nnodes)
            if self.full_embeddings is not None:
                hx = self.full_embeddings
            else:
                hx = _forward(x)
                self.full_embeddings = hx
            hx = self.readout(hx).repeat(wsize, 1)
        elif not hasattr(x, "__getitem__")  and x == -1:  # not a batch
            hx = _forward(torch.arange(self.nnodes))
        else:  # encoding of a list of nodes
            if self.full_embeddings is not None:
                print("fast return")
                hx = self.full_embeddings[x]

            else:
                indices = x
                if requires_adj[self.name] or len(x) > self.nnodes:
                    print("full forward")
                    #  these encoders require a full feature matrix
                    #  (since they need to calculate output reprs with neighboring features)
                    #  and so we must send all nodes into these layers
                    x = torch.arange(self.nnodes)
                    tf1 = time.time()
                    self.full_embeddings = _forward(x)
                    print("forward time = ", time.time() - tf1)
                    hx = self.full_embeddings[indices]
                else:  # these encoders do not depend on other nodes to calculate repr
                    print("normal forward")
                    tf1 = time.time()
                    hx = _forward(x)
                    print("forward time = ", time.time() - tf1)
        print("time = ", time.time() - t0)
        return hx

"Layers"

layer_dict = {
    "linear": layers.Linear,
    "gcn": layers.GraphConvolution,
    "gat": layers.GAT,
    "gin": layers.GIN
}

requires_adj = {
    "none": False,
    "linear": False,
    "gcn": True,
    "gat": False,
    "gin": True
}