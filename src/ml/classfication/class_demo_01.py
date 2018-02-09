# coding:utf-8
import numpy as np
from sklearn import datasets
from sklearn.cross_validation import train_test_split

iris = datasets.load_iris()
X = iris.data[:, [2,3]]
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
print(len(X_train))

# 数据的标准化
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# 三分类感知机模型
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
ppn = Perceptron(n_iter=40, eta0=.1, random_state=0)
ppn.fit(X_train_std, y_train)

y_predic = ppn.predict(X_test_std)
print("result ", (y_test != y_predic).sum() )
print("result ", accuracy_score(y_test, y_predic))