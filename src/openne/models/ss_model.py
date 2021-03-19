from .ss_encoder import Encoder
from .ss_decoder import Decoder
from .ss_sampler import BaseSampler
from .ss_readout import BaseReadOut
from .ss_estimator import BaseEstimator
import torch
import torch.nn as nn
import torch.nn.functional as F


class SSModel(nn.Module):
    def __init__(self, encoder_name, decoder_name, sampler_name, readout_name, estimator_name, enc_dims, graph, supports, features, batch_size, negative_ratio=5, dropout=0, dec_dims=None, norm=False, **kwargs):
        super(SSModel, self).__init__()
        self.enc_dims = enc_dims
        self.dec_dims = dec_dims
        self.graph = graph
        self.supports = supports

        self.layers = nn.ModuleList()
        self.sigm = nn.Sigmoid()
        self.encoder_name = encoder_name
        self.decoder_name = decoder_name
        self.sampler_name = sampler_name
        self.readout_name = readout_name
        self.estimator_name = estimator_name
        self.features = features
        self.normalize = norm
        kwargs.pop('name')
        self.readout = BaseReadOut(self.readout_name)
        self.encoder = Encoder(self.encoder_name, self.enc_dims, self.supports, self.features, dropout, self.readout)
        self.decoder = Decoder(self.decoder_name, self.enc_dims[-1], self.dec_dims)
        self.estimator = BaseEstimator(self.estimator_name)

        self.sampler = BaseSampler(self.sampler_name, self.graph, batch_size, negative_ratio, **kwargs)

    def embed(self, x):
        return self.encoder(x)

    def forward(self, x, pos, neg):
        hx = self.embed(x)
        hpos = self.embed(pos)
        hneg = self.embed(neg)

        if self.normalize:
            hx = F.normalize(hx, dim=-1)
            hpos = F.normalize(hpos, dim=-1)
            hneg = F.normalize(hneg, dim=-1)
        loss = self.estimator(self.decoder(hx, hpos), self.decoder(hx, hneg))
        self.encoder.reset()  # remove full forward record
        return loss
    
    def sample(self):
        return next(self.sampler)
    