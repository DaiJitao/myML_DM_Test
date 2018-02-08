# coding:utf-8

import csv
import numpy as np
import math
import random
import sys
from sklearn.ensemble import RandomForestRegressor

def load_dataset(filename):
    file_reader = csv.reader(open(filename, 'r'))
    x, y = [], []
    for row in file_reader:
        x.append(row[2:13])
        y.append([-1])
    feature_names = np.array(x[0])
    return np.array(x[1:]).astype(np.float32), np.array(y[1:]).astype(np.float32), feature_names

fileName = r"E:\pycharm_workspace\myML_DM_Test\resource\python_ml_instances\Chapter01\bike_day.csv"
# file_reader = csv.reader(open(fileName, 'r'))
# print(file_reader)
# for row in file_reader:
#     print(row)

X, y, feature_names = load_dataset(fileName)


# 将数据分成训练集和测试集
num_training = int(.9 * len(X))
# 训练集合
X_train = X[:num_training]
y_train = y[:num_training]
# 测试集
X_test = X[num_training:]
y_test = y[num_training:]
