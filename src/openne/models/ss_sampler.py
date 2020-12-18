import torch
from torch.utils.data import Sampler


class BaseSampler(Sampler):
    def __init__(self, name, adj, batch_size):
        # super(BaseSampler, self).__init__()
        self.adj = adj
        self.nnodes = self.adj.size()[0]
        self.nedges = self.adj._indices().size()[1]
        self.batch_size = batch_size
        self.sampler = sampler_dict[name](adj, self.nnodes, self.nedges)

    def __iter__(self):
        batch = []
        for idx in self.sampler:
            batch.append(idx)
            if len(batch) == self.batch_size:
                yield batch
                batch = []

        if len(batch) > 0:
            yield batch

    def __len__(self):
        return (len(self.sampler) + self.batch_size - 1) // self.batch_size
torch.sparse.Tensor(1)

class TripleGenerator(Sampler):
    def __init__(self, adj, nnodes, nedges, name):
        # super().__init__()
        self.nnodes = nnodes
        self.nedges = nedges
        self.adj = adj
        self.adj_ind = self.adj._indices()
        self.anchor_name, self.pos_name, self.neg_name = name.split('-')

    def anchor(self):
        if self.pos_name == 'node':
            return self.adj_ind[0]
        # todo: deal with 'graph' condition

    def positive(self):
        if self.pos_name == 'nei':
            return self.adj_ind[1]
        # todo: deal with other conditions

    def negative(self):
        if self.neg_name == 'random':
            return torch.randint(high=self.nnodes, size=(self.nedges,)).tolist()
        # todo: deal with other conditions

    def __iter__(self):
        return iter(list(zip(self.anchor(), self.positive(), self.negative())))


class NNRSampler(TripleGenerator):
    def __init__(self, *args, **kwargs):
        super(NNRSampler, self).__init__(*args, name='node-nei-random', **kwargs)


sampler_dict = {
    "node-nei-random": NNRSampler
}

'''
TO DO:
    ● node-random walk-random nodes (DeepWalk)
    ● node-neighborhood-except neighborhood (GAE)
    ● graph-node-permuted nodes (DGI)
    ● node-random walk-except neighborhood
'''
