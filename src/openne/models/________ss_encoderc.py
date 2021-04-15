import torch
import torch.nn as nn
import torch.nn.functional as F
from . import layers

class Encoder(nn.Module):
    def __init__(self, name, dimensions, adj, features, dropout, readout):
        super(Encoder, self).__init__()
        self.dimensions = dimensions
        self.layers = nn.ModuleList()
        self.features = features
        self.nnodes = adj.size()[0]
        self.sigm = nn.Sigmoid()
        self.name = name
        self.readout = readout
        # self.act = nn.PReLU()
        self.act = F.relu
        if name == 'none':
            self.embedding = nn.Embedding(self.nnodes + 1, self.dimensions[-1])
        else:
            for i in range(1, len(self.dimensions)-1):
                self.layers.append(layer_dict[name](self.dimensions[i-1], self.dimensions[i], adj, dropout, act=self.act))
            self.layers.append(layer_dict[name](self.dimensions[-2] * 2, self.dimensions[-1], adj, dropout, act=self.act))

    def embed(self, x):
        if self.name == 'none':
            return self.embedding(x)
        else:
            return x
    
    def forward(self, x):
        """
        special input: graph
        """
        hx = self.embed(x.feat)
        if self.name != 'none':
            for layer in self.layers:
                hx = layer([hx, x.adj])

        if x.typ == 'graph':
            wsize = x.feat.size()[0]
            hx = self.sigm(self.readout(hx)).repeat(wsize, 1)
        return hx

"Layers"

layer_dict = {
    "linear": layers.c.Linear,
    "gcn": layers.c.GraphConvolution,
    "gat": layers.c.GAT,
    "gin": layers.c.GIN
}

