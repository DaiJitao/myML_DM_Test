import pandas as pd


def __3_user(content):
    """ 找出评论数大于三的用户 """
    result = dict()
    for key, value in content.items():
        if len(value) > 2:
            result[key] = value
    return result


def load_data(file):
    data = pd.read_csv(file, header=None)
    result = dict()
    for index, row in data.iterrows():
        id = row[0]
        comment = row[3]
        if id not in result:
            result[id] = [comment]
        elif id in result:
            result[id].append(comment)

    return __3_user(result)  # """ 找出评论数大于三的用户 """


file = r"F:\scrapy\sina_data1.0.0\zhangDanFeng\parsedData\all_data.csv"
result = load_data(file)
print(result)
