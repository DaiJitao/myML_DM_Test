


"""
单变量 x0 = 1
      alfa = .2
      梯度下降算法
"""
def gradient_descent(x0, num_iterations=100, alfa=.3):
    tmp = x0
    for num in range(num_iterations):
        tmp = tmp - alfa * 2 * tmp

    return tmp

tmp = gradient_descent(1005, 25, .4)
print('%.25f' %tmp)
