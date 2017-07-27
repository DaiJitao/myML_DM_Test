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


x = np.random.randn(4,4)
print "x:"
print x

print "where(): "
print np.where(x > 0, 2, -2)

xarr = np.array([1.1,1.2,1.3,1.4,1.5])
yarr = np.array([2.1,2.2,2.3,2.4,2.5])
is_true = np.array([True,False,True,True,False])

print "xarr:",xarr
print "yarr:",yarr
print "is_true",is_true

result = np.where(is_true, xarr, yarr)
print "result:",result

for i in range(10):
    print "dai"

