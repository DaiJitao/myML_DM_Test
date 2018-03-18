#coding:utf-8

import pandas as pd

s = pd.Series([12,-4,7,9], index=['a','b','c','d'])
print(s)
print(s.index)
print(s['a'])