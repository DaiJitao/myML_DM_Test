import numpy as np
import matplotlib.pyplot as plt


def demo():
    data = np.linspace(-10, 10, 1000)
    data2 = [tanh(x) for x in data]
    data3 = [sigmoid(x) for x in data]
    plt.plot(data, data2, label = "tanh")
    plt.plot(data, data3, label = "sigmoid")
    plt.grid(True)
    plt.legend()
    plt.show()


def sigmoid(v):
    return 1 / (1 + np.exp(-v))


def tanh(v):
    a = np.exp(v)
    b = np.exp(-v)
    return (a - b) / (a + b)

if __name__ == "__main__":
    demo()