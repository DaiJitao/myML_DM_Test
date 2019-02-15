'''
    爬取《python数据挖掘入门与实践》提到的nba赛况
    https://www.basketball-reference.com/leagues/NBA_2014_games-october.html
    操作：编译.py后，使用save()方法即可
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import pickle

year = "2014"

BASE_URL = 'https://www.basketball-reference.com/leagues/NBA_' + year + '_games-{month}.html'
all_month = np.array(['october', 'november', 'december', 'january', 'february', 'march', 'april', 'may', 'june'])


def get_content():
    list = []
    for i in range(len(all_month)):
        url = BASE_URL.format(month=all_month[i])
        print(url)
        html = urlopen(url).read()
        bsObj = BeautifulSoup(html, 'lxml')
        rows = [dd for dd in bsObj.select('tbody tr')]  # selectk()可以多重刷选
        for row in rows:
            cell = [i.text for i in row.find_all('td')]  # 对于每一个tr标签内也可以进行td标签筛选
            list.append(cell)
    return list  # 返回二维列表


# 存储为scv格式
def save():
    file = open('./matches' + year + '.csv', 'w')  # 地址要自己改
    list = get_content()
    df_data = pd.DataFrame(columns=[1, 2, 3, 4, 5, 6, 7, 8, 9], data=list)
    df_data.to_csv(file)
    print('done')


datafile = './match_data_2014.csv'
dataSet = pd.read_csv(datafile)
print(dataSet.head(6).shape)
print(dataSet.ix[:5])

data = dataSet
dataset2 = data.iloc[:, [0, 6, 2, 3, 4, 5, 7, 9]]
dataset2.columns = ["Date", "Score Type", "Visitor Team", "VisitorPts", "Home Team", "HomePts", "OT?", "Notes"] #重命名
print(dataset2.ix[:5])

datafile = "./cleanedData.dai"

with open(datafile, 'wb') as file:
    pickle.dump(dataset2, file, 2)


