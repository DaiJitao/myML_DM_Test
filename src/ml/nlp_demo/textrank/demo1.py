data = ['程序员', '英文', '程序', '开发', '维护', '专业', '人员', '程序员', '分为', '程序', '设计', '人员',
        '程序', '编码', '人员', '界限', '特别', '中国', '软件', '人员', '分为', '程序员', '高级', '程序员',
        '系统', '分析员', '项目', '经理']


def span_dict(data, span=5):
    tmp_dict, size = dict(), len(data)
    for word in set(data):
        indexs = index(data, word)
        tmp = set()
        for i in indexs:
            if i >= 0 and i < 5:
                p1 = set(data[0: i]) | set(data[i, i + 5])
            if i >= 5 and i <= size - 5:
                p1 = set(data[i - 5, i + 5])
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


from jieba.analyse import textrank

content = "4月24日下午2时30分，赶了2个小时的车程来到杭州浙江大学儿童医院的小毛，在湖州市红十字会工作人员的见证下，在重症监护室的一间办公室里签下了《中国人体器官捐献确认登记表》和手术同意书。几分钟后，" \
          "出生才6天、抢救无效离世的小毛豆接受器官捐献手术，为那些素不相识、时刻等待着生命希望的人们捐献一对眼角膜和一对肾脏。"
data = textrank(content, topK=10)
print(data)
print(len(data))
