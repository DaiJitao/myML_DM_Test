import copy

def length(x, y):
    """ 求最长公共子序列 """
    xlen = len(x)
    ylen = len(y)
    c = [0] * xlen
    for i in range(xlen):
        c[i] = [0] * ylen
    b = copy.deepcopy(c)

    if xlen == 0 or ylen == 0:
        return 0
    for i in range(1, xlen):
        for j in range(1, ylen):
            if x[i] == y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1
            elif c[i][j - 1] >= c[i - 1][j]:
                c[i][j] = c[i][j - 1]
                b[i][j] = 2
            else:
                c[i][j] = c[i - 1][j]
                b[i][j] = 3
    return c, b


c, b = length('abocd', 'ocd')
print(c)
print("================")
print(b)
