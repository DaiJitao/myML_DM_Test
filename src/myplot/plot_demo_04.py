
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from common.figure_style import Figure_Style
import seaborn as sns
# sns.set()
from sklearn.datasets import load_iris

x = np.linspace(0, 8, 100)
def plot_demo1():
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(x, np.sin(x),  label='sin(x)')
    plt.legend()
    plt.axis('equal')
    plt.subplot(2, 1, 2)
    plt.plot(x, np.cos(x),  label='cos(x)')
    plt.legend()
    plt.show()

def plot_demo2():
    fig, ax = plt.subplots(2)
    print(fig)
    print(type(fig))
    print(dir(fig))
    ax[0].plot(x, np.sin(x), label='sin(x)')
    ax[0].plot(x, np.cos(x), label='cos(x)');
    ax[0].legend()
    plt.show()

def plot_demo3():
    fig = plt.figure() # 创建图形
    ax = plt.axis() # 创建坐标轴
    plt.show()

def plot_demo4():
    plt.plot(x, np.sin(x))
    plt.title("哈哈")
    plt.xlabel("x")
    plt.ylabel("sin(x)")

def demo5():
    iris = load_iris()
    feature = iris.data.T

    plt.scatter()

if __name__ == "__main__":
    type__ = Figure_Style(1)
    plot_demo1()