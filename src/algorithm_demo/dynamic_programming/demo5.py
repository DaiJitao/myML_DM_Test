# https://blog.csdn.net/rock_joker/article/details/68928150
import numpy as np

data = [[7], [3, 8], [8, 1, 0]]
d = data
def m(r):
    if r == 0:
        return d[0][0]
    else:
        return max(d[r]) + m(r-1)

# 剪绳子问题



# 走方格问题
d = np.array([[7, 1, 23,11], [28, 1, 42, 19],[43, 41, 42, 6], [3, 17, 11, 4]])
d2 = np.array([[7, 1], [28, 1]])
def _max(r, j):
    if r !=0 and j == 0:
        return sum(d[:r+1, j])
    if r == 0 and j != 0:
        return sum(d[r, :j+1])
    if r == 0 and j == 0:
        return d[0 , 0]
    else:
        return max(_max(r-1, j), _max(r, j-1)) + d[r, j]

print(_max(3, 3))



