# _*_ coding:utf-8 _*_

import numpy as np

class AdalineGD(object):
    def __init__(self, eta=0.01, n_iter=50):
        self.eta = eta;
        self.n_iter = n_iter;

    def net_input(self, X):
        return np.dot(X, self.w_) + self.w_[0]

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []

        for i in range(self.n_iter):
            """ 训练数据集 """
            output = self.net_input(X); #
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors ** 2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def activation(self, X):
        return self.net_input(X)

    def predict(self, X):
        return np.where(self.activation(X) > 0.0, 1, -1)
