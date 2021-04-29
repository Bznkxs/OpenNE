import torch
import torch.nn as nn
import torch.nn.functional as F
from . import layers
from .layers.others import FF
from .utils import process_graphs
from ..utils import getdevice
from .ss_input import model_input


class Encoder(nn.Module):
    def __init__(self, name, dimensions, graphs, features, dropout, readout):
        super(Encoder, self).__init__()
        # print("Encoder dimensions", dimensions)
        self.dimensions = dimensions
        self.layers = nn.ModuleList()
        self.sigm = nn.Sigmoid()
        self.name = name
        self.readout = readout
        # self.output_dim = sum(self.dimensions[1:])
        self.output_dim = self.dimensions[-1]
        self.nodesize = getattr(graphs, 'nodesize', 1)
        self.register_buffer('nodelist', torch.arange(self.nodesize))
        # assert self.name != 'none'
        if name == 'none':
            self.embedding = nn.Embedding(self.nodesize, self.dimensions[-1])
        else:
            for i in range(1, len(self.dimensions) - 1):
                self.layers.append(
                    layer_dict[name](self.dimensions[i - 1], self.dimensions[i], None, dropout, act=F.relu))
            self.layers.append(layer_dict[name](self.dimensions[-2], self.dimensions[-1], None, dropout, act=lambda x: x))
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
        adj = x.adj

        if True in torch.isnan(hx):
            print("NaN in input feat!")
            exit(-1)

        # print("encoder:", hx.device, adj.device)
        # adj = x.adj.to_dense().to(getdevice())
        # print(adj.sum(1))
        # exit(1)
        start_idx = x.start_idx

        if x.actual_indices is not None and self.full_embeddings is not None:
            hx = self.full_embeddings[x.actual_indices]
        else:
            hxs = []

            if self.name != 'none':
                for layer in self.layers:
                    hx = layer([hx, adj])
                    hxs.append(hx)
            else:
                hxs = [self.embedding(self.nodelist)] * len(self.dimensions)
                hx = self.embedding(self.nodelist)
            if True in torch.isnan(hx):
                print("NaN in real encoder!", flush=True)
                exit(-1)
            if x.typ == x.GRAPHS:
                # todo: this is a brute-force graph-wise pooling. change this to faster pooling
                nhxs = []

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
                if self.readout == 'jk-net':
                    for hx in hxs:
                        nhxs.append(pooling(hx))
                    hx = self.readout.trans(torch.cat(nhxs, 1))
                else:
                    hx = pooling(hx)
                hx = self.sigm(self.global_d(hx))
            else:
                # hx = torch.cat(hxs, 1)
                hx = self.local_d(hx)
                if x.actual_indices is not None:
                    self.full_embeddings = hx
                    hx = hx[x.actual_indices]
        if True in torch.isnan(hx):
            print("NaN in encoder!", flush=True)
            exit(-1)
        return hx


"Layers"

layer_dict = {
    "linear": layers.c.Linear,
    "gcn": layers.c.GraphConvolution,
    "gat": layers.c.GAT,
    "gin": layers.c.GIN
}
