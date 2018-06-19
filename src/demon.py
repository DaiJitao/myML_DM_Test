# _*_ coding:utf-8 _*_

import a
import numpy as np

"""
zip():并行迭代
"""
# days = [1, 2, 3, 4, 5, 6, 7]
# fruits = ["dai", "ji", "tao", "fenbg", "shu", "ting", "dd"]
# weights_1 = np.zeros(8)
# weights_2 = [1, 1, 1, 1, 1, 1]
# print weights_1
# for i, f in zip(days, fruits):
#     print str(i) + ": " + f
#     # 明白这种写法的意义
#     weights_1[1:] += 1
#     """上式等价于下面的
#     weights_1[1] += 1
#     weights_1[2] += 1
#     weights_1[3] += 1
#     weights_1[4] += 1
#     weights_1[5] += 1
#     weights_1[6] += 1
#     """
# errors = 0
# update = 0.883


"""                    
    numpy where 的使用   
    http://www.cnblogs.com/oxxxo/p/6129294.html
    numpy.where(condition[, x, y])
    这里x,y是可选参数，condition是条件，这三个输入参数都是array_like的形式；而且三者的维度相同

    当conditon的某个位置的为true时，输出x的对应位置的元素，否则选择y对应位置的元素；

    如何只有参数condition，则函数返回为true的元素的坐标位置信息；
"""

x = np.random.randn(4, 4)
print("x:", x)

print("where(): ")
print(np.where(x > 0, 2, -2))

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
is_true = np.array([True, False, True, True, False])

print("xarr:", xarr)
print("yarr:", yarr)
print("is_true", is_true)

result = np.where(is_true, xarr, yarr)
print("result:", result)

for i in range(10):
    print("dai")

print("====================================================================")


def fib(times):
    n = 0
    a, b = 0, 1
    while n < times:
        yield b
        a, b = b, a + b
        n += 1
    return "done"


d = fib(5)
print(d)
print(next(d))
for i in d:
    print(i)

from multiprocessing import Process
import os
import time


def runproc(test):
    print(os.getpid())
    time.sleep(20)  # 单位是秒
    # print(test + " is running at id " + os.getpid())


# if __name__ == "__main__":
#     print("parent process id " + str(os.getpid()))
#     p = Process(target = runproc, args = ("daijitao",))
#     print("sub process is running, my parent_pid is " + str(os.getpid()))
#     p.start() #
#     p.join() #
#     print("end")

def create_volumes(disks):
    volumes = []
    for disk in disks:
        if "root_disk" in disk and disk["root_disk"] is True:
            continue
        else:
            print("disk：", disk)
        # volumes.append(volume)
    return volumes


if __name__ == "__main__":
    dict_1 = {}
    dict_1["name"] = "jitao"
    dict_1["age"] = 20
    dict_1["addr"] = "ctsi"
    result = None
    dict_1.update({"name": "yanzheng"})
    addr = dict_1.get("addr", None)
    # dict_1.append({"grade": "g1"})
    result = "name=" + str(dict_1["name"]) + ",age=" + str(dict_1["age"]) + ",addr=" + str(addr)
    print(result)
    disks = [
        {
		"instanceUuid": "265df3a8-af14-4251-9157-6fca1ae1029c",
         "name": "test2-i-0000004E-xvde",
         "diskuuid": "e1eb5364-98ac-4456-a601-56a9e4f49585",
         "disktype": "thick",
         "cluster_name": "autoDS1",
         "diskpath": "urn:sites:4B760883:datastores:8",
         "instanceName": "test2",
         "size": 1048576
        }]
    volumes = create_volumes(disks)
    print(True is True)
    disk = disks[0]
    print("diskpath" in disk)



