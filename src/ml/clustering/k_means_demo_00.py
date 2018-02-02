# coding;utf-8

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

font = FontProperties(fname=r"c:\windows\fonts\msyh.ttc", size=10)
X0 = np.array([7, 5, 7, 3, 4, 1, 0, 2, 8, 6, 5, 3])
X1 = np.array([5, 7, 7, 3, 6, 4, 0, 2, 7, 8, 5, 7])

plt.figure()
plt.axis([-1, 9, -1, 9])
plt.grid()
plt.plot(X0, X1, 'k.')
plt.show()

print(len(X1))