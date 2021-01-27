from .utils import *
from .models import *
from .ss_modelc import SSModel
import time
import scipy.sparse as sp
import torch
import torch.nn.functional as F

class model_input:

    def __init__(self, typ, ind, adj, feature):
        """
        batch graph input
        @param typ: "graphs"
        @param ind: a slice, graph indices
        @param adj: a collection, adj[ind] is the real input
        @param feature: feature matrices, feat[ind] is the real input

        @param typ: "graph"
        @param ind: None
        @param adj: graph adj
        @param feature: graph feat

        @param typ: "node"
        @param ind: None
        @param adj: graph adj
        @param feature: graph feat
        """
        self.typ = typ
        self.ind = ind
        self.adj = adj
        self.feat = feature


class SS_GAE(ModelWithEmbeddings):

    def __init__(self, output_dim=32, hiddens=None, max_degree=0, **kwargs):
        if hiddens is None:
            hiddens = [32]
        super(SS_GAE, self).__init__(output_dim=output_dim, hiddens=hiddens, max_degree=max_degree, **kwargs)

    @classmethod
    def check_train_parameters(cls, **kwargs):
        check_existance(kwargs, {'dim': 128,
                                 "learning_rate": 0.01,
                                 "epochs": 200,
                                 "dropout": 0.,
                                 "weight_decay": 1e-4,
                                 "early_stopping": 50,
                                 "patience": 100,
                                 'enc': 'gcn',
                                 'dec': 'inner',
                                 'sampler': 'dgi',
                                 'readout': 'mean',
                                 "min_delta": 0.00003,
                                 "clf_ratio": 0.5,
                                 "batch_size": 100000,
                                 "hiddens": [64],
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
        if not graphtype.attributed():
            raise TypeError("GAE only accepts attributed graphs!")

    def build(self, graph, *, dim=128, learning_rate=0.01, epochs=300,
              dropout=0., weight_decay=1e-4, early_stopping=100, patience=10, min_delta=0.00003,
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

        self.preprocess_data(graph)
        # Create models
        input_dim = self.features.shape[1] if not self.sparse else self.features[2][1]
        self.output_dim = dim
        
        self.dimensions = [input_dim] + self.hiddens + [self.output_dim]
        self.dec_dims = [self.dimensions[-1] * 2, 1]
        self.model = SSModel(encoder_name=self.enc, decoder_name=self.dec, sampler_name=self.sampler,
                             readout_name=self.readout, estimator_name=self.est, enc_dims=self.dimensions, 
                             adj=self.support[0], features=self.features,
                             batch_size=self.batch_size, dropout=self.dropout, dec_dims=self.dec_dims, device=self._device)
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=self.learning_rate)
        self.cost_val = []

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
        if self.sampler in ['dgi', 'mvgrl']:
            batch_num = 1
            ba, bd, bf, shuf_fts = self.model.sampler.sample()
            bx = model_input('graph', None, ba, bf)
            bpos = model_input('node', None, bd, bf)
            bneg = model_input('node', None, bd, shuf_fts)

            bx_r = model_input('graph', None, bd, bf)
            bpos_r = model_input('node', None, ba, bf)
            bneg_r = model_input('node', None, ba, shuf_fts)
            self.optimizer.zero_grad()
            loss = self.model(bx, bpos, bneg) + self.model(bx_r, bpos_r, bneg_r)
            if train:
                loss.backward()
                self.optimizer.step()

            cur_loss += loss.item()

        else:    
            for batch in self.model.sampler:
                x, pos, neg = zip(*batch)
                self.optimizer.zero_grad()
                bx = torch.tensor(list(x))
                bpos = torch.tensor(list(pos))
                bneg = torch.tensor(list(neg))
                bx = model_input('node', bx, self.adj[bx], self.features)
                bpos = model_input('node', bpos, self.adj[bpos], self.features)
                bneg = model_input('node', bneg, self.adj[bneg], self.features)
                '''
                lbl_1 = torch.ones(1, len(x))
                lbl = torch.cat((lbl_1, 1 - lbl_1), 1).to(self._device)
                '''
                batch_num += 1
                loss = self.model(bx, bpos, bneg)
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


    def _get_embeddings(self, graph, **kwargs):
        all_nodes = model_input('node', torch.tensor(range(self.nb_nodes)), self.support[0].to_dense(), self.features)
        self.embeddings = self.model.embed(all_nodes).detach()

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
