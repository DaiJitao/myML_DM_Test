import requests
import random
from requests.exceptions import RequestException
import json
import time
import src.demo.scrapy_demo.selenium_demo.save_load as saveLoad
from selenium import webdriver


def get_page_index(url):

    print("access url: ", url)
    headers = {'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'  # 解决中文乱码
            return response.text
        else:
            return None
    except RequestException as e:
        print(e)
        return None


url = "https://www.toutiao.com/api/comment/list/?group_id=6650967291171176967&item_id=6650967291171176967&offset=0&count=5" # 评论地址

def get_comments(comments_url, all_num=0, count=10):
    num = 5 # 每页的展示数量
    pages = int(all_num / num) # 一共有多少呀
    for i in range(pages):
        offset = num * i
        count = offset + num

        url_part = "&offset=" + str(offset) + "&count=" + str(count)
        print("url : ", url + url_part)


    # # url = 'https://www.toutiao.com/a6665857373661299214/'
    # url = "https://www.toutiao.com/api/comment/list/?group_id=6650967291171176967&item_id=6650967291171176967&offset=0&count=5" # 评论地址
    #
    # # print(get_page_index(url))
    # browser = webdriver.Chrome()
    # browser.get(url)
    # html = browser.page_source
    # print(html)
    #
    # time.sleep(5)
    # browser.close()
    # saveHtml = "./htmlData.pkl"
    # saveLoad.save_data(saveHtml, html)

def get_url(page):
    url = 'http://comment.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-hrfqzka0522165&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=10&t_size=3&h_size=3&thread=1&uid=unlogin_user&callback=jsonp_1553253040954&_=1553253040954'
    url = url.replace("page=1", page)
    return url


def save_data_txt(path, data):
    with open(path, 'wb') as file:
        file.write(data)

if __name__ == "__main__":

    """
    url = 'http://comment5.news.sina.com.cn/comment/skin/default.html?channel=gn&newsid=comos-hrfqzkc3291821&group=0'
    browser = webdriver.Chrome()
    browser.get(url)
    html = browser.page_source
    savePath = 'F:/test.html'
    with open(savePath, 'wb') as file:
        file.write(html.encode("utf-8"))
    time.sleep(3)
    browser.close()
    """
    page = 0
    file = 'F:/scrapy/xinlang/data39/'
    print(url)
    r = requests.get(url)
    for i in range(10):
        saveData = file + "page" + str(i) + ".txt"
        print(saveData)

        page = "page=" + str(i+1)
        url = get_url(page)
        response = requests.get(url)
        print("access url ", url)
        data = response.text.encode('utf-8')
        save_data_txt(saveData, data)
        breakTime = random.choice([2, 1.5, 2.5, 1, 3.5, 1])
        time.sleep(breakTime)
    print("结束")





