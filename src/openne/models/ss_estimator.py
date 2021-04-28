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
        est = self.estimator(*args, **kwargs)
        if True in torch.isnan(est):
            print("NaN in est!", flush=True)
            exit(-1)
        return est

class JSDEstimator(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.m = torch.nn.LogSigmoid()
        for i, j in kwargs.items():
            setattr(self, i, j)

    def forward(self, pos_score, neg_score, pos_mask, neg_mask):
        ep = self.m(pos_score)
        eq = self.m(-neg_score)
        if True in torch.isnan(ep):
            print("NaN in ep!", flush=True)
            exit(-1)
        if True in torch.isnan(eq):
            print("NaN in eq!", flush=True)
            exit(-1)
        if True in torch.isinf(ep):
            print("inf in ep!", flush=True)
            exit(-1)
        if True in torch.isinf(eq):
            print("inf in eq!", flush=True)
            exit(-1)
        if pos_mask is not None:
            ep = (ep * pos_mask).sum(1) / pos_mask.sum(1)
            eq = (eq * neg_mask).sum(1) / neg_mask.sum(1)
        loss = -(ep + eq).mean()
        #print(ep.shape)
        return loss



class NCEEstimator(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        for i, j in kwargs.items():
            setattr(self, i, j)

    def forward(self, pos_score, neg_score, pos_mask, neg_mask):
        mx_score = torch.max(torch.max(pos_score), torch.max(neg_score))
        ep = torch.exp(pos_score - mx_score)#.sum()
        eq = torch.exp(neg_score - mx_score)#.sum()
        epsilon = 1e-30  # avoid division by zero
        if pos_mask is not None:
            ep = (ep * pos_mask).sum(1)
            eq = (eq * neg_mask).sum(1)
        exp_loss = (ep + epsilon) / (ep + eq + epsilon)
        loss = -torch.log(exp_loss).sum()
        # print("loss=", loss)
        return loss

estimator_dict = {
    "jsd": JSDEstimator,
    "nce": NCEEstimator
}

"""
todo:
    "NCE": NCEEstimator,
"""