from torch_geometric.datasets import TUDataset
from torch_geometric.data import DataLoader
from sklearn.model_selection import KFold
from .tasks import BaseTask
from .classify import Classifier
from ..utils import *
from ..models import ModelWithEmbeddings
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV

class GraphClassification(BaseTask):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def check(self, modelclass, datasetclass):
        pass

    def train_kwargs(self) -> dict:
        return super(GraphClassification, self).train_kwargs()

    def evaluate(self, model, res, dataset):
        return self._classify(dataset, res, 0)

    def _classify(self, dataset, vectors, seed=None, simple=False):
        """
        @param dataset: dataset (TUNet)
        @param vectors: features
        @param seed: -
        @param simple: -
        @return:
        """
        self.debug("Training classifier using {:.2f}% nodes...".format(
                self.kwargs['clf_ratio']*100))
        clf = Classifier(vectors=vectors, clf=LogisticRegressionCV(cv=5, random_state=seed), simple=simple, silent=self.kwargs['silent'])
        return clf.train_and_evaluate(dataset, self.train_kwargs()['clf_ratio'], seed=seed)