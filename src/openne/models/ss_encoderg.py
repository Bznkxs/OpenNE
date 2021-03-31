import torch
import torch.nn as nn
import torch.nn.functional as F
from . import layers
from .layers.others import FF
from .utils import process_graphs
from ..utils import getdevice
from .ss_input import model_input

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
        self.full_embeddings = None
        self.init_emb()

    def reset(self):
        self.full_embeddings = None

    def init_emb(self):
        for m in self.modules():
            if isinstance(m, nn.Linear):
                torch.nn.init.xavier_uniform_(m.weight.data)
                if m.bias is not None:
                    m.bias.data.fill_(0.0)

    def forward(self, x: model_input):
        """
        encoder for a batch of graphs
        @requires self.name != 'none'
        @param x: model_input, with .feat, .adj, .start_idx, .typ
        @return:
        """
        hx = torch.cat(x.feat)
        # print(hx.shape)
        adj = x.adj
        # print("encoder:", hx.device, adj.device)
        # adj = x.adj.to_dense().to(getdevice())
        start_idx = x.start_idx

        if x.actual_indices is not None:
            if self.full_embeddings is not None:
                hx = self.full_embeddings[x.actual_indices]
                return hx

        # hxs = []
        for layer in self.layers:
            hx = layer([hx, adj])
            # hxs.append(hx)

        if x.typ == x.GRAPHS:
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
                    vectors.append(self.readout(hx[old_idx:idx]).repeat(repeat, 1))
                    old_idx = idx
                return torch.cat(vectors).to(getdevice())

            # for hx in hxs:
            #     nhxs.append(pooling(hx))
            #
            # hx = torch.cat(nhxs, 1)
            hx = pooling(hx)
            hx = self.global_d(hx)
        else:
            # hx = torch.cat(hxs, 1)
            hx = self.local_d(hx)

            if x.actual_indices is not None:
                self.full_embeddings = hx
                hx = hx[x.actual_indices]
        # print(hx.shape)
        return hx


"Layers"

layer_dict = {
    "linear": layers.c.Linear,
    "gcn": layers.c.GraphConvolution,
    "gat": layers.c.GAT,
    "gin": layers.c.GIN
}
