
def sort1(dict_):
    """
    从大到小排序
    :param dict_:
    :return:
    """
    d = dict_
    return sorted(d.items(),key = lambda x:x[1],reverse = True)

def sort2(dict_):
    """
    从小到大排序
    :param dict_:
    :return:
    """
    d = dict_
    import operator
    return sorted(d.items(), key=operator.itemgetter(1))

def sort3(dict_):
    """
    从小到大排序
    :param dict_:
    :return:
    """
    d = dict_
    f = zip(d.values(), d.keys())
    return sorted(f)

if __name__=="__main__":
    mm = {'0': 1.4863178588673052, '1': 1.4142135623730951, '2': 0.0, '3': 0.0999755859375}
    print("1---> ", sort1(mm))
    print("2---> ",sort2(mm))
    print("3---> ",sort3(mm))