from .layers import Layer
from ..utils import sparse_dropout
from ..inits import zeros
import torch

# from https://github.com/fanyun-sun/InfoGraph/blob/master/unsupervised/gin.py
class GIN(Layer):
    """
    output = MLP((1+eps)input + sum(input))
    """

    def __init__(self, input_dim, output_dim, _,
                 dropout=0., *, sparse_inputs=False,
                 act=torch.relu, **kwargs):
        super(GIN, self).__init__(**kwargs)
        self.input_dim = input_dim
        self.output_dim = output_dim
        # if isinstance(adj, list):  # input support
        #     self.adj = adj[0]
        # else:
        #     self.adj = adj
        self.dropout = dropout
        self.sparse_inputs = sparse_inputs
        self.mlp = torch.nn.Linear(input_dim, output_dim)
        self.eps = zeros([1])
        self.act = act
        self.batch_norm = torch.nn.BatchNorm1d(output_dim)

    def forward(self, inputs):
        x = inputs[0]
        adj = inputs[1]
        if self.training:
            # dropout
            if self.sparse_inputs:
                x = sparse_dropout(x, self.dropout, self.num_features_nonzero)
            else:
                x = torch.dropout(x, self.dropout, True)  # dropout
        # sum pooling
        y = self.mlp((1 + self.eps) * x + torch.mm(adj, x))
        # y = self.mlp(torch.mm(adj, x))
        # y = torch.mm(adj, self.mlp(x))
        # batch norm
        y = self.act(y)
        # y = self.batch_norm(y)
        return y
