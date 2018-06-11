#coding:utf-8

"""
    求二进制中1 的个数
"""
def count_solution(data):
    """
    时间复杂度为 O(n)
    :param data:
    :return:
    """
    count = 0
    for i in data:
        if i is "1":
            count += 1
    return count

print("solution1" ,count_solution("11101"))

def count_solution2(data):
    """

    :param data: str
    :return:
    """
    temp= int(data, 2) # 二进制转十进制
    count = 0
    # temp = int(data)
    while (temp != 0):
        if temp % 2 == 1:
            count += 1
        temp = temp // 2

    return count

print(count_solution2("111"))
