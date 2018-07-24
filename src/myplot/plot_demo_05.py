
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from common.figure_style import Figure_Style


x = np.linspace(0, 8, 100)
x = np.linspace(0, 10, 50)

def demo1(data):
    dy = 0.8
    y = np.sin(x) + dy * np.random.randn(50)

    plt.errorbar(x, y=y, yerr=dy, fmt='.k')
    plt.show()

if __name__ == "__main__":
    type__ = Figure_Style(1)
    demo1(x)
