#coding:utf-8

def fibonanci():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 7
    yield 11
    yield 18

data = fibonanci()
print(data)
print(next(data))
for i in fibonanci():
    print(i)
import sys
print(sys.maxsize)
print("===>", sys.maxsize ** 66)
data = str(sys.maxsize + 1)
# print("size ", len(data))


import abc
class AbstractDict(metaclass=abc.ABCMeta):
    def foo(self):
        return None

AbstractDict.register(dict)

print(isinstance({}, AbstractDict))