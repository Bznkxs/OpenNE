from .layers import Layer
from ..inits import *
from ..utils import sparse_dropout

import torch


class Linear(Layer):
    """Linear layer."""

    def __init__(self, input_dim, output_dim, adj=None, dropout=0., num_features_nonzero=0.,
                 sparse_inputs=False, act=torch.relu, bias=False, **kwargs):
        super(Linear, self).__init__(**kwargs)

        self.dropout = dropout  # note we modified the API
        self.act = act
        self.adj = adj
        self.sparse_inputs = sparse_inputs
        self.output_dim = output_dim
        self.input_dim = input_dim
        # helper variable for sparse dropout
        self.num_features_nonzero = num_features_nonzero
        self.logging = False

        self.weight = torch.nn.Parameter(torch.zeros(input_dim, output_dim), requires_grad=True)

        if bias:
            self.bias = zeros([output_dim])
        else:
            self.bias = None
        self.reset_parameters()

    def reset_parameters(self):
        torch.nn.init.xavier_uniform_(self.weight)

    def forward(self, inputs):
        x = inputs
        if self.training:
            # dropout
            if self.sparse_inputs:
                x = sparse_dropout(x, self.dropout, self.num_features_nonzero)
            else:
                x = torch.dropout(x, self.dropout, True)


        pre_sup = torch.mm(x, self.weight)
        output = pre_sup

        # bias
        if self.bias is not None:
            output += self.bias
        return self.act(output)

    def __repr__(self):
        return self.name + '(' + str(self.input_dim) + '->' + str(self.output_dim) + ')'
