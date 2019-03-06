import scipy as scy
import numpy as np
import types
data = range(10)

c = np.random.choice(data)
print(c)


class School(object):
    def __init__(self, sub1):
        self.sub1 = sub1
        self.sub2 = 'c'

    def __getattribute__(self, item):
        if item == 'sub1':
            print('sub1: ')
        elif item == 'sub2':
            print('sub2')
        else:
            print('else attr')
            return object.__getattribute__(self, item)

    def __call__(self, *args, **kwargs):
        print('test call')

s = School('python')
s.c = 'ok'
print(s.c)

x = np.array([1, 2])
y = np.array([3, 4])
print(x.dot(y))

@classmethod
def myfun(cls):
    print('class cls')

@staticmethod
def myfun2(a, b):
    print('static method')

School.myfun = myfun
School.myfun2 = myfun2

s = School('python')
s.myfun()
s.myfun2(1, 3)

s()