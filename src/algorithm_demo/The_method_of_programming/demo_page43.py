

"""
跳台阶问题
"""

def solution(steps):
    if steps == 1 :
        return 1
    if steps == 2:
        return 2
    elif steps > 2:
        return solution(steps-1) + solution(steps-2)
    else:
        print("error")



def solution2(n):
    if n < 0:
        print("error")
    if n == 1:
        return 1
    elif n == 2:
        return 2
    a = 0
    b = 1
    result = 0
    for i in range(n):
        current = a + b
        a = b
        b = current
    return current

import time
n = 56
start1 = time.clock()
dd = solution2(n)
end1 = time.clock()
print("slution2() \n", dd, (end1-start1)* 1000000000)
start2 = time.clock()
d = solution(n)
end2 = time.clock()
print(d)


print("slution1() \n", d, (end2-start2) * 1000000000)

