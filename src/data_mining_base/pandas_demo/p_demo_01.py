#coding:utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

def demo1():
    s = pd.Series([12, -4, 7, 9], index=['a', 'b', 'c', 'd'])
    print("s\n", s)
    print(s.index)
    print("s.values: ", s.values)
    print(s['a'])
    print(s[s > 6])
    data = {'state': ['ddd', 'ddd', 'ddd', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002, 2001, 2002],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    frame = DataFrame(data)
    print("frame")
    print(frame)

def demo2():
    pass

def demo3():
    pass

def demo4():
    pass

def demo5():
    pass

if __name__ == "__main__":
    demo2()