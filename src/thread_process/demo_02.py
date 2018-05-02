from multiprocessing import Process
import time
import os

def fun(name, **kwargs):
    print("子进程名字" + str(name) + "num " )
    for k, v in kwargs.items():
        print(k, v)

if __name__ == "__main__":
    p1 = Process(target=fun,  args = ("djt", ), kwargs = {"name":"daijitao","age":"99"})
    p1.start()
    p1.join()
    print("end")




