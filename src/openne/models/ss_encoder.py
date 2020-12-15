import torch.nn as nn
import torch.nn.functional as F
from . import layers

class Encoder(nn.Module):
    def __init__(self, name, dimensions, adj, features, dropout):
        super(Encoder, self).__init__()
        self.dimensions = dimensions
        self.adj = adj
        self.layers = nn.ModuleList()
        self.features = features
        self.nnodes = self.features.size()[0]
        self.sigm = nn.Sigmoid()
        self.name = name
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
            return self.features[x]
    
    def forward(self, x):
        hx = self.embed(x)
        if self.name != 'none':
            for layer in self.layers:
                hx = layer(hx)
        return hx

"Layers"

layer_dict = {
    "linear": layers.Linear,
    "gcn": layers.GraphConvolution,
    "gat": layers.GAT
}

'''
TO DO:
    ● GCN
    ● GAT
    ● GIN
'''