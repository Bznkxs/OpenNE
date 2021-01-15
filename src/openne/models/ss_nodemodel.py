import time
import torch
import numpy as np
import scipy.sparse as sp
import networkx as nx
from .ss_model import SSModel
from .models import ModelWithEmbeddings
from ..utils import check_existance, check_range
from .utils import scipy_coo_to_torch_sparse, preprocess_features, preprocess_graph, chebyshev_polynomials



class SS_NodeModel(ModelWithEmbeddings):

    def __init__(self, dim=128, **kwargs):
        super(SS_NodeModel, self).__init__(dim=dim, **kwargs)

    @classmethod
    def check_train_parameters(cls, **kwargs):
        check_existance(kwargs, {'dim': 128,
                                 # model
                                 'enc': 'gcn',
                                 'dec': 'inner',
                                 'sampler': 'node-rand_walk-random',
                                 'readout': 'mean',
                                 'est': 'JSD',

                                 "negative_ratio": 1,


                                 # gcn
                                 "max_degree": 0,

                                 #  randwalk
                                 'path_length': 5,
                                 'num_paths': 2,
                                 'p': 1.0,
                                 'q': 1.0,
                                 'window': 2,
                                 'workers': 8,
                                 'max_vocab_size': None,  # 1 << 32,  # 4 GB


                                 "lr": 0.01,
                                 "epochs": 200,
                                 "dropout": 0.,
                                 "hiddens": [],
                                 "weight_decay": 1e-4,
                                 "early_stopping": 50,
                                 "patience": 5,

                                 "min_delta": 0.01,
                                 "batch_size": 400000,
                                 })
        check_range(kwargs, {
            "lr": (0, np.inf),
            "epochs": (0, np.inf),
            "dropout": (0, 1),
            "weight_decay": (0, 1),
            "early_stopping": (0, np.inf),
            "max_degree": (0, np.inf)})
        return kwargs

    def build(self, graph, *, dim=128,
              enc='gcn', dec='inner', sampler='node-rand_walk-random', readout='mean', est='JSD',
              hiddens=[],
              dropout=0., weight_decay=1e-4, early_stopping=5, patience=2, min_delta=1e-5,
              batch_size=10000, negative_ratio=5, lr=0.1, epochs=200,
              **kwargs):
        self.graph = graph
        self.nb_nodes = graph.nodesize
        self.adj = self.adjmat_device(graph=graph, weighted=False, directed=True, sparse=True)
        self.learning_rate = lr
        self.epochs = epochs
        self.dropout = dropout
        self.batch_size = batch_size
        self.negative_ratio=negative_ratio
        self.weight_decay = weight_decay
        self.early_stopping = early_stopping
        self.patience = patience
        self.min_delta = min_delta
        self.enc = enc
        self.dec = dec
        self.sampler = sampler
        self.readout = readout
        self.est = est
        self.hiddens = hiddens


        if self.enc in ['gcn', ]:
            self.preprocess_data(graph)
        else:
            features = torch.from_numpy(graph.features())
            self.register_buffer("features", features)
            self.support = [self.adj]
        self.dim = dim

        input_dim = graph.features().shape[1]
        self.dimensions = [input_dim] + self.hiddens + [self.dim]
        self.dec_dims = [self.dimensions[-1] * 2, 1]
        self.model = SSModel(encoder_name=self.enc, decoder_name=self.dec, sampler_name=self.sampler,
                             readout_name=self.readout, estimator_name=self.est, enc_dims=self.dimensions,
                             graph=graph, supports=[self.adj], features=self.features,
                             batch_size=self.batch_size, negative_ratio=self.negative_ratio,
                             dropout=self.dropout, dec_dims=self.dec_dims, **kwargs)
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=self.learning_rate)
        self.cost_val = []
        self.c_up = 0

    def train_model(self, graph, **kwargs):
        output, train_loss, __ = self.evaluate()
        self.cost_val.append(train_loss)
        self.debug_info = str({"train_loss": "{:.5f}".format(train_loss)})

    def early_stopping_judge(self, graph, *, step=0, **kwargs):
        if self.patience > len(self.cost_val) - self.early_stopping:
            return False
        if self.cost_val[-1] > self.cost_val[-2]:
            self.c_up += 1
            if (self.c_up) >= self.patience:
                return True
        else:
            self.c_up = 0
        return False
        # if self.patience > len(self.cost_val) - self.early_stopping:
        #     start = self.early_stopping
        # else:
        #     start = -self.patience
        #
        # # if step>self.early_stopping:
        # #     print("costval[-1]=", self.cost_val[-1])
        # #     print(f"patience = {self.cost_val[start:-1]}")
        # #     print(f"expr = {torch.mean(torch.tensor(self.cost_val[start:-1]))} * {(1 - self.min_delta)} = {torch.mean(torch.tensor(self.cost_val[start:-1])) * (1 - self.min_delta)}")
        # return step > self.early_stopping and self.cost_val[-1] > torch.mean(
        #     torch.tensor(self.cost_val[start:-1])) * (1 - self.min_delta)

    def evaluate(self, train=True):

        t_test = time.time()
        cur_loss = 0.
        batch_num = 0.
        output = None
        for batch in self.model.sampler:
            x, pos, neg = batch
            x = x.to(self._device)
            pos = pos.to(self._device)
            neg = neg.to(self._device)
            print(x.device, pos.device, neg.device)
            self.optimizer.zero_grad()
            batch_num += 1
            loss = self.model(x, pos, neg)
            if train:
                loss.backward()
                self.optimizer.step()

            cur_loss += loss.item()

        return output, cur_loss / batch_num, (time.time() - t_test)

    def _get_embeddings(self, graph, **kwargs):
        self.embeddings = self.model.embed(torch.tensor(range(self.nb_nodes)).to(self._device)).detach()

    def preprocess_data(self, graph):
        """
            adj, features, y_train, y_val, y_test, train_mask, val_mask, test_mask
            y_train, y_val, y_test can merge to y
        """
        g = graph.G
        features = torch.from_numpy(graph.features()).type(torch.float32)
        features = preprocess_features(features, sparse=self.sparse)
        self.register_buffer("features", features)
        n = graph.nodesize
        self.build_label(graph)
        adj_label = graph.adjmat(weighted=False, directed=False, sparse=True)
        self.register_float_buffer("adj_label", adj_label + sp.eye(n).toarray())
        adj = nx.adjacency_matrix(g)  # the type of graph
        self.register_float_buffer("pos_weight", [float(n * n - adj.sum()) / adj.sum()])
        self.norm = n * n / float((n * n - adj.sum()) * 2)

        if self.max_degree == 0:
            self.support = [preprocess_graph(adj)]
        else:
            self.support = chebyshev_polynomials(adj, self.max_degree)

        self.features = self.features.to(self._device)
        self.nb_nodes = self.features.shape[0]
        self.support = [i.to(self._device) for i in self.support]
        for n, i in enumerate(self.support):
            self.register_buffer("support_{0}".format(n), i)

    def build_label(self, graph):
        g = graph.G
        look_up = graph.look_up_dict
        labels = []
        label_dict = {}
        label_id = 0
        for node in g.nodes():
            labels.append((node, g.nodes[node]['label']))
            for l in g.nodes[node]['label']:
                if l not in label_dict:
                    label_dict[l] = label_id
                    label_id += 1
        self.labels = torch.zeros((len(labels), label_id))
        self.label_dict = label_dict
        for node, l in labels:
            node_id = look_up[node]
            for ll in l:
                l_id = label_dict[ll]
                self.labels[node_id][l_id] = 1