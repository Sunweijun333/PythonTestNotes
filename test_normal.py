import torch
from torch.autograd import Variable
import torch.nn.functional as F
import matplotlib.pyplot as plt

n_data = torch.ones(100,2)
x0 = torch.normal(2*n_data, 1)
# b = torch.arange(0,6)
y0 = torch.zeros(100)
x1 = torch.normal(-2*n_data, 1)
y1 = torch.ones(100)
# 按行拼接
x = torch.cat((x0, x1), 0).type(torch.FloatTensor)   # FloatTensor = 32-bit floating
y = torch.cat((y0, y1), 0).type(torch.LongTensor)    # LongTensor = 64-bit integer
x, y = Variable(x), Variable(y)
# print(n_data)
# print(x0)
# print(x)
print(x.size())
print(y.size())
# print(x.data.numpy()[:,0])
# print(x1)
# print(y)
# print(b)
# plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1], c=y.data.numpy(), s=100, lw=0, cmap='RdYlGn')
plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1])
plt.savefig("E:\\Python\\picture\\scatter.png")
plt.show()