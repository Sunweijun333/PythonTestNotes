import torch
import numpy as np
from torch.autograd import Variable
import torch.nn.functional as F
import matplotlib.pyplot as plt

a = torch.randn(3,3)
b = torch.max(a,1)
c = torch.randn(1)

print(c.data.numpy().shape)

# print(b.data.numpy())
print(a)
print(b)
print(b[1])
print(c)