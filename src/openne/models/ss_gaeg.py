from .utils import *
from .models import *
from .ss_modelg import SSModel
import time
import scipy.sparse as sp
import torch
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
                                 "batch_size": 100000,
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

    def build(self, graph, *, dim=128, hiddens=[], learning_rate=0.01, epochs=300,
              dropout=0., weight_decay=1e-4, early_stopping=100, patience=10, min_delta=3e-5,
              clf_ratio=0.5, batch_size=128, enc='gcn', dec='inner', sampler='dgi', readout='mean', est='jsd', **kwargs):
        """
                        learning_rate: Initial learning rate
                        epochs: Number of epochs to train
                        hidden1: Number of units in hidden layer 1
                        dropout: Dropout rate (1 - keep probability)
                        weight_decay: Weight for L2 loss on embedding matrix
                        early_stopping: Tolerance for early stopping (# of epochs)
                        max_degree: Maximum Chebyshev polynomial degree
        """
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
                             dropout=self.dropout, dec_dims=self.dec_dims, device=self._device)
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=self.learning_rate)
        self.cost_val = []
        self.negative_ratio = 5


    def train_model(self, graph, **kwargs):
        # Train models
        output, train_loss, __ = self.evaluate()
        self.cost_val.append(train_loss)
        self.debug_info = str({"train_loss": "{:.5f}".format(train_loss)})

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
        batch_num = 0.
        output = None
        assert self.sampler in ['dgi', 'mvgrl']
        batch_num = 1

        self.optimizer.zero_grad()

        if self.sampler == 'dgi':
            ba, bd, bf, shuf_fts = self.model.sampler.sample()
            adj, start_idx = process_graphs(ba)
            add, start_idd = process_graphs(bd)
            bx = model_input('graphs', adj, start_idx, bf)
            bpos = model_input('nodes', add, start_idd, bf)
            bneg = model_input('nodes', add, start_idd, shuf_fts)

            bx_r = model_input('graphs', add, start_idd, bf)
            bpos_r = model_input('nodes', adj, start_idx, bf)
            bneg_r = model_input('nodes', adj, start_idx, shuf_fts)

            loss = self.model(bx, bpos, bneg) + self.model(bx_r, bpos_r, bneg_r)
        else:
            ba, bdiff, bfeat, bneg, bnegdiff, bnegfeat = self.model.sampler.sample()
            adj, start_idx = process_graphs(ba)
            add, start_idd = process_graphs(bdiff)
            adn, start_idn = process_graphs(bneg)
            adnd, start_idnd = process_graphs(bnegdiff)
            bx = model_input('graphs', adj, start_idx, bfeat)
            bpos = model_input('nodes', add, start_idd, bfeat)
            bneg = model_input('nodes', adnd, start_idnd, bnegfeat)

            bx_r = model_input('graphs', add, start_idd, bfeat)
            bpos_r = model_input('nodes', adj, start_idx, bfeat)
            bneg_r = model_input('nodes', adn, start_idn, bnegfeat)

            loss = self.model(bx, bpos, bneg) + self.model(bx_r, bpos_r, bneg_r)
        if train:
            loss.backward()
            self.optimizer.step()

        cur_loss += loss.item()

        return output, cur_loss / batch_num, (time.time() - t_test)

    def early_stopping_judge(self, graph, *, step=0, **kwargs):
        if self.patience > len(self.cost_val) - self.early_stopping:
            start = self.early_stopping
        else:
            start = -self.patience
        return step > self.early_stopping and self.cost_val[-1] > torch.mean(
                    torch.tensor(self.cost_val[start:-1])) * (1 - self.min_delta)

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
        adj, start_idx = process_graphs(graph.data)
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
