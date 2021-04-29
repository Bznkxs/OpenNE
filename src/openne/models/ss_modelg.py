from .ss_encoderg import Encoder
from .ss_decoder import Decoder
from .ss_samplerg import BaseSampler
from .ss_readout import BaseReadOut
from .ss_estimator import BaseEstimator
from .ss_input import model_input, graphinput
from ..utils import getdevice
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Union
from ..dataloaders.graph import Graph
from ..dataloaders.graphs import Graphs
import networkx as nx
from .utils import scipy_coo_to_torch_sparse

class SSModel(nn.Module):
    def __init__(self, encoder_name, decoder_name, sampler_name, readout_name, estimator_name, enc_dims,
                 graphs: Union[Graphs, Graph], features, batch_size, dropout=0, dec_dims=None, norm=False):
        super(SSModel, self).__init__()
        self.enc_dims = enc_dims
        self.dec_dims = dec_dims

        self.layers = nn.ModuleList()
        self.sigm = nn.Sigmoid()
        self.encoder_name = encoder_name
        self.decoder_name = decoder_name
        self.sampler_name = sampler_name
        self.readout_name = readout_name
        self.estimator_name = estimator_name
        self.features = features
        self.normalize = norm
        self.readout = BaseReadOut(self.readout_name, self.enc_dims)
        if isinstance(graphs, Graphs):
            graphs_data = graphs.data
        else:
            feats = torch.from_numpy(graphs.features())
            adjmat = scipy_coo_to_torch_sparse(graphs.adjmat(sparse=True).tocoo())
            edgelist = adjmat._indices()
            weights = adjmat._values()
            graphs_data = [graphinput(feats, None, edgelist, weights)]
        self.graphs_data = graphs_data
        self.num_graphs = len(graphs_data)
        self.graph_sampler = False
        if self.sampler_name in ['dgi', 'mvgrl', 'aug', 'gca']:
            self.graph_sampler = True
        self.mask = False
        if (self.graph_sampler and self.num_graphs > 1) or self.sampler_name == 'gca':
            self.mask = True
        self.outer = self.graph_sampler
        
        self.encoder = Encoder(self.encoder_name, self.enc_dims, graphs, self.features, dropout, self.readout)
        self.decoder = Decoder(self.decoder_name, self.encoder.output_dim, self.dec_dims)
        self.estimator = BaseEstimator(self.estimator_name)
        self.sampler = BaseSampler(self.sampler_name, graphs_data, self.features, batch_size)

    def embed(self, x):
        if self.normalize:
            return F.normalize(self.encoder(x), dim=-1)
        return self.encoder(x)

    def forward(self, x: model_input, pos: model_input, neg: model_input):
        
        def get_anchor():
            pos_mask, neg_mask = None, None
            # repeat
            def repeat(start_idx):
                old_idx = start_idx[0]
                vectors = []
                for i, idx in enumerate(start_idx[1:]):
                    vectors.append(hx[i].repeat(idx-old_idx, 1))
                    old_idx = idx
                return torch.cat(vectors)
            
            def get_mask(start_idx):
                pos_mask = torch.zeros(hx.shape[0], hpos.shape[0])
                neg_mask = torch.ones(hx.shape[0], hpos.shape[0])
                old_idx = start_idx[0]
                if self.sampler_name == 'aug':
                    pos_mask = torch.diag(torch.ones(hx.shape[0]))
                    neg_mask = 1 - pos_mask
                else:
                    for i, idx in enumerate(start_idx[1:]):
                        pos_mask[i][old_idx:idx] = 1
                        neg_mask[i][old_idx:idx] = 0
                        old_idx = idx
                    if neg_mask.sum() == 0:
                        print("all zero neg_mask")
                        print(start_idx)
                        print(neg.num_graphs)
                return pos_mask.to(getdevice()), neg_mask.to(getdevice())
            '''
            if x.typ == x.GRAPHS and pos.typ == x.NODES:
                hxp = repeat(pos.start_idx)
                hxn = repeat(neg.start_idx)
            else:
                hxp = hxn = hx
            '''
            if self.mask:
                pos_mask, neg_mask = get_mask(pos.start_idx)
            hxp = hxn = hx
            return hxp, hxn, pos_mask, neg_mask

        def get_score(anchor, sample):
            h = self.embed(sample)
            return self.decoder(anchor, h)
        hx = self.embed(x)
        hpos = self.embed(pos)
        hneg = self.embed(neg)
        hxp, hxn, pos_mask, neg_mask = get_anchor()
        #print(hx.shape)
        

        pos_score = self.decoder(hxp, hpos, self.outer)
        
        if self.mask:
            neg_score = pos_score
        else:
            neg_score = self.decoder(hxn, hneg, self.outer)
        #print(pos_mask.sum(1), pos_mask.shape)
        #exit(1)
        '''
        if not self.graph_sampler:
            neg_score = self.decoder(hxn, hneg)
            loss = self.estimator(pos_score, neg_score)
        elif self.num_graphs == 1 and self.sampler_name != 'gca':
            neg_score = self.decoder(hxn, hneg)
            loss = self.estimator(pos_score, neg_score)
        else:
            neg_score = self.decoder(hxn, hneg, outer=True)
            loss = self.estimator(pos_score, neg_score, self.graph_sampler)
        '''
        loss = self.estimator(pos_score, neg_score, pos_mask, neg_mask)
        
        # loss = self.estimator(hxp, hxn, hpos, hneg, self.decoder)                                                                                                                                                                                                           )
        self.encoder.reset()
        return loss

    def sample(self):
        return next(self.sampler)
