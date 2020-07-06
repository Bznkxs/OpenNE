import numpy as np
from .gcn.utils import *
from .gcn import models
from .gcn.layers import *
from .models import *
import time
import scipy.sparse as sp
import torch
import torch.nn as nn
import torch.nn.functional as F


class VGAE(ModelWithEmbeddings):

    def __init__(self, output_dim=16, hiddens=None, max_degree=0, **kwargs):
        if hiddens is None:
            hiddens = [32]
        super(VGAE, self).__init__(output_dim=output_dim, hiddens=hiddens, max_degree=max_degree, **kwargs)

    @classmethod
    def check_train_parameters(cls, **kwargs):
        check_existance(kwargs, {"learning_rate": 0.01,
                                 "epochs": 200,
                                 "dropout": 0.5,
                                 "weight_decay": 1e-4,
                                 "early_stopping": 100,
                                 "clf_ratio": 0.8,
                                 "hiddens": [16],
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

    def build(self, graph, *, learning_rate=0.01, epochs=200,
              dropout=0.5, weight_decay=1e-4, early_stopping=100,
              clf_ratio=0.1, **kwargs):
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
        self.weight_decay = weight_decay
        self.early_stopping = early_stopping
        self.sparse = False

        self.preprocess_data(graph)
        # Create models
        input_dim = self.features.shape[1] if not self.sparse else self.features[2][1]
        feature_shape = self.features.shape if not self.sparse else self.features[0].shape[0]

        self.mumodel = models.GCNModel(input_dim=input_dim, output_dim=self.output_dim, hidden_dims=self.hiddens,
                                supports=self.support, dropout=self.dropout, sparse_inputs=self.sparse,
                                num_features_nonzero=feature_shape, weight_decay=self.weight_decay, logging=False)
        self.varmodel = models.GCNModel(input_dim=input_dim, output_dim=self.output_dim, hidden_dims=self.hiddens,
                                supports=self.support, dropout=self.dropout, sparse_inputs=self.sparse,
                                num_features_nonzero=feature_shape, weight_decay=self.weight_decay, logging=False)
        

    def get_train(self, graph, **kwargs):
        # Train models
        output, train_loss,  __ = self.evaluate(torch.ones(graph.nodesize))
        self.debug_info = {"train_loss": "{:.5f}".format(train_loss)}
        
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
    
    def loss(self, output, adj_label, pos_weight, norm, mu, logvar, n_nodes):
        cost = 0.

        cost += norm * F.binary_cross_entropy_with_logits(torch.sigmoid(torch.mm(output, output.t())), adj_label, pos_weight=adj_label * pos_weight)
        KLD = -0.5 / n_nodes * torch.mean(torch.sum(1 + 2 * logvar - mu.pow(2) - logvar.exp().pow(2), 1))
        return cost + KLD
    
    def reparameterize(self, mu, logvar):
        if self.training:
            std = torch.exp(logvar)
            eps = torch.randn_like(std)
            return eps.mul(std).add_(mu)
        else:
            return mu

    # Define models evaluation function
    def evaluate(self, mask, train=True):
        torch.autograd.set_detect_anomaly(True)
        t_test = time.time()
        self.mumodel.zero_grad()
        self.mumodel.train(train)
        self.varmodel.zero_grad()
        self.varmodel.train(train)
        mu = self.mumodel(self.features)
        var = self.varmodel(self.features)
        output = self.reparameterize(mu, var)
        loss = self.loss(output, self.adj_label, self.pos_weight, self.norm, mu, var, self.n_nodes)
        if train:
            loss.backward()
            #print([(name, param.grad) for name,param in self.model.named_parameters()])
            self.mumodel.optimizer.step()
            self.varmodel.optimizer.step()
        return output, loss, (time.time() - t_test)



        # # Testing
        # test_res, test_cost, test_acc, test_duration = self.evaluate(self.test_mask, False)
        # print("Test set results:", "cost=", "{:.5f}".format(test_cost),
        #       "accuracy=", "{:.5f}".format(test_acc), "time=", "{:.5f}".format(test_duration))

    def make_output(self, graph, **kwargs):
        mu = self.mumodel(self.features)
        var = self.varmodel(self.features)
        self.embeddings = self.reparameterize(mu, var).detach()

    def build_train_val_test(self, graph):
        """
            build train_mask test_mask val_mask
        """
        train_precent = self.clf_ratio
        training_size = int(train_precent * graph.G.number_of_nodes())
        state = torch.random.get_rng_state()
        torch.random.manual_seed(0)
        shuffle_indices = torch.randperm(graph.G.number_of_nodes())
        torch.random.set_rng_state(state)
        g = graph.G

        def sample_mask(begin, end):
            mask = torch.zeros(g.number_of_nodes())
            for i in range(begin, end):
                mask[shuffle_indices[i]] = 1
            return mask

        self.train_mask = sample_mask(0, training_size - 100)
        self.val_mask = sample_mask(training_size - 100, training_size)
        self.test_mask = sample_mask(training_size, g.number_of_nodes())

    def preprocess_data(self, graph):
        """
            adj, features, y_train, y_val, y_test, train_mask, val_mask, test_mask
            y_train, y_val, y_test can merge to y
        """
        g = graph.G
        look_back = graph.look_back_list
        self.features = torch.from_numpy(graph.features()).type(torch.float32)
        self.features = preprocess_features(self.features, sparse=self.sparse)

        n = graph.nodesize
        self.n_nodes = n
        self.build_label(graph)
        self.build_train_val_test(graph)
        adj_label = graph.adjmat(weighted=False, directed=False, sparse=True)
        
        self.adj_label = torch.FloatTensor((adj_label + sp.eye(n).toarray()))
        adj = nx.adjacency_matrix(g)  # the type of graph
        self.pos_weight = float(n * n - adj.sum()) / adj.sum()
        self.norm = n * n / float((n * n - adj.sum()) * 2)

        if self.max_degree == 0:
            self.support = [preprocess_adj(adj)]
        else:
            self.support = chebyshev_polynomials(adj, self.max_degree)
        # print(self.support)