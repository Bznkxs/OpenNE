from .layers import Layer
from ..utils import sparse_dropout
from ..inits import zeros
import torch

class GIN(Layer):
    """
    output = MLP((1+eps)input + sum(input))
    """

    def __init__(self, input_dim, output_dim, adj,
                 dropout=0., sparse_inputs=False,
                 act=torch.relu, **kwargs):
        super(GIN, self).__init__(**kwargs)
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.adj = adj
        self.dropout = dropout
        self.sparse_inputs = sparse_inputs
        self.mlp = torch.nn.Linear(input_dim, output_dim)
        self.eps = zeros([1])
        self.act = act

    def forward(self, inputs):
        x = inputs
        if self.training:
            # dropout
            if self.sparse_inputs:
                x = sparse_dropout(x, self.dropout_input, self.num_features_nonzero)
            else:
                x = torch.dropout(x, self.dropout_input, True)  # dropout
        y = self.mlp((1 + self.eps) * x + torch.mm(self.adj, x))
        return self.act(y)
