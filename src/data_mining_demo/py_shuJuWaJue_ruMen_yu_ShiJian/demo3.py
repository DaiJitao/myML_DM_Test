import numpy as np

def ELU(data, lamda = 1):
    if data >= 0:
        return data
    else:
        return (np.exp(data) - 1) * lamda

x = np.linspace(-10, 2, 100)
y1 = [ELU(i) for i in x]
y2 = [ELU(i, 3) for i in x]
y3 = [ELU(i, 8) for i in x]
import matplotlib.pyplot as plt

plt.plot(x, y1, 'b--')
plt.plot(x, y2, 'r--')
plt.plot(x, y3, 'g-')
plt.grid(True)
plt.show()