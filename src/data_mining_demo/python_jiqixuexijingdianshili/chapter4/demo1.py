

import numpy as np
from sklearn.cluster import k_means
from sklearn import metrics as mt
from matplotlib import pyplot as plt
from common.utilities import  load_data

def explore_data(data_file = None):
    data_file = r'E:\pycharm_workspace\myML_DM_Test\resource\python_ml_instances\Chapter04\data_multivar.txt'
    data = load_data(data_file)
    print("======")
    print(data)
    print(type(data))
    x = data[:, 0]
    y = data[:, 1]
    xmin, xmax = np.min(x), np.max(x)
    ymin, ymax = np.min(y), np.max(y)
    fig = plt.figure()
    plt.scatter(x, y, marker='o', edgecolors='k')

    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    plt.xticks()
    plt.yticks()
    plt.grid()
    plt.show()
    return data


def K_mean(data, num_clusters = 4):
    kmeans = k_means(init='')



