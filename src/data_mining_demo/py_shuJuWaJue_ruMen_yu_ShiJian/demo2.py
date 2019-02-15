import numpy as np
import csv
from sklearn.model_selection import train_test_split

data = r'E:\pycharm_workspace\myML_DM_Test\resource\python_shuJuWaJueRuMenYuShiJian\chapter2\data\ionosphere.data'

def load_data(file, first_line_isHeader = False):
    """
    :param file:
    :param first_line_isHeader: 第一行是否为标题
    :return:
    """
    X = np.zeros(shape=(351, 34), dtype=np.float)
    Y = np.zeros(shape=(351,), dtype=np.float)
    with open(file, 'r') as input_file:
        if first_line_isHeader is False:
            reader = csv.reader(input_file)
            for i, row in enumerate(reader):
                data_row = row[:-1]
                X[i] = data_row
                Y[i] = row[-1] == 'g'
        else:
            pass
    return X, Y

X, Y = load_data(data, first_line_isHeader = False)
print(X)
print(Y)


x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=.4, random_state = 11)
from sklearn.neighbors import KNeighborsClassifier

def model_train(num_k = [5]):
    result = []
    for i in num_k:
        estimator = KNeighborsClassifier(n_neighbors=i)
        estimator.fit(x_train, y_train)
        y_predict = estimator.predict(x_test)
        accuracy = np.mean(y_predict == y_test)
        result.append(accuracy)
    return result
num_ks = range(1, 19)
result = model_train(num_ks)
for i in range(len(result)):
    print(" num_k=", num_ks[i], " accuracy=", "{:.11f}".format(result[i]))

import matplotlib.pyplot as plt

plt.plot(num_ks, result, '-.')
plt.xlabel('num_ks')
plt.ylabel("accuracy")
plt.xlim(1, 18)
plt.xticks(num_ks)
plt.yticks(result)
plt.grid(True)
plt.show()