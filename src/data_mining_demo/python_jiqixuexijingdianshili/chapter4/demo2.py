import numpy as np

def demo():
    '''
    numpy函数np.c_和np.r_学习使用
    '''
    data_list1 = [4, 6, 12, 6, 0, 3, 7]
    data_list2 = [1, 5, 2, 65, 6, 7, 3]
    print('np.r_')
    print(np.r_[data_list1, data_list2])
    print('np.c_')
    print(np.c_[data_list1, data_list2])
demo()