import torch
import torch.nn as nn
import torch.nn.functional as F
from . import layers
from .layers.others import FF
from .utils import process_graphs


class Encoder(nn.Module):
    def __init__(self, name, dimensions, adj, features, dropout, readout):
        super(Encoder, self).__init__()
        print("Encoder dimensions", dimensions)
        self.dimensions = dimensions
        self.layers = nn.ModuleList()
        self.sigm = nn.Sigmoid()
        self.name = name
        self.readout = readout
        # self.output_dim = sum(self.dimensions[1:])
        self.output_dim = self.dimensions[-1]
        assert self.name != 'none'
        for i in range(1, len(self.dimensions) - 1):
            self.layers.append(layer_dict[name](self.dimensions[i - 1], self.dimensions[i], adj, dropout, act=F.relu))
        self.layers.append(layer_dict[name](self.dimensions[-2], self.dimensions[-1], adj, dropout, act=lambda x: x))
        self.local_d = FF(self.output_dim)
        self.global_d = FF(self.output_dim)
        self.init_emb()

    def init_emb(self):
        for m in self.modules():
            if isinstance(m, nn.Linear):
                torch.nn.init.xavier_uniform_(m.weight.data)
                if m.bias is not None:
                    m.bias.data.fill_(0.0)

    def forward(self, x):
        """
        encoder for a batch of graphs
        @requires self.name != 'none'
        @param x: model_input, with .feat, .adj, .start_idx, .typ
        @return:
        """
        hx = torch.cat(x.feat)
        adj = x.adj
        start_idx = x.start_idx

        hxs = []
        for layer in self.layers:
            hx = layer([hx, adj])
            hxs.append(hx)

        if x.typ == 'graphs':
            # todo: this is a brute-force graph-wise pooling. change this to faster pooling
            # nhxs = []

            def pooling(hx):
                old_idx = start_idx[0]
                vectors = []
                for idx in start_idx[1:]:
                    if x.repeat:
                        repeat = idx - old_idx
                    else:
                        repeat = 1
                    vectors.append(self.sigm(self.readout(hx[old_idx:idx])).repeat(repeat, 1))
                    old_idx = idx
                return torch.cat(vectors)

            # for hx in hxs:
            #     nhxs.append(pooling(hx))
            #
            # hx = torch.cat(nhxs, 1)
            hx = pooling(hx)
            hx = self.global_d(hx)
        else:
            # hx = torch.cat(hxs, 1)
            hx = self.local_d(hx)
        return hx


"Layers"

layer_dict = {
    "linear": layers.c.Linear,
    "gcn": layers.c.GraphConvolution,
    "gat": layers.c.GAT,
    "gin": layers.c.GIN
}
