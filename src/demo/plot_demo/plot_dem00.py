
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,100,10000) #创建X轴

y_sin = np.sin(2 * x)

def sin_x(x):
    sum_ = 0
    for i in range(1,401):
        if i % 2 != 0:
            sum_ += 1.0/i * np.sin(i * x)
    return sum_

def cos_x(x):
    sum_ = 0
    for i in range(1,1):
        sum_ += 1.0/i * np.cos(i * x)
    return sum_

y_cos = np.cos(x)

a = 1
b = -1

y_sum =  y_sin + a * y_cos



# f = plt.ginput()
plt.plot(x, sin_x(x), label='sin')
#plt.plot(x, cos_x(x), label='cos')
# plt.plot(x, y_sum, 'r-.', label='sin(x) + cos(x)',linewidth=3)
plt.grid()
plt.legend()
plt.show()
