# coding:utf-8

import numpy as np
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\msyh.ttc", size=10)
from sklearn import preprocessing

X = np.array([
[0., 0., 5., 13., 9., 1.],
[0., 0., 13., 15., 10., 15.],
[0., 3., 15., 2., 0., 11.]
])
print(preprocessing.scale(X))

import numpy as np

data = np.arange(-0.5,.5, 0.05)

def f(t):
    temp = []
    for i in t:
        temp.append(1 / (1 + np.exp(-i)))
    return np.array(temp)

y = f(data)
print(y)


import matplotlib.pyplot as plt
# plt.figure()
# plt.axis([-6, 6, 0, 1])
# plt.grid(True)
X = np.arange(-6,6,0.1)
y = 1 / (1 + np.e ** (-X))
# plt.plot(X, y, 'b-')


