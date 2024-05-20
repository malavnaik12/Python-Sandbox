import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import numpy as np
import pandas

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

max_seq_len = 4
n_head = 1
test = nn.Parameter(torch.zeros(2*max_seq_len-1, n_head))
print("test:",test.shape)
test2 = torch.nn.init.trunc_normal_(test,std=0.02)
print("test2:",test2)
coords_h = np.arange(max_seq_len)
coords_w = np.arange(max_seq_len-1, -1, -1)
coords = coords_h[:, None] + coords_w[None, :]-(2*max_seq_len-1)
print("coords shape:",coords.shape)
print("coords:\n",coords)
test3 = coords.flatten()
print("test3",test3.shape)

file = open("./train_data/Apr23_out.txt",'r')
splitlines = file.read().split('\n')
# print(splitlines[0].split(' '))
file_pd = pandas.read_csv("./train_data/Apr23_out.txt",header=None)
print(file_pd[0][0].split(' '))
# for line in splitlines:
#     print(line)