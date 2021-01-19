import torch
import torch.nn as nn
import torch.nn.functional as F
from . import layers

class Encoder(nn.Module):
    def __init__(self, name, dimensions, adj, features, dropout, readout):
        super(Encoder, self).__init__()
        self.dimensions = dimensions
        self.adj = adj
        self.layers = nn.ModuleList()
        self.features = features
        self.nnodes = self.features.size()[0]
        self.sigm = nn.Sigmoid()
        self.name = name
        self.readout = readout
        if name == 'none':
            self.embedding = nn.Embedding(self.nnodes, self.dimensions[-1])
        else:
            for i in range(1, len(self.dimensions)-1):
                self.layers.append(layer_dict[name](self.dimensions[i-1], self.dimensions[i], self.adj, dropout, act=F.relu))
            self.layers.append(layer_dict[name](self.dimensions[-2], self.dimensions[-1], self.adj, dropout, act=lambda x: x))

    def embed(self, x):
        if self.name == 'none':
            return self.embedding(x)
        else:
            return x
    
    def forward(self, x):
        """
        special input: graph
        """
        isgraph = False
        if x.typ == 'graph':
            isgraph = True
            #x = torch.arange(self.nnodes)
        hx = self.embed(x.feat)
        if self.name != 'none':
            for layer in self.layers:
                hx = layer([hx, x.adj])
        if isgraph:
            hx = self.sigm(self.readout(hx))
        return hx

"Layers"

layer_dict = {
    "linear": layers.Linear,
    "gcn": layers.GraphConvolution,
    "gat": layers.GAT,
    "gin": layers.GIN
}

