import numpy as np
import pandas as pd
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,recall_score, f1_score, precision_score, confusion_matrix
from pprint import pprint
from sklearn.externals import joblib

data = pd.read_csv("./user_tb.csv", header=0)

y = np.array(data['user_type'])
avg_interval_time = np.array(data.avg_interval_time)
active_days = np.array(data.active_days)
post_num = np.array(data.post_num)
similarity_degree = np.array(data.similarity_degree)
x = np.array([avg_interval_time, active_days, post_num, similarity_degree]).T

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=.3)
cls = svm.SVC(kernel='rbf', class_weight='balanced')
cls = cls.fit(x_train, y_train)
print(cls.score(x_test, y_test))

y_predict = cls.predict(x_test)
print("混淆矩阵：\n", confusion_matrix(y_test, y_predict))
print('准确率： \n', accuracy_score(y_true=y_test, y_pred=y_predict))
print('recall: \n', recall_score(y_true=y_test, y_pred=y_predict))
print('f1-score: \n', f1_score(y_test, y_predict))

# 采取交叉验证
from sklearn.model_selection import StratifiedKFold, cross_val_score

cls = svm.SVC(kernel='rbf', class_weight='balanced')
scores = cross_val_score(cls, x_train, y_train, cv=10, scoring='accuracy') # 采取交叉验证
print("准确率 ", scores.mean())

cls = svm.LinearSVC()
scores = cross_val_score(cls, x_train, y_train, cv=10, scoring='accuracy') # 采取交叉验证
print("准确率 ", scores.mean())