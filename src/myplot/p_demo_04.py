#coding:utf-8
import math
import numpy as np
import matplotlib.pyplot as plt

x = range(1, 1000)
def demo(x):
    t = []
    for i in x:
        data = i * math.log(i, math.e)
        t.append(data)
    return t

fig = plt.figure()
y = demo(x)
plt.plot(x, y, 'k--')
plt.show()