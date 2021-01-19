import numpy as np
import pickle as pkl
import networkx as nx
import scipy.sparse as sp
from scipy.sparse.linalg.eigen.arpack import eigsh
import sys
import torch
import math
import random

def parse_index_file(filename):
    """Parse index file."""
    index = []
    for line in open(filename):
        index.append(int(line.strip()))
    return index

def scipy_coo_to_torch_sparse(scipy_sparse_coo):
    values = scipy_sparse_coo.data
    indices = np.vstack((scipy_sparse_coo.row, scipy_sparse_coo.col))
    v = torch.tensor(values, dtype=torch.float32)
    i = torch.tensor(indices, dtype=torch.long)
    return torch.sparse_coo_tensor(i, v, scipy_sparse_coo.shape)

def torch_sparse_to_scipy_coo(torch_sparse):
    a = torch_sparse.coalesce()
    (i, j), v = a.indices().numpy(), a.values().numpy()
    return sp.coo_matrix((v, (i, j)), shape=a.shape)


def preprocess_features(features, sparse=False):
    """Row-normalize feature matrix and convert to tuple representation"""
    rowsum = features.sum(1)
    r_inv = (rowsum**-1).flatten()
    r_inv[torch.isinf(r_inv)] = 0.
    r_mat_inv = torch.diag(r_inv)
    features = r_mat_inv.mm(features)
    return features.to_sparse() if sparse else features


def normalize_adj(adj):  #  safe. don't change by now
    """Symmetrically normalize adjacency matrix."""
    adj = sp.coo_matrix(adj)
    rowsum = np.array(adj.sum(1))
    d_inv_sqrt = np.power(rowsum, -0.5).flatten()
    d_inv_sqrt[np.isinf(d_inv_sqrt)] = 0.
    d_mat_inv_sqrt = sp.diags(d_inv_sqrt)
    return adj.dot(d_mat_inv_sqrt).transpose().dot(d_mat_inv_sqrt).tocoo()

def preprocess_graph(adj):
    adj = sp.coo_matrix(adj)
    adj_ = adj + sp.eye(adj.shape[0])
    rowsum = np.array(adj_.sum(1))
    degree_mat_inv_sqrt = sp.diags(np.power(rowsum, -0.5).flatten())
    adj_normalized = adj_.dot(degree_mat_inv_sqrt).transpose().dot(degree_mat_inv_sqrt).tocoo()
    # return sparse_to_tuple(adj_normalized)
    return sparse_mx_to_torch_sparse_tensor(adj_normalized)

def preprocess_adj(adj):
    """Preprocessing of adjacency matrix for simple GCN models and conversion to tuple representation."""
    adj_normalized = normalize_adj(adj + sp.eye(adj.shape[0]))
    return scipy_coo_to_torch_sparse(adj_normalized)

def sparse_mx_to_torch_sparse_tensor(sparse_mx):
    """Convert a scipy sparse matrix to a torch sparse tensor."""
    sparse_mx = sparse_mx.tocoo().astype(np.float32)
    indices = torch.from_numpy(
        np.vstack((sparse_mx.row, sparse_mx.col)).astype(np.int64))
    values = torch.from_numpy(sparse_mx.data)
    shape = torch.Size(sparse_mx.shape)
    return torch.sparse.FloatTensor(indices, values, shape)

def chebyshev_polynomials(adj, k):
    """Calculate Chebyshev polynomials up to order k. Return a list of sparse matrices (tuple representation)."""
    print("Calculating Chebyshev polynomials up to order {}...".format(k))

    adj_normalized = normalize_adj(adj)
    laplacian = sp.eye(adj.shape[0]) - adj_normalized
    largest_eigval, _ = eigsh(laplacian, 1, which='LM')
    scaled_laplacian = (
        2. / largest_eigval[0]) * laplacian - sp.eye(adj.shape[0])

    t_k = list()
    t_k.append(sp.eye(adj.shape[0]))
    t_k.append(scaled_laplacian)

    def chebyshev_recurrence(t_k_minus_one, t_k_minus_two, scaled_lap):
        s_lap = sp.csr_matrix(scaled_lap, copy=True)
        return 2 * s_lap.dot(t_k_minus_one) - t_k_minus_two

    for i in range(2, k+1):
        t_k.append(chebyshev_recurrence(t_k[-1], t_k[-2], scaled_laplacian))

    return [scipy_coo_to_torch_sparse(st.tocoo()) for st in t_k]

def sparse_dropout(x, drop_prob, noise_shape):
    """Dropout for sparse tensors."""
    random_tensor = drop_prob
    random_tensor += torch.rand(noise_shape)
    dropout_mask = torch.floor(random_tensor).type(torch.bool)
    i = x.indices()[:, dropout_mask]
    preout = torch.sparse_coo_tensor(i, values=x.values()[dropout_mask], size=x.shape, dtype=torch.float32, device=x.device)
    return preout * (1./drop_prob)

def alias_setup(probs):
    """
    Compute utility lists for non-uniform sampling from discrete distributions.
    Refer to https://hips.seas.harvard.edu/blog/2013/03/03/the-alias-method-efficient-sampling-with-many-discrete-outcomes/
    for details
    """
    K = len(probs)
    q = [0 for i in range(K)] # torch.zeros(K, dtype=torch.float32) # np.zeros(K, dtype=np.float32)
    J = [0.0 for i in range(K)] # np.zeros(K, dtype=np.int32)

    smaller = []
    larger = []
    for kk, prob in enumerate(probs):
        q[kk] = K*prob
        if q[kk] < 1.0:
            smaller.append(kk)
        else:
            larger.append(kk)

    while len(smaller) > 0 and len(larger) > 0:
        small = smaller.pop()
        large = larger.pop()

        J[small] = large
        q[large] = q[large] + q[small] - 1.0
        if q[large] < 1.0:
            smaller.append(large)
        else:
            larger.append(large)

    return J, q

# from https://github.com/Stonesjtu/Pytorch-NCE
def alias_draw(J, q, *size):
    """
    Draw sample from a non-uniform discrete distribution using alias sampling.
    """
    if len(size) == 0:
        K = len(J)
        kk = int(math.floor(random.random()*K))

        if random.random() < q[kk]:
            return kk
        else:
            return J[kk]

    q = torch.tensor(q)
    J = torch.tensor(J)
    max_value = q.size()[0]

    kk = q.new(*size).random_(0, max_value).long().view(-1)
    prob = J[kk]
    alias = q[kk]
    # b is whether a random number is greater than q
    b = torch.bernoulli(prob).long()
    oq = kk.mul(b)
    oj = alias.mul(1 - b)

    return (oq + oj).view(size)
