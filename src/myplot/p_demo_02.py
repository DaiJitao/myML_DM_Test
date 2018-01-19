import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)


x = np.arange(-5,5,0.001)
y = np.log(1 + np.exp(x))
plt.plot(x, y, 'k--')


ax2 = fig.add_subplot(2,2,2)

def relu(x):
    if x <= 0:
        return 0
    else:
        return x
y2 = map(relu, x)
plt.plot(x, y, )

plt.show()