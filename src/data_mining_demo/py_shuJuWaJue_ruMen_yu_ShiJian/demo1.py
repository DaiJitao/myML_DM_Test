
import numpy as np

file = r'G:\category_prediction_data_a\valid_a.txt'

def load_data(file):
    result = []
    with open(file) as content:
        lines = content.readlines()
        for line in lines:
            result.append(line.split())
    titles = result[0]
    desc = ['商品id', '商品标题的字符序列', '商品标题的分词序列', '商品描述的字符', '商品描述的分词', '商品1级类目id', '商品2级类目id', '商品3级类目id']
    titles_desc = zip(titles, desc)
    title_data  = {'title': titles_desc, 'data': result[1:]}
    return title_data

data = load_data(file)
print(data['title'])
for i in data['title']:
    print(i)

print()