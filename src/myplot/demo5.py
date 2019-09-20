import numpy as np
import matplotlib.pyplot as plt


def demo():
    data = np.linspace(-10, 10, 1000)
    data2 = [tanh(x) for x in data]
    data3 = [sigmoid(x) for x in data]
    plt.plot(data, data2, label="tanh")
    plt.plot(data, data3, label="sigmoid")
    plt.grid(True)
    plt.legend()
    plt.show()


def sigmoid(v):
    return 1 / (1 + np.exp(-v))


import matplotlib.pyplot as plt
from math import log
import numpy as np


# 计算二元信息熵
def entropy(props, base=2):
    sum = 0
    for prop in props:
        sum += prop * log(prop, base)
    return sum * -1


def n_entropy(props, base=2):
    sum = 0
    for prop in props:
        sum += prop * log(prop, base)
    return sum * -1


# 构造数据
x = np.arange(0.01, 1, 0.01)
props = []
for i in x:
    props.append([i, 1 - i])

y = [entropy(i) for i in props]

# plt.plot(x, y)
# plt.xlabel("p(x)")
# plt.ylabel("H(x)")
# plt.grid(True)
# plt.show()



if __name__ == "__main__":
    # x = [1, 2, 3, 4, 5]
    # y = [1, 2, 3, 4, 5]
    # plt.bar(x, y, y)
    # plt.show()
    x = [n for n in range(2, 50)]
    y = []
    for n in x:
        temp = n * [1 / n]
        s = n_entropy(temp)
        y.append(s)
    print("n元信息熵", y[18])
    print("n元", x[18])
    threds = [z / 2 for m, z in zip(x, y)]
    print("阈值", threds)
    print([(n, e, thred) for n, e, thred in zip(x, y, threds)])
    # 在我的 notebook 里，要设置下面两行才能显示中文
    plt.rcParams['font.family'] = ['sans-serif']
    # 如果是在 PyCharm 里，只要下面一行，上面的一行可以删除
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.plot(x, y, label="正常用户理论最大信息熵值", )
    plt.plot(x, threds, "--", label="水军阈值", color="red")
    plt.xlabel("n", size=22)
    plt.ylabel("H(n)", size=22)
    plt.grid(True)
    plt.xticks(x[::2], color='blue', rotation=60)
    plt.xlim(x[0], x[-1])
    # plt.title("n元信息熵")
    plt.legend()
    plt.show()
