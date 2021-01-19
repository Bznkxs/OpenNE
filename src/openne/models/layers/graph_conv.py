from .layers import Layer
from ..inits import *
from ..utils import sparse_dropout

import torch

class GraphConvolution(Layer):
    """Graph convolution layer."""

    def __init__(self, input_dim, output_dim, support, dropout=0., *,
                 act=torch.nn.PReLU(), bias=False,
                 num_features_nonzero=0.,
                 sparse_inputs=False,
                 featureless=False, **kwargs):
        super(GraphConvolution, self).__init__(**kwargs)

        self.dropout = dropout  # note we modified the API
        self.act = act
        self.support = support
        self.sparse_inputs = sparse_inputs
        self.featureless = featureless
        self.output_dim = output_dim
        self.input_dim = input_dim
        # helper variable for sparse dropout
        self.num_features_nonzero = num_features_nonzero

        setattr(self, 'weights',  glorot([input_dim, output_dim]))
        if bias:
            self.bias = zeros([output_dim])
        else:
            self.bias = None

        self.batch_norm = torch.nn.BatchNorm1d(self.output_dim)

        if self.logging:
            self._log_vars()

    def forward(self, inputs=None):
        x = inputs[0]
        sup = inputs[1]
        if not self.featureless and self.training:
            # dropout
            if self.sparse_inputs:
                x = sparse_dropout(x, self.dropout, self.num_features_nonzero)
            else:
                x = torch.dropout(x, self.dropout, True)

        # convolve
        output = torch.zeros([sup.size()[0], self.output_dim], device=x.device)
        if not self.featureless:
            pre_sup = torch.mm(x, getattr(self, 'weights'))
        else:
            pre_sup = getattr(self, 'weights')
        support = torch.mm(sup, pre_sup)
        output += support

        # bias
        if self.bias is not None:
            output += self.bias
        # output = self.batch_norm(output)
        return self.act(output)