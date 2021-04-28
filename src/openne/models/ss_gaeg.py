
from .utils import *
from .models import *
from .ss_modelg import SSModel
import time
import scipy.sparse as sp
import torch
import torch.cuda
from .ss_input import model_input
import torch.nn.functional as F
from torch.cuda.amp import autocast


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
                                 "patience": 10,
                                 'enc': 'gcn',
                                 'dec': 'inner',
                                 'sampler': 'dgi',
                                 'est': 'jsd',
                                 'readout': 'mean',
                                 "min_delta": 0.00003,
                                 "clf_ratio": 0.5,
                                 "batch_size": 4096,
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
              clf_ratio=0.5, batch_size=4096, enc='gcn', dec='inner', sampler='dgi', readout='mean', est='jsd', **kwargs):
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
        # print("____________________build____________________")
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
        if est == 'jsd':
            norm = False
        else:
            norm = True
        self.patience = patience
        self.min_delta = min_delta
        self.output_dim = dim
        self.hiddens = hiddens

        self.preprocess_data(graph)
        # Create models
        input_dim = self.features.shape[1] if not self.sparse else self.features[2][1]
        self.dimensions = [input_dim] + self.hiddens + [self.output_dim]
        self.dec_dims = [self.dimensions[-1] * 2, 1]
        self.model = SSModel(encoder_name=self.enc, decoder_name=self.dec, sampler_name=self.sampler,
                             readout_name=self.readout, estimator_name=self.est, enc_dims=self.dimensions,
                             graphs=graph, features=self.features, batch_size=self.batch_size,
                             dropout=self.dropout, dec_dims=self.dec_dims, norm=norm)
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=self.learning_rate)
        self.cost_val = []
        self.negative_ratio = 5
        self.c_up = 0
        self.emergency_stop = False
        # print("----------------------built--------------------")


    def train_model(self, graph, **kwargs):
        # Train models
        output, train_loss, __ = self.evaluate()
        self.cost_val.append(train_loss)
        if getdevice() != torch.device('cpu'):
            self.debug_info = f"train_loss: {'{:.5f}'.format(train_loss)}; Allocated: {torch.cuda.memory_allocated()}; " \
                              f"Reserved: {getattr(torch.cuda, 'memory_reserved', torch.cuda.memory_cached)()}"
        else:
            self.debug_info = f"train_loss: {'{:.5f}'.format(train_loss)}"
        if np.isnan(train_loss):
            self.emergency_stop = True

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

        if train:
            self.optimizer.zero_grad()
        batch_num = len(self.model.sampler)
        print("epoch start", flush=True)
        for batch in self.model.sampler:
            loss = 0.
            print("batch start", flush=True)
            for bx, bpos, bneg in batch:
            #    print("  sample in batch", flush=True)
                # md_start = time.time()

                loss += self.model(bx, bpos, bneg)
                # process = psutil.Process(os.getpid())
                # print(process.memory_info().rss)
                # print("forward: ", time.time() - md_start)

            loss /= batch_num
            if True in torch.isnan(loss):
                print("gaeg: NaN in forward propagation!")
                exit(-1)
            if train:
                # bp_start = time.time()
                loss.backward()
                for k in self.parameters():
                    if True in torch.isnan(k):
                        print("NaN in backward prop!")
                        exit(-1)
                # print("bp: ", time.time() - bp_start)

            cur_loss += loss.item()
            #
            # if getdevice() != torch.device('cpu'):
            #
            #     print()
            if getdevice() != torch.device('cpu'):
                torch.cuda.empty_cache()
        if train:
            self.optimizer.step()

        return output, cur_loss, (time.time() - t_test)

    def early_stopping_judge(self, graph, *, step=0, **kwargs):
        if self.emergency_stop:
            return True
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

    def _ss_get_embeddings(self, graph, input_flag):
        # print("get embeddings", flush=True)
        # self.to('cpu')
        self.requires_grad_(False)
        graphs_data = self.model.graphs_data  # List[graphinput]
        slices = self.model.sampler.sampler.sample_slicer([g.x for g in graphs_data])
        embeddings = []
        processed_nodes = 0
        # print("ready get embeddings")
        for i in slices:
            # print("slice", i)

            adj, start_idx = process_graphs(graphs_data[i], getdevice())
            feature_slice = slice(processed_nodes, processed_nodes+start_idx[-1])
            all_graphs = model_input(input_flag, adj, start_idx, [self.features[feature_slice]], repeat=False)
            processed_nodes += start_idx[-1]
            if self.enc == 'gat' and adj.shape[0] > 10000:  # save space
                with autocast():
                    sub_embeddings = self.model.embed(all_graphs).detach()
            else:
                sub_embeddings = self.model.embed(all_graphs).detach()
            embeddings.append(sub_embeddings)
        self.embeddings = torch.cat(embeddings)
        #self.embeddings = self.features

    def _get_embeddings(self, graph, **kwargs):
        self._ss_get_embeddings(graph, model_input.GRAPHS)

    def preprocess_data(self, graph):
        """
            adj, features, y_train, y_val, y_test, train_mask, val_mask, test_mask
            y_train, y_val, y_test can merge to y
        """
        g = graph.G
        features = torch.from_numpy(graph.features()).type(torch.float32)
        
        features = preprocess_features(features, sparse=self.sparse)
        #print(features.sum(1))
        graph.setfeatures(features)
        self.register_buffer("features", features)