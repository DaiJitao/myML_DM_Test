import matplotlib.pyplot as plt
import numpy as np

data = range(10)
data2 = range(-10)
fig = plt.figure()
print(id(fig))
ax1 = fig.add_subplot(211)
ax1.plot(data)
ax2 = fig.add_subplot(212)
ax2.plot(data2, 's-')




ax2 = fig.add_subplot(212)
ax2.plot(data)
plt.show()