import torch
import math
from .utils import alias_setup, alias_draw

class BaseEstimator(torch.nn.Module):
    def __init__(self, name, **kwargs):
        super().__init__()
        self.estimator = estimator_dict[name](**kwargs)

    def forward(self, *args, **kwargs):
        self.estimator(*args, **kwargs)

# from https://github.com/fanyun-sun/InfoGraph
class JSDEstimator(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        for i, j in kwargs.items():
            setattr(self, i, j)

    def forward(self, positive, negative):
        ep = math.log(2) - torch.nn.functional.softplus(-positive)

        eq = torch.nn.functional.softplus(-negative) + negative - math.log(2)
        return ep, eq



class NCEEstimator(torch.nn.Module):
    pass

estimator_dict = {
    "JSD": JSDEstimator,
    "NCE": NCEEstimator,

}

"""
todo:
    "NCE": NCEEstimator,
    "InfoNCE": I
    "NT-Xent":
"""