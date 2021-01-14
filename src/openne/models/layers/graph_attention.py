from .layers import Layer
from ..inits import zeros, glorot
from ..utils import *
import torch


#  a reimplementation of https://github.com/PetarV-/GAT
#  from Graph Attention Networks(https://arxiv.org/abs/1710.10903)

class GAT(Layer):
    def __init__(self, input_dim, output_dim, adjmat, dropout=0., *,
                 act=torch.nn.functional.elu,
                 num_features_nonzero=0.,
                 sparse_inputs=False, bias=False,

                 dropout_coef=None,
                 attn_heads=1, attn_heads_reduction='average',
                 **kwargs):
        super(GAT, self).__init__(**kwargs)
        if attn_heads_reduction not in ['concat', 'average']:
            raise ValueError("attn_heads_reduction must be one of {'concat', 'average'}")
        self.attn_heads_reduction = attn_heads_reduction
        self.input_dim = input_dim
        self.output_dim = output_dim
        if isinstance(adjmat, list):  # input supports
            self.adjmat = adjmat[0]
        else:
            self.adjmat = adjmat
        self.attn_heads = int(attn_heads+0.5)
        self.dropout_input = dropout
        if dropout_coef is None:
            dropout_coef = dropout
        self.dropout_coef = dropout_coef
        self.num_features_nonzero = num_features_nonzero
        self.sparse_inputs = sparse_inputs
        self.act = act
        self.bias = bias

        self.weights = []
        if self.bias:
            self.biases = []
        self.attn_kernels = []
        print(self.attn_heads)
        for head in range(self.attn_heads):
            print("attn ",head)
            # weights
            w = glorot([input_dim, output_dim])
            setattr(self, 'weights_' + str(head),  w)
            self.weights.append(w)

            # biases
            if self.bias:
                b = zeros([output_dim, 1])
                setattr(self, "biases_" + str(head), b)
                self.biases.append(b)

            # attention kernels: [k_self, k_neigh]
            ak1, ak2 = zeros([output_dim, 1]), zeros([output_dim, 1])
            setattr(self, "attn_kernels_A_" + str(head), ak1)
            setattr(self, "attn_kernels_B_" + str(head), ak1)

            self.attn_kernels.append([
                ak1,ak2
            ])

        if self.logging:
            self._log_vars()

    def forward(self, inputs):
        x = inputs  # input node features (n * input_dim)
        if self.training:
            # dropout
            if self.sparse_inputs:
                x = sparse_dropout(x, self.dropout_input, self.num_features_nonzero)
            else:
                x = torch.dropout(x, self.dropout_input, True)  # dropout

        y_list = []
        for i in range(self.attn_heads):  # do for every independent attention kernel
            weight = self.weights[i]
            if self.bias:
                bias = self.biases[i]
            else:
                bias = 0.
            a = self.attn_kernels[i]

            # feature_in = h * W, (n * output_dim)
            feat_in = torch.mm(x, weight)

            # attention coefficients
            # c(i,j) = a^T(Wh_i || Wh_j) = a_1^T Wh_i + a_2^T Wh_j
            # c = a_1^T Wh + (a_2^T Wh)^T : broadcasting, (n * n)

            f1 = torch.mm(feat_in, a[0])
            f2 = torch.mm(feat_in, a[1])

            c = f1 + f2.T

            # leakyReLU and softmax
            c = torch.nn.functional.softmax(torch.nn.functional.leaky_relu(c, 0.2), dim=0)

            if self.training:
                # dropout
                if self.sparse_inputs:
                    c = sparse_dropout(c, self.dropout_coef, self.num_features_nonzero)
                    feat_in = sparse_dropout(feat_in, self.dropout_input, self.num_features_nonzero)
                else:
                    c = torch.dropout(c, self.dropout_coef, True)  # dropout
                    feat_in = torch.dropout(feat_in, self.dropout_input, True)

            feat_out = torch.mm(c, feat_in)
            if self.bias:
                feat_out += bias
            y_list.append(feat_out)

        # aggregate
        if self.attn_heads_reduction == 'concat':
            y = torch.cat(y_list, dim=1)  # concatenate along dim 1 (n * (k*output_dim))
        else:
            y = torch.mean(torch.stack(y_list), dim=0)   # (n * output_dim)

        return self.act(y)

