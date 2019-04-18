import numpy as np
import pandas as pd
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,recall_score, f1_score, precision_score, confusion_matrix
from pprint import pprint
from sklearn.externals import joblib

data = pd.read_csv("./user_tb.csv", header=0)
''' 数据读取 '''
y = np.array(data['user_type'])
avg_interval_time = np.array(data.avg_interval_time)
active_days = np.array(data.active_days)
post_num = np.array(data.post_num)
similarity_degree = np.array(data.similarity_degree)
x = np.array([avg_interval_time, active_days, post_num, similarity_degree]).T
# 0.3 测试集；0.7 训练集
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, test_size=.3)
cls = svm.SVC(kernel='rbf', class_weight='balanced') # rbf核函数
cls = cls.fit(x_train, y_train)
print(cls.score(x_test, y_test)) # 准确率

y_predict = cls.predict(x_test)
print("混淆矩阵：\n", confusion_matrix(y_test, y_predict))
print('准确率：\n', accuracy_score(y_true=y_test, y_pred=y_predict))
print('recall: \n', recall_score(y_true=y_test, y_pred=y_predict))
print('f1-score: \n', f1_score(y_test, y_predict))

# 采取交叉验证
from sklearn.model_selection import StratifiedKFold, cross_val_score

cls = svm.SVC(kernel='rbf', class_weight='balanced') # bf核函数
scores = cross_val_score(cls, x_train, y_train, cv=10, scoring='accuracy') # 采取交叉验证
print("rbf准确率 ", scores.mean())
# y_predict = cls.predict(x_test)
# print("测试准确率：", accuracy_score(y_true=y_test, y_pred=y_predict))
# print("测试f1-value：", f1_score(y_true=y_test, y_pred=y_predict))
# print("测试recall:", recall_score(y_true=y_test, y_pred=y_predict))

cls = svm.LinearSVC() # 线性模型
scores = cross_val_score(cls, x_train, y_train, cv=10, scoring='accuracy') # 采取交叉验证
print("Linear准确率 ", scores.mean())
# y_predict = cls.predict(x_test)
# print("线性模型，测试准确率：", accuracy_score(y_true=y_test, y_pred=y_predict))
# print("线性模型，测试f1-value：", f1_score(y_true=y_test, y_pred=y_predict))
# print("线性模型，测试recall:", recall_score(y_true=y_test, y_pred=y_predict))