import json
import src.demo.scrapy_demo.selenium_demo.save_load as saveLoad
from bs4 import BeautifulSoup

html = saveLoad.load_data("./htmlData.pkl")
print(html)

bsObj = BeautifulSoup(html, 'lxml')

print(bsObj.pre.string)
print(bsObj.pre.text)

data = bsObj.pre.text

data = json.loads(data)

print(data.keys())
print('data' in data.keys())


if  'data' in data.keys():
    print(data.get('data').get('comments'))

print(type(html))