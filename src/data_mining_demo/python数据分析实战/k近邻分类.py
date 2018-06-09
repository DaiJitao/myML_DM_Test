#coding;utf-8

from sklearn import datasets
import numpy as np

np.random.seed(0)

iris = datasets.load_iris()
x = iris.data
y = iris.target
i = np.random.permutation(len(x)) # 打乱数据集
x_train = x[i[:-10]]
y_train = y[i[:-10]]
x_test = x[i[-10:]]
y_test = y[i[-10:]]

from sklearn.neighbors import KNeighborsClassifier

KNN = KNeighborsClassifier()
KNN.fit(x_train, y_train)

test = KNN.predict(x_test)

print("i_test:", test)
print("y_test:", y_test)

# end page213