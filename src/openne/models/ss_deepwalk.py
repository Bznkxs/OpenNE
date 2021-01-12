import time
from tqdm import tqdm
import torch
import numpy as np
import scipy.sparse as sp
from .ss_model import SSModel
from .models import ModelWithEmbeddings
from ..utils import check_existance, check_range
from .utils import scipy_coo_to_torch_sparse

class SS_DeepWalk(ModelWithEmbeddings):

    def __init__(self, dim=128, **kwargs):
        super(SS_DeepWalk, self).__init__(dim=dim, **kwargs)

    @classmethod
    def check_train_parameters(cls, **kwargs):
        check_existance(kwargs, {'dim': 128,
                                 'path_length': 80,
                                 'num_paths': 10,
                                 'p': 1.0,
                                 'q': 1.0,
                                 'window': 10,
                                 'workers': 8,
                                 'max_vocab_size': None,  #1 << 32,  # 4 GB
                                 "learning_rate": 0.01,
                                 "epochs": 200,
                                 "dropout": 0.,
                                 "weight_decay": 1e-4,
                                 "early_stopping": 100,
                                 "clf_ratio": 0.5,
                                 "batch_size": 4096,
                                 })
        check_range(kwargs, {
                             "learning_rate": (0, np.inf),
                             "epochs": (0, np.inf),
                             "dropout": (0, 1),
                             "weight_decay": (0, 1),
                             "early_stopping": (0, np.inf),
                             "clf_ratio": (0, 1),
                             "max_degree": (0, np.inf)})
        return kwargs

    def build(self, graph, *, path_length=80, num_paths=10, p=1.0, q=1.0,
              enc='none', dec='inner', sampler='node-rand_walk-random', readout='mean', est='JSD',
              dropout=0., weight_decay=1e-4, early_stopping=100,
              clf_ratio=0.5, batch_size=10000, learning_rate=0.1, epochs=200,
              **kwargs):
        self.graph = graph
        self.nb_nodes = graph.nodesize
        self.adj = scipy_coo_to_torch_sparse(
            sp.coo_matrix(graph.adjmat(weighted=False, directed=True, sparse=True)))
        self.clf_ratio = clf_ratio
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.dropout = dropout
        self.batch_size = batch_size
        self.weight_decay = weight_decay
        self.early_stopping = early_stopping

        self.enc = enc
        self.dec = dec
        self.sampler = sampler
        self.readout = readout
        self.est = est

        self.model = SSModel(encoder_name=self.enc, decoder_name=self.dec, sampler_name=self.sampler,
                readout_name=self.readout, estimator_name=self.est, enc_dims=[self.dim],
                graph=self.graph, supports=[self.adj], features=torch.from_numpy(graph.features()),
                batch_size=self.batch_size, dropout=self.dropout, dec_dims=[1])
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=self.learning_rate)

    def train_model(self, graph, **kwargs):
        output, train_loss, __ = self.evaluate()
        self.debug_info = str({"train_loss": "{:.5f}".format(train_loss)})

    def evaluate(self, train=True):

        t_test = time.time()
        cur_loss = 0.
        batch_num = 0.
        output = None
        print("evaluation epoch")
        for batch in tqdm(self.model.sampler):
            x, pos, neg = batch
            self.optimizer.zero_grad()
            bx = x
            bpos = pos
            bneg = neg
            batch_num += 1
            loss = self.model(bx, bpos, bneg)
            if train:
                loss.backward()
                self.optimizer.step()

            cur_loss += loss.item()

        return output, cur_loss / batch_num, (time.time() - t_test)

    def _get_embeddings(self, graph, **kwargs):
        self.embeddings = self.model.embed(torch.tensor(range(self.nb_nodes))).detach()