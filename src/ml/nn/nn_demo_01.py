#coding:utf-8
import numpy as np
from matplotlib import pyplot

class Network(object):
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biaes = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x,y in zip(sizes[:1], sizes[1:])]


    def sigmoid(self, z):
        return 1.0 / (1. + np.exp(-z))
