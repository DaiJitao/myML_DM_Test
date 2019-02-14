import matplotlib.pyplot as plt
import numpy as np

data = range(1, 10, .1)
y = np.sin(data)
print(y)

plt.plot(data, y, label = "sin(x)")
plt.grid(True)
plt.show()