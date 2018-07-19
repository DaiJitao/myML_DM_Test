
def list2dict(list_):
    """

    :param list_: ['A', 'A', 'B']
    :return:
    """
    if list_ is None:
        return None
    result = {}
    if len(list_) == 0:
        print("list为空")
        return result
    for i in list_:
        if i not in result:
            result[i] = 1
        else:
            v = result[i] + 1
            result[i] = v
    return result

if __name__=="__main__":
    d = list2dict(['A', 'A', 'B'])
    print(d)
    sum_ = 0
    for v in d.values():
        sum_ += v
    print(sum_)