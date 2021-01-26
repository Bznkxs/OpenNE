import torch
import torch.nn as nn
import torch.nn.functional as F
from . import layers
from .utils import process_graphs

class Encoder(nn.Module):
    def __init__(self, name, dimensions, adj, features, dropout, readout):
        super(Encoder, self).__init__()
        self.dimensions = dimensions
        self.layers = nn.ModuleList()
        self.sigm = nn.Sigmoid()
        self.name = name
        self.readout = readout
        assert self.name != 'none'
        for i in range(1, len(self.dimensions)-1):
            self.layers.append(layer_dict[name](self.dimensions[i-1], self.dimensions[i], adj, dropout, act=F.relu))
        self.layers.append(layer_dict[name](self.dimensions[-2], self.dimensions[-1], adj, dropout, act=lambda x: x))

    def forward(self, x):
        """
        encoder for a batch of graphs
        @requires self.name != 'none'
        @param x: model_input, with .feat, .graphs, .typ
        @return:
        """
        hx = torch.cat(x.feat)
        adj, start_idx = process_graphs(x.graphs)


        for layer in self.layers:
            hx = layer([hx, adj])

        if x.typ == 'graphs':
            # todo: this is a brute-force graph-wise pooling. change this to faster pooling
            old_idx = start_idx[0]
            vectors = []
            for idx in start_idx[1:]:
                vectors.append(self.sigm(self.readout(hx[old_idx:idx])).repeat(idx-old_idx, 1))
                old_idx = idx

            hx = torch.cat(vectors)

        return hx

"Layers"

layer_dict = {
    "linear": layers.c.Linear,
    "gcn": layers.c.GraphConvolution,
    "gat": layers.c.GAT,
    "gin": layers.c.GIN
}

