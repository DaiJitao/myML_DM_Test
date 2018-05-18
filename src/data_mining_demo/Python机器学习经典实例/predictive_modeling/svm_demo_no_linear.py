#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import python_utilities as utilities


input_file = "E:/pycharm_workspace/myML_DM_Test/resource/python_ml_instances/Chapter03/data_multivar.txt"
def load_data(input_file):
    """
    数据读取： 加载数据
    :param input_file:
    :return: np.array()
    """
    X = []; y = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            data = [float(x) for x in line.split(',')]
            X.append(data[:-1])
            # print("X : ", X)
            y.append(data[-1])
            # print("y: " , y)
        X = np.array(X); y = np.array(y)
        return X, y

X, y = load_data(input_file)
# 将数据分类
class_0 = np.array([ X[i] for i in range(len(X)) if y[i] == 0])
class_1 = np.array([ X[i] for i in range(len(X)) if y[i] == 1])
# 将数据可视化
plt.figure()
plt.scatter(class_0[:,0], class_0[:,1], facecolors='red', edgecolors='red', marker='s') # facecolors 填充色； 边框色：edgexolors
plt.scatter(class_1[:,0], class_1[:,1], facecolors='None', edgecolors='black', marker='s')
plt.title('data')
# plt.show()
# 数据集的划分：训练集和验证集
from sklearn import cross_validation
from sklearn.svm import SVC
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=.25, random_state=5)

# 开始训练
# params = {"kernel": 'linear'}
params = {'kernel': 'poly', 'degree': 3} # 多项式核函数
params2 = {'kernel': 'rbf'} # 用径向基函数建立非线性分类器

classifier = SVC(**params2) # 加入线性核函数, 指明该参数params 为字典，等同于kernet='linear'
classifier.fit(X_train, y_train)
classifier.predict(X_test)
# 模型效果的指标评价
from sklearn.metrics import classification_report

target_names = ['Class-' + str(int(i)) for i in set(y)]
print("\n" + "#" * 60)
print("\nClassifier performance on training dataset\n")
print(classification_report(y_train, classifier.predict(X_train), target_names=target_names))
print("#" * 60 + "\n")

y_test_pred = classifier.predict(X_test)
print("#"*60)
print ("\nClassification report on test dataset\n")
print (classification_report(y_test, y_test_pred, target_names=target_names))
print ("#"*60 + "\n")

# if __name__ == "__main__":
#     x_test = classifier.predict(X_test)
#     print("x_test: ", x_test)
#     print("y_test: ", y_test)