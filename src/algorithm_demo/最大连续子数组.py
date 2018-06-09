# coding=utf-8
"""
最大连续子数组的和： 给定一个数组A[0,…,n-1]，求A的连续子数组，使得该子数组的和最大
1 暴力法 时间复杂度
2 分治法 时间复杂度
3 分析法 时间复杂度
3 动态规划算法 时间复杂度
"""

"""
暴力法:
    假设最大连续子数组的最左下标为i, 最右边下标为j, 则有
"""


def max_sub_array(array):
    n = len(array)
    max_sum = array[0]
    for i in range(n):
        for j in range(i, n):
            current = 0
            for k in range(i, j):
                current = current + array[k]
            if current > max_sum:
                max_sum = current
    return max_sum


# data = [1, -2, 3, 10, -4, 7, 2, -5]
# print("max:%d" % max_sub_array(data))

"""2 分治法

"""


def max_sub_sum():
    pass


"""
链接：https://www.nowcoder.com/questionTerminal/459bd355da1549fa8a49e350bf3df484?orderByHotValue=1&page=4&onlyReference=false

F（i）：以array[i]为末尾元素的子数组的和的最大值，子数组的元素的相对位置不变
F（i）=max（F（i-1）+array[i] ， array[i]）
res：所有子数组的和的最大值
res=max（res，F（i））

如数组 a = [6, -3, -2, 7, -15, 1, 2, 2]
初始状态：
    F（0）=6
    res=6
i=1：
    F（1）=max（F（0）-3，-3）=max（6-3，3）=3
    res=max（F（1），res）=max（3，6）=6
i=2：
    F（2）=max（F（1）-2，-2）=max（3-2，-2）=1
    res=max（F（2），res）=max（1，6）=6
i=3：
    F（3）=max（F（2）+7，7）=max（1+7，7）=8
    res=max（F（2），res）=max（8，6）=8
i=4：
    F（4）=max（F（3）-15，-15）=max（8-15，-15）=-7
    res=max（F（4），res）=max（-7，8）=8
以此类推
最终res的值为8
"""
# 第一种解法 动态规划
def find_greate_sum_subArray(a):
    n = len(a)
    res = a[0]
    _max = a[0] # 相当于F(i)
    for i in range(len(a)):
        _max = max(_max + a[i], a[i])
        res = max(_max, res)
    return res


# 第二种解法 动态规划
def max_sum_sub_array(a):
    # 初始状态
    sum = a[0]
    result = a[0]
    for i in range(1, len(a)):
        if sum > 0:
            sum += a[i]
        else:
            sum = a[i]
        if sum > result:
            result = sum
    return result


a = [6, -3, -2, 7, -15, 1, 2, 2]
print("find_greate_sum_subArray: %d" %find_greate_sum_subArray(a))
print("max_sum_sub_array: %d " %max_sum_sub_array(a))
print("max_sub_array: %d" % max_sub_array(a))


def fibo(n):
    """ 斐波那契数列 """
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
