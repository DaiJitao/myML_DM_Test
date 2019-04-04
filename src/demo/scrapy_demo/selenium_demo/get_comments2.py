import requests
import random
from requests.exceptions import RequestException
import time
from selenium import webdriver
from urllib.parse import urlsplit
import urllib.parse


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


def get_comments(comments_url, all_num=0, count=10):
    num = 5 # 每页的展示数量
    pages = int(all_num / num) # 一共有多少呀
    for i in range(pages):
        offset = num * i
        count = offset + num
        url_part = "&offset=" + str(offset) + "&count=" + str(count)
        print("url : ", url + url_part)



def save_data_txt(path, data):
    with open(path, 'wb') as file:
        file.write(data)

def get_query(url):
    result = urlsplit(url)
    query = dict(urllib.parse.parse_qsl(result.query))
    return query

def get_url(page):
    title_url = 'http://comment5.news.sina.com.cn/comment/skin/default.html?channel=cj&newsid=comos-hmutuec7789553&group=0'
    query = get_query(title_url)
    channel = query['channel']
    newsid = query['newsid']
    url='http://comment.sina.com.cn/page/info?version=1&format=json&channel='+channel+'&newsid='+newsid+'&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=10&t_size=3&h_size=3&thread=1&uid=unlogin_user&callback=jsonp_1553578475928&_=1553578475928'
    url = url.replace("page=1", page)
    return url

if __name__ == "__main__":
    page = 0
    file = 'F:/scrapy/xinlang/data146-------------/'
    num_comnt = ---5
    for i in range(num_comnt):
        saveData = file + "page" + str(i) + ".txt"
        print(saveData)
        page = "page=" + str(i+1)
        url = get_url(page)
        response = requests.get(url)
        print("access url：", url)
        data = response.text.encode('utf-8')
        save_data_txt(saveData, data)
        breakTime = random.choice([2, 1.5, 0.5, 1, 2.5, 1])
        time.sleep(breakTime)
    print("结束！")





