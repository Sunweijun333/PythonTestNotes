import torch
import numpy as np

a = torch.randn(3,2,2)
# b = torch.unsqueeze(a,dim=1)
b = torch.unsqueeze(a, dim =0)
print(a)
print(a.shape)
print(b)
print(b.shape)