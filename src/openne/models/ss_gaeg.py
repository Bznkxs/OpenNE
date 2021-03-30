from .utils import *
from .models import *
from .ss_modelg import SSModel
import time
import scipy.sparse as sp
import torch
import torch.cuda

import torch.nn.functional as F

class model_input:
    def __init__(self, typ, adj, start_idx, feature, repeat=False):
        """
        batch graph input
        @param typ: "graphs"/"nodes"
        @param graphs: a collection
        @param feature: collection of feat
        @param repeat: (only for typ graphs) if True, embedding of graph will be repeated (num_node) times
        """
        self.typ = typ
        self.adj = adj
        self.start_idx = start_idx
        self.feat = feature
        self.repeat = repeat


class SS_GAEg(ModelWithEmbeddings):

    def __init__(self, output_dim=32, hiddens=None, max_degree=0, **kwargs):
        if hiddens is None:
            hiddens = [32]
        super(SS_GAEg, self).__init__(output_dim=output_dim, hiddens=hiddens, max_degree=max_degree, **kwargs)

    @classmethod
    def check_train_parameters(cls, **kwargs):
        check_existance(kwargs, {'dim': 128,
                                 "learning_rate": 0.01,
                                 "epochs": 200,
                                 "dropout": 0.,
                                 "weight_decay": 1e-4,
                                 "early_stopping": 50,
                                 "patience": 3,
                                 'enc': 'gcn',
                                 'dec': 'inner',
                                 'sampler': 'dgi',
                                 'readout': 'mean',
                                 "min_delta": 0.00003,
                                 "clf_ratio": 0.5,
                                 "hiddens": [],
                                 "max_degree": 0})
        check_range(kwargs, {"learning_rate": (0, np.inf),
                             "epochs": (0, np.inf),
                             "dropout": (0, 1),
                             "weight_decay": (0, 1),
                             "early_stopping": (0, np.inf),
                             "clf_ratio": (0, 1),
                             "max_degree": (0, np.inf)})
        return kwargs

    @classmethod
    def check_graphtype(cls, graphtype, **kwargs):
        pass

    def build(self, graph, *, dim=128, hiddens=None, learning_rate=0.01, epochs=300,
              dropout=0., weight_decay=1e-4, early_stopping=100, patience=10, min_delta=3e-5,
              clf_ratio=0.5, batch_size=12800, enc='gcn', dec='inner', sampler='dgi', readout='mean', est='jsd', **kwargs):
        """
                        learning_rate: Initial learning rate
                        epochs: Number of epochs to train
                        hidden1: Number of units in hidden layer 1
                        dropout: Dropout rate (1 - keep probability)
                        weight_decay: Weight for L2 loss on embedding matrix
                        early_stopping: Tolerance for early stopping (# of epochs)
                        max_degree: Maximum Chebyshev polynomial degree
        """
        if hiddens is None:
            hiddens = []
        print("____________________build____________________")
        self.clf_ratio = clf_ratio
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.dropout = dropout
        self.batch_size = batch_size
        self.weight_decay = weight_decay
        self.early_stopping = early_stopping
        self.sparse = False
        self.enc = enc
        self.dec = dec
        self.sampler = sampler
        self.readout = readout
        self.est = est
        self.patience = patience
        self.min_delta = min_delta
        self.output_dim = dim
        self.hiddens = hiddens

        self.preprocess_data(graph)
        # Create models
        input_dim = self.features.shape[1] if not self.sparse else self.features[2][1]
        feature_shape = self.features.shape if not self.sparse else self.features[0].shape[0]

        self.dimensions = [input_dim] + self.hiddens + [self.output_dim]
        self.dec_dims = [self.dimensions[-1] * 2, 1]
        self.model = SSModel(encoder_name=self.enc, decoder_name=self.dec, sampler_name=self.sampler,
                             readout_name=self.readout, estimator_name=self.est, enc_dims=self.dimensions,
                             graphs=graph, features=self.features, batch_size=self.batch_size,
                             dropout=self.dropout, dec_dims=self.dec_dims, norm=True)
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=self.learning_rate)
        self.cost_val = []
        self.negative_ratio = 5
        self.c_up = 0
        print("----------------------built--------------------")


    def train_model(self, graph, **kwargs):
        # Train models
        output, train_loss, __ = self.evaluate()
        self.cost_val.append(train_loss)
        self.debug_info = f"train_loss: {'{:.5f}'.format(train_loss)}; Allocated: {torch.cuda.memory_allocated()}; " \
                          f"Reserved: {getattr(torch.cuda, 'memory_reserved', torch.cuda.memory_cached)()}"

    def loss(self, output, adj_label):
        cost = F.binary_cross_entropy_with_logits(output, adj_label)

        return cost

        # Define models evaluation function

    def evaluate(self, train=True):
        t_test = time.time()
        # st, ed = 0, self.batch_size
        # neg = self.gen_neg(self.x.size()[0], self.nb_nodes)
        # neg_inds = self.features[torch.tensor(neg)]
        cur_loss = 0.
        output = None
        assert self.sampler in ['dgi', 'mvgrl']

        if train:
            self.optimizer.zero_grad()
        batch_num = len(self.model.sampler)
        for bx, bpos, bneg in self.model.sampler:

            loss = self.model(bx, bpos, bneg)
            loss /= batch_num

            if train:
                loss.backward()

            cur_loss += loss.item()
            #
            # if getdevice() != torch.device('cpu'):
            #
            #     print()
        # if getdevice() != torch.device('cpu'):
        #     torch.cuda.empty_cache()
        if train:
            self.optimizer.step()

        return output, cur_loss, (time.time() - t_test)

    def early_stopping_judge(self, graph, *, step=0, **kwargs):
        if self.patience > len(self.cost_val) - self.early_stopping:
            return False
        if self.cost_val[-1] > self.cost_val[-2]:
            self.c_up += 1
            if self.c_up >= self.patience:
                return True
        else:
            self.c_up = 0
        return False

    def _get_vectors(self, graph):
        """
            Get self.vectors (which is a dict in format {node: embedding}) from self.embeddings.
            This should only be called in self.make_output().

            Rewrite when self.embeddings is not used and self.vectors is not acquired in self.train_model.
        """
        embs = self.embeddings
        if embs is None:
            return self.vectors
        self.vectors = {}
        for i, embedding in enumerate(embs):
            self.vectors[i] = embedding
        # (embs[:10])
        return self.vectors

    def _get_embeddings(self, graph, **kwargs):
        adj, start_idx = process_graphs(graph.data, getdevice())
        all_graphs = model_input('graphs', adj, start_idx, [self.features], repeat=False)
        self.embeddings = self.model.embed(all_graphs).detach()

    def preprocess_data(self, graph):
        """
            adj, features, y_train, y_val, y_test, train_mask, val_mask, test_mask
            y_train, y_val, y_test can merge to y
        """
        g = graph.G
        features = torch.from_numpy(graph.features()).type(torch.float32)
        features = preprocess_features(features, sparse=self.sparse)
        self.register_buffer("features", features)