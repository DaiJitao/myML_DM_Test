#coding;utf-8

import numpy as np
import matplotlib.pyplot as plt


data = np.array([1,2,3,4]).astype(float)
print(data)
x = np.linspace(-10,10,30) #创建X轴

func = np.poly1d(data) # 多项式
func1 = func.deriv(m=1) #一介导数
func2 = func.deriv(m=2)
# print(func)
# print(func(2))
y1 = func(x)
y2 = func1(x)
y3 = func2(x)

fig = plt.figure()
ax1 = fig.add_subplot(411)
# plt.subplot(311)
ax1.plot(x, y1, 'r-')
plt.title("Polynomial")
plt.xlabel('x')
plt.ylabel('y')

ax2 = fig.add_subplot(412)
# plt.subplot(312)
ax2.plot(x, y2, 'b^')
plt.title("First Derivative")
plt.xlabel('x')
plt.ylabel('y')

# plt.subplot(313)
ax3 = fig.add_subplot(413)
ax3.plot(x, y3, 'g-')
# ax3.title("Second Derivative")
# http://blog.csdn.net/you_are_my_dream/article/details/53457960
plt.fill_between(x, y1, y2, facecolor = "yellow")
plt.xlabel('x')
plt.ylabel('y')

ax4 = fig.add_subplot(414)
y4 = np.exp(x * np.pi) + 1
ax4.plot(x, y4, 'g-')
# ax3.title("Second Derivative")
# http://blog.csdn.net/you_are_my_dream/article/details/53457960
# plt.fill_between(x, y1, y2, facecolor = "yellow")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
