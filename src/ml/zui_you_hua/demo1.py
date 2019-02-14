import matplotlib.pyplot as plt
import numpy as np

"""
min f(x)
"""

def line(x1, x2, k=4):
    if k <= 4:
        return 0
    else:
        p1 = np.square(x1-2)
        p2 = np.square(x2-2)
        return None


fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)
a = 4
b = 2
theta = np.arange(0, 2 * np.pi, np.pi / 100)
print(theta)
x = a*np.cos(theta)
y = b*np.sin(theta)
ax.plot(x, y)
ax.grid(True)
plt.show()
