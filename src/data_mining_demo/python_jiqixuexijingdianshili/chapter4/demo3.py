#coding:utf-8

"""" 客户细分"""

import csv
import numpy as np
from sklearn import cluster,covariance, manifold
from sklearn.cluster import MeanShift, estimate_bandwidth
import matplotlib.pyplot as plt

input_file = r'E:\pycharm_workspace\myML_DM_Test\resource\jiQiXueXiJingDianShiLi\Chapter04\wholesale.csv'
file_reader = csv.reader(open(input_file, 'rb'), delimiter=',')
X = []
for count, row in enumerate(file_reader):
    if not count:
        names = row[2:]
        continue
    X.append([float(x) for x in row[2:]])
# 转换为numpy数组
X = np.array(X)
print(X)



