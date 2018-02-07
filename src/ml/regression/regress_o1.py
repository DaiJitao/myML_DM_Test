# coding:utf-8

import csv
import numpy as np
import sys
from sklearn.ensemble import RandomForestRegressor

def load_dataset(filename):
    file_reader = csv.reader(open(filename, 'rb'), delimiter=',')
    x, y = [], []
    for row in file_reader:
        x.append(row[2:13])
        y.append([-1])
    feature_names = np.array(x[0])
    return np.array(x[1:]).astype(np.float32), np.array(y[1:]).astype(np.float32), feature_names

X, y, feature_names = load_dataset(sys.argv[1])

# 将数据分成训练集和测试集
num_training = int(.9 * len(X))
