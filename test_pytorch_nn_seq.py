import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import numpy as np

# input_image = torch.rand(3,28,28)
# print("Input: ",input_image.size())
# flatten = nn.Flatten()
# flat_image = flatten(input_image)
# print("flatten output:",flat_image.size())
# layer1 = nn.Linear(in_features=28*28, out_features=20)
# hidden1 = layer1(flat_image)
# print("hidden1 output:",hidden1.size())
# print(f"Before ReLU: {hidden1}\n\n")
# hidden1 = nn.ReLU()(hidden1)
# print(f"After ReLU: {hidden1}")

# seq_modules = nn.Sequential(
#     flatten,
#     layer1,
#     nn.ReLU(),
#     nn.Linear(20, 10)
# )
# # input_image = torch.rand(3,28,28)
# logits = seq_modules(input_image)
# print("logits from seq_modules:",logits)
# print("logits shape:",logits.shape)
# softmax = nn.Softmax(dim=1)
# pred_probab = softmax(logits)
# print("softmax output",pred_probab)
# print("softmax output type",type(pred_probab))
# print("predicted output",pred_probab.argmax(1))

max_seq_len = 512
n_head = 8
test = nn.Parameter(torch.zeros(2*max_seq_len-1, n_head))
test2 = torch.nn.init.trunc_normal_(test,std=0.02)
coords_h = np.arange(max_seq_len)
coords_w = np.arange(max_seq_len-1, -1, -1)
coords = coords_h[:, None] + coords_w[None, :]
print(coords.shape)
test3 = coords.flatten()
print("test:",test.shape)
print("test2:",test2)
print("test3",test3.shape)