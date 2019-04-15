import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,recall_score, f1_score, precision_score, confusion_matrix
from pprint import pprint
from sklearn.externals import joblib

iris = datasets.load_iris()
x = iris['data']
y = iris['target']
print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
print("X_train: ", x_train)
print("X_test: ", x_test)
print(len(x_test))
print(y_test)
## 线性分类器
cls = svm.LinearSVC()
cls.fit(x_train, y_train)
print('特征权重：%s。截距：%s' %(cls.coef_, cls.intercept_))
print('算法评分：', cls.score(x_test, y_test))

# 预测
y_predict = cls.predict(x_test)
# print("混淆矩阵：", confusion_matrix(y_test, y_predict))
print('准确率： ', accuracy_score(y_true=y_test, y_pred=y_predict))
# print('recall: ', recall_score(y_true=y_test, y_pred=y_predict))
# print('f1: ', f1_score(y_test, y_predict))
# 非线性分类器 kernel='rbf', class_weight='balanced'
cls = svm.LinearSVC()
cls = svm.SVC(kernel='rbf', class_weight='balanced')
cls.fit(x_train, y_train)
save_model = "./model"
joblib.dump(cls, save_model)
# 预测
cls_ = joblib.load(save_model)
y_predict = cls_.predict(x_test)
# print("混淆矩阵：", confusion_matrix(y_test, y_predict))
print('rbf准确率： ', accuracy_score(y_true=y_test, y_pred=y_predict))