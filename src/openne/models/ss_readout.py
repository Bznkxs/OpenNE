import torch

class BaseReadOut(torch.nn.Module):
    def __init__(self, name,  **kwargs):
        super().__init__()
        self.readout = readout_dict[name](**kwargs)

    def forward(self, *args, **kwargs):
        return self.readout(*args, **kwargs)


class AvgReadOut(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        for i, j in kwargs.items():
            setattr(self, i, j)

    def forward(self, embeddings):
        return torch.mean(embeddings, 0)

class SumReadOut(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        for i, j in kwargs.items():
            setattr(self, i, j)

    def forward(self, embeddings):
        return torch.sum(embeddings, 0)

# from https://arxiv.org/pdf/1811.01287.pdf
class JKNetReadOut(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, embeddings):
        # mean || max
        return torch.cat([torch.mean(embeddings, 0), torch.max(embeddings, 0).values], dim=1)

readout_dict = {
    "mean": AvgReadOut,
    "sum": SumReadOut,
    "jk-net": JKNetReadOut
}


"""
todo:
"""

