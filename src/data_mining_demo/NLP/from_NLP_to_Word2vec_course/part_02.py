import re
import numpy as np

"""" 词权重 """

data_01 = "John likes to watch movies Mary likes too"
data_02 = "John also likes to watch football games"


def pre_process_data(data):
    temp = data.replace(".", "")
    return temp.strip()


def get_dict(data):
    """
    处理
    :param data:
    :return:
    """
    processed_data = pre_process_data(data)
    result = {}
    for i in processed_data.split(" "):
        if i in result:
            count = result.get(i)
            result.update({i: count + 1})
        else:
            result[i] = 1
    return result


def bag_of_words(*args, **kwargs):
    result = []
    _sum = ""
    for i in args:
        i = i + " "
        _sum += i
    print("_dum:", _sum)
    return get_dict(_sum)


def __log(N, n_t):
    temp = np.log(1 + N / n_t)
    return temp


def tf_idf(data, data_1, data_2):
    """

    :param data: 所计算的预料
    :param data_1: 文档1
    :param data_2: 文档2
    :return:
    """
    N = 2
    processed_data = pre_process_data(data)
    bag_dict = bag_of_words(data_1, data_2)
    result = {}
    for i in pre_process_data(data_2).split():
        if i in data_2 and i in data_1:
            n_t = 2
        else:
            n_t = 1
        result[i] = __log(N, n_t)
    return result

print("tf-idf:", tf_idf(data_01, data_02, data_01))





