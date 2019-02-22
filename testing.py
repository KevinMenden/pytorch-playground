import torch

x = torch.empty(3, 5)
y = torch.rand(3, 5)

z = x.add_(y)