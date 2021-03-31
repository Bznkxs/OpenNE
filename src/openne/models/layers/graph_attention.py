from .layers import Layer
from ..inits import zeros, glorot
from ..utils import *
from ...utils import getdevice
import torch


#  a reimplementation of https://github.com/PetarV-/GAT
#  from Graph Attention Networks(https://arxiv.org/abs/1710.10903)

class GAT(Layer):
    """
    max memory usage: approx. 4n^2, where n is the number of nodes in graph
    """
    def __init__(self, input_dim, output_dim, adjmat, dropout=0., *,
                 act=torch.nn.functional.elu,
                 num_features_nonzero=0.,
                 sparse_inputs=False, bias=False,

                 dropout_coef=0.2,
                 attn_heads=3, attn_heads_reduction='average',
                 residual=True,
                 **kwargs):
        super(GAT, self).__init__(**kwargs)
        if attn_heads_reduction not in ['concat', 'average']:
            raise ValueError("attn_heads_reduction must be one of {'concat', 'average'}")
        self.attn_heads_reduction = attn_heads_reduction
        self.input_dim = input_dim
        self.output_dim = output_dim
        if attn_heads_reduction == 'concat':
            self.output_dim *= attn_heads
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
        self.threshold_val = 1e-4
        self.residual = residual

        self.weights = []
        if self.bias:
            self.biases = []
        self.attn_kernels = []
        self.residuals = []
        for head in range(self.attn_heads):
            print("attn ",head)
            # weights
            w = glorot([input_dim, output_dim])
            setattr(self, 'weights_' + str(head),  w)
            self.weights.append(w)

            # biases
            if self.bias:
                b = zeros([1, output_dim])
                setattr(self, "biases_" + str(head), b)
                self.biases.append(b)

            # attention kernels: [k_self, k_neigh]
            ak1, ak2 = zeros([output_dim, 1]), zeros([output_dim, 1])
            setattr(self, "attn_kernels_A_" + str(head), ak1)
            setattr(self, "attn_kernels_B_" + str(head), ak2)
            print("head", head)
            self.attn_kernels.append([
                ak1,ak2
            ])

            if self.residual:
                res = glorot([input_dim, output_dim])
                setattr(self, 'res_' + str(head), res)
                self.residuals.append(res)


        # self.batch_norm = torch.nn.BatchNorm1d(self.output_dim)

        if self.logging:
            self._log_vars()

    def forward(self, inputs):
        print(f"  input:{inputs.shape}, Allocated: {torch.cuda.memory_allocated()} - ")
        x = inputs  # input node features (n * input_dim)
        #print("input_device", x.device)
        if self.training:
            # dropout
            if self.sparse_inputs:
                x = sparse_dropout(x, self.dropout_input, self.num_features_nonzero)
            else:
                x = torch.dropout(x, self.dropout_input, True)  # dropout
        #print("mid", x.device)
        y_list = []
        for i in range(self.attn_heads):  # do for every independent attention kernel
            print("*", torch.cuda.memory_allocated(), '- ', end='')
            weight = self.weights[i]
            if self.bias:
                bias = self.biases[i]
            else:
                bias = 0.
            a = self.attn_kernels[i]
            print(torch.cuda.memory_allocated(), '-- ', end='')
            # feature_in = h * W, (n * output_dim)
            feat_in = torch.mm(x, weight)
            print(torch.cuda.memory_allocated(), '-+- ', end='')
            # attention coefficients
            # c(i,j) = a^T(Wh_i || Wh_j) = a_1^T Wh_i + a_2^T Wh_j
            # c = a_1^T Wh + (a_2^T Wh)^T : broadcasting, (n * n)

            f1 = torch.mm(feat_in, a[0])
            f2 = torch.mm(feat_in, a[1])
            print(torch.cuda.memory_allocated(), f"({f1.shape},{f2.shape})", '-++- ', end='')
            c = f1 + f2.T
            print(torch.cuda.memory_allocated(), '-+++- ', end='')
            c += -1e9 * (1 - self.adjmat)  # memory n^2 * 1

            # leakyReLU and softmax
            c = torch.nn.functional.softmax(torch.nn.functional.leaky_relu(c, 0.2), dim=0)  # memory n^2 * 2

            if self.training:
                # dropout
                if self.sparse_inputs:
                    c = sparse_dropout(c, self.dropout_coef, self.num_features_nonzero)
                    feat_in = sparse_dropout(feat_in, self.dropout_input, self.num_features_nonzero)
                else:
                    c = torch.dropout(c, self.dropout_coef, True)  # dropout: memory n^2 * 1
                    feat_in = torch.dropout(feat_in, self.dropout_input, True)
            #print(c.device, feat_in.device)
            feat_out = torch.mm(c, feat_in)
            if self.bias:
                feat_out += bias

            if self.residual:
                feat_out += torch.mm(x, self.residuals[i])

            feat_out = self.act(feat_out)
            y_list.append(feat_out)

        # aggregate
        if self.attn_heads_reduction == 'concat':
            y = torch.cat(y_list, dim=1)   # concatenate along dim 1 (n * (k*output_dim))
        else:
            y = torch.mean(torch.stack(y_list), dim=0)    # (n * output_dim)
        #print(y.device)
        #print("??")
        # y = self.batch_norm(y)
        print(torch.cuda.memory_allocated())
        return y

