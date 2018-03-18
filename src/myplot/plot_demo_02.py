#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

fig1 = plt.figure()
x = [1,2,3,4]
y = [5,4,3,2]

plt.subplot(231)
plt.plot(y)

plt.subplot(232)
plt.bar(x,y)

plt.subplot(233)
plt.barh(x,y)

y1 = [7,8,5,3]
plt.subplot(234)
plt.bar(x, y)

plt.bar(x,y1,bottom=y, color='r')
#
plt.subplot(235)
plt.boxplot(x)
#
plt.subplot(236)
plt.scatter(x,y)
plt.show()

this_x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
cos_y = np.cos(this_x)
sin_y = np.sin(this_x)

plt.plot(this_x, cos_y, 'b--', linewidth=5)
lines = plt.plot(this_x, sin_y, 'r-.')
print(lines)
print(len(lines))
for i in lines:
    print(i)
lines[0].set_linewidth(10)
plt.grid()
plt.show()