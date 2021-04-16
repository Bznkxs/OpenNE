import torch
import math
import numpy as np
import torch.nn.functional as F
from .utils import alias_setup, alias_draw

class BaseEstimator(torch.nn.Module):
    def __init__(self, name, **kwargs):
        super().__init__()
        self.estimator = estimator_dict[name.lower()](**kwargs)

    def forward(self, *args, **kwargs):
        return self.estimator(*args, **kwargs)

class JSDEstimator(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        for i, j in kwargs.items():
            setattr(self, i, j)

    def forward(self, hxp, hxn, pos, neg, decoder):
        m = torch.nn.LogSigmoid()
        ep = m(decoder(hxp, pos)).mean()
        eq = m(-decoder(hxn, neg)).mean()
        loss = -(ep + eq)
        return loss



class NCEEstimator(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        for i, j in kwargs.items():
            setattr(self, i, j)

    def forward(self, positive, negative):
        ep = torch.exp(positive).sum()
        eq = torch.exp(negative).sum()
        # print(ep, eq)
        exp_loss = ep / (ep + eq)
        loss = -torch.log(exp_loss).mean()
        return loss

estimator_dict = {
    "jsd": JSDEstimator,
    "nce": NCEEstimator
}

"""
todo:
    "NCE": NCEEstimator,
"""