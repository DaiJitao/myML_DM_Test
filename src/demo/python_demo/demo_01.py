#codnig:utf-8


import os

# file_name = os.environ.get("./test")
file_name = "./test"  # 输入文件的路径
print(file_name)
if file_name and os.path.isfile(file_name):
    exec(open(file_name).read()) # 执行文件， 该文件是python代码

import site
print("site: ", site.getsitepackages())
print(dir())

from timeit import Timer
time = Timer('t=a; a=b; b=t','a=1; b=2').timeit()
print(time)

def test(n):
    for i in range(n):
        return

class ContextManager(object):
    def __init__(self):
        self.entered = False
    def __enter__(self):
        self.entered = True
        print("self ", str(self))
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.entered = False
    def __repr__(self):
        return "test ok?"

cm = ContextManager()

with cm:
    print(cm.entered)
print(cm.entered)

class BubbleException(object):
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(" exc_type ",  exc_type)
        print("exc_val ", exc_val)
        print("exc_tb ", exc_tb)
        if exc_val:
            print("异常: ", exc_val)
        return False
print("=============================》")
# with BubbleException():
#     print(5 + 5)

with BubbleException():
    5 / 0











