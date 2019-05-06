import requests
import random
from requests.exceptions import RequestException
import time
from urllib.parse import urlsplit
import urllib.parse
from math import ceil
import multiprocessing
import threading


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

def save_data_txt(path, data):
    with open(path, 'wb') as file:
        file.write(data)

def get_query(url):
    result = urlsplit(url)
    query = dict(urllib.parse.parse_qsl(result.query))
    return query

def get_url(page):
    # 评论URL
    # title_url = 'http://comment5.news.sina.com.cn/comment/skin/default.html?channel=cj&newsid=comos-hmutuec7789553&group=0'
    title_url = 'http://comment5.news.sina.com.cn/comment/skin/default.html?channel=yl&newsid=comos-hqfskcp5146460&group=0'
    query = get_query(title_url)
    channel = query['channel']
    newsid = query['newsid']
    url = 'http://comment.sina.com.cn/page/info?version=1&format=json&channel='+ channel \
          +'&newsid='+ newsid \
          +'&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=10&t_size=3&h_size=3&thread=1&uid=unlogin_user&callback=jsonp_1553578475928&_=1553578475928'
    url = url.replace("page=1", page)
    return url

def save_data(start, end):
    name = threading.current_thread().getName()
    file = 'F:/scrapy/xinLang_zhaiTianLin/'
    # num_comnt = ceil(235604 / 10) # 共有多少页
    for i in range(start, end):
        saveData = file + "page" + str(i) + ".txt"
        page = "page=" + str(i+1)
        url = get_url(page)
        response = requests.get(url)
        data = response.text.encode('utf-8')
        save_data_txt(saveData, data)
        breakTime = random.choice([2, 1.5, 0.5, 1, 2.5, 1])
        time.sleep(breakTime)
        print("保存文件", saveData, " 线程-",name, " access url:",url)
    print("线程-", name, " 执行完毕！")

def main():
    num_comnt = ceil(235612 / 10)
    cpu_num = multiprocessing.cpu_count()
    interval = ceil(num_comnt / cpu_num)
    for i in range(cpu_num):
        start = i * interval
        end = start + interval
        s = threading.Thread(target=save_data, args=(start, end), name=str(i))
        s.start()

if __name__ == "__main__":
    main()
