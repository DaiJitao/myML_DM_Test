# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['lines.color'] = 'r'
mpl.rcParams['lines.linewidth'] = 2
func4 = np.poly1d(np.array([1,2,3,4]).astype(float))
func5 = np.poly1d(np.array([1,2,3,4,5]).astype(float))
func5_2 = np.poly1d(np.array([2,4,6,8,10]).astype(float))
x = np.linspace(-100,100, 60)
y = list(map(func4, x))
y5 = list(map(func5, x))
y5_2 = list(map(func5_2, x))

plt.plot( x, y5, 'b--', x, y5_2, "g--")
plt.ylabel("y")
plt.xlabel("x show")
plt.show()
