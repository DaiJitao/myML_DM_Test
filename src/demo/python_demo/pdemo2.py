def doca(func):
    def wrapper():
        print(func.__name__)
        func()

    return wrapper


def fun():
    print("---1---")


@doca
def fun2():
    print("===2===")


import numpy as np
from numpy import linalg as la

df = np.mat([[1, 1], [1, 7]])
U, Sigma, Vt = la.svd(df)
print("U")
print(U)
print("Sigma")
print(Sigma)
print("Vt")
print(Vt)
a, bb = la.eig(df)
print(a)
print()
print(bb)


#
def loadExData():
    return [[0, 0, 0, 2, 2],
            [0, 0, 0, 3, 3],
            [0, 0, 0, 1, 1],
            [1, 1, 1, 0, 0],
            [2, 2, 2, 0, 0],
            [5, 0, 5, 0, 0],
            [1, 1, 1, 0, 0]]


