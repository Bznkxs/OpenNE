import torch
import math
import numpy as np
import torch.nn.functional as F
from .utils import alias_setup, alias_draw

class BaseEstimator(torch.nn.Module):
    def __init__(self, name, **kwargs):
        super().__init__()
        self.estimator = estimator_dict[name](**kwargs)

    def forward(self, *args, **kwargs):
        return self.estimator(*args, **kwargs)

class JSDEstimator(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        for i, j in kwargs.items():
            setattr(self, i, j)

    def forward(self, positive, negative):
        m = torch.nn.LogSigmoid()
        ep = m(positive).mean()
        eq = m(-negative).mean()
        loss = -(ep + eq)
        return loss



class NCEEstimator(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        for i, j in kwargs.items():
            setattr(self, i, j)

    def forward(self, positive, negative):
        ep = torch.exp(positive)
        eq = torch.exp(negative)
        exp_loss = ep / (ep + eq)
        loss = -torch.log(exp_loss).mean()
        return loss

estimator_dict = {
    "JSD": JSDEstimator,
    "NCE": NCEEstimator
}

"""
todo:
    "NCE": NCEEstimator,
"""