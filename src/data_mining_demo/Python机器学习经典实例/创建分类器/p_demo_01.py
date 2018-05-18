#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

X = np.array([[3,1], [2,5], [1,8], [6,4], [5,2], [3,5], [4,7], [4,-1]])
y = [0, 1, 1, 0, 0, 1, 1, 0]

class_0 = np.array(X[i] for i in range(len(X)) if y[i] == 0)
class_1 = np.array(X[i] for i in range(len(X)) if y[i] == 1)

print(class_0.shape)

# plt.figure()
# plt.scatter(class_0[:,0], class_0[:,1])
# plt.scatter(class_1[:,0], class_1[:,1])
# plt.show()