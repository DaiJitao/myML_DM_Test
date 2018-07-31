
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from common.figure_style import Figure_Style


x = np.linspace(0, 8, 100)
x = np.linspace(0, 10, 1000)

def demo1(data):
    dy = 0.8
    y = np.sin(x) + dy * np.random.randn(50)

    plt.errorbar(x, y=y, yerr=dy, fmt='.k')
    plt.show()

def demo2():
    import pandas as pd
    file = r'E:\pycharm_workspace\myML_DM_Test\resource\python_data\births.csv'
    births = pd.read_csv(file)
    print(births)
    print(births.shape)

def demo3():
    from sklearn.datasets import load_digits
    digits = load_digits(n_class=6)
    fig, ax = plt.subplots(8, 8, figsize = (6,6))
    print(ax.flat)
    for i, axi in enumerate(ax.flat):
        print(i, axi)
        axi.imshow(digits.images[i], cmap='binary')
        axi.set(xticks=[], yticks=[])
    plt.show()

def demo4():
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), '-b', label='sine')
    ax.plot(x, np.cos(x), '--k', label='Cosine')
    ax.axis('equal')
    leg = ax.legend()
    plt.show()

def demo6():
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), '-b', label='sine')
    ax.plot(x, np.cos(x), '--k', label='Cosine')
    ax.axis('equal')
    leg = ax.legend(loc='upper left', frameon=False) # 取消外边框
    plt.show()

def demo5():
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), '-b', label='sine')
    ax.plot(x, np.cos(x), '--k', label='Cosine')
    ax.axis('equal')
    leg = ax.legend(loc='lower center', ncol=2, frameon=False) # 取消外边框
    plt.show()

if __name__ == "__main__":
    styles = [0, 1]
    type__ = Figure_Style(0)
    demo5()
    type__ = Figure_Style(1)
    demo5()

