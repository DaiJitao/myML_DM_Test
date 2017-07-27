# _*_ coding:utf-8 _*_

import numpy as np

class Perceptron(object):
    """
    eta:float
    n_iter:int
    w_:
    errors_:

    """
    def __index__(self, eta = 0.01, n_iter = 10):
        self.eta = eta;
        self.n_iter = n_iter;

    def fit(self, x, y):
        """
        :param x:
        :param y:
        :return:
        """
        self.w_ = np.zeros(1 + x.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0

            for xi, target in zip(x,y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0)
            self.errors_.append(errors)

    def net_input(self, x):
        """内积"""
        return np.dot(x, self.w_[1:]) + self.w_[0]

    def predict(self, x):
        """"""
        return np.where(self.net_input(x) >= 0.0, 1, -1)
