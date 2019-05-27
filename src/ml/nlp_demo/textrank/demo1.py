

data = ['程序员', '英文', '程序', '开发', '维护', '专业', '人员', '程序员', '分为', '程序', '设计', '人员',
        '程序', '编码', '人员', '界限', '特别', '中国', '软件', '人员', '分为', '程序员', '高级', '程序员',
        '系统', '分析员', '项目', '经理']


def span_dict(data, span=5):
    tmp_dict, size = dict(), len(data)
    for word in set(data):
        indexs = index(data, word)
        tmp = set()
        for i in indexs:
            if i>= 0 and i < 5:
                p1 = set(data[0: i]) | set(data[i, i + 5])
            if i >= 5 and i <= size - 5:
                p1 = set(data[i-5, i+5])
            if i > size - 5:
                p1 = set(data[i - 5, i]) | set(data[i, size])
            tmp = tmp | p1
        tmp_dict[word] = tmp
    return tmp


def index(data, v):
    result = []
    count = 0
    for value in data:
        if value == v:
            result.append(count)
        count += 1
    return result


print(index(data, '程序员'))
