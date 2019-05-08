import requests
import random
from requests.exceptions import RequestException
import time
from urllib.parse import urlsplit
import urllib.parse
from math import ceil
import multiprocessing
import threading
from src.demo.Sina_Data_Collection.common.util import mkdir
import logging

logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                    filename='log/get_comments.log',
                    filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志# a是追加模式，默认如果不写的话，就是追加模式
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'  # 日志格式
                    )


# 装饰器
def count_time(func):
    def inner(url, page):
        s = time.time()
        url = func(url, page)
        e = time.time()
        inv = e - s
        print("采集完毕，共耗时", inv)
        return url

    return inner


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


def get_url(page, url):
    query = get_query(url)  # 评论URL
    channel = query['channel']
    newsid = query['newsid']
    _url = 'http://comment.sina.com.cn/page/info?version=1&format=json&channel=' + channel \
           + '&newsid=' + newsid \
           + '&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=10&t_size=3&h_size=3&thread=1&uid=unlogin_user&callback=jsonp_1553578475928&_=1553578475928'
    _url = _url.replace("page=1", page)
    return _url


def save_data(out_path, start, end, reviews_url):
    name = threading.current_thread().getName()
    for i in range(start, end):
        saveData = out_path + "page" + str(i) + ".txt"
        page = "page=" + str(i + 1)
        url = get_url(page, reviews_url)
        response = requests.get(url)
        data = response.text.encode('utf-8')
        save_data_txt(saveData, data)
        breakTime = random.choice([0.8, 1.5, 0.5, 1, 2.3, 1.8])
        time.sleep(breakTime)
        logging.info("保存文件" + saveData + " 线程-" + name + " access url:" + url)
    print("线程-", name, " 执行完毕！")
    logging.info("线程-" + name + " 执行完毕！")


def main():
    out_path = 'F:/scrapy/sina_data/zhaiTianLin/data/'
    reviews_url = 'http://comment5.news.sina.com.cn/comment/skin/default.html?channel=yl&newsid=comos-hqfskcp5146460&group=0'
    mkdir(out_path)
    save_data_txt(out_path + "url.txt", reviews_url.encode('utf-8'))
    num_comnt = ceil(236094 / 10)
    cpu_num = multiprocessing.cpu_count()  # 获取核数，一个线程对应一个核
    interval = ceil(num_comnt / cpu_num)
    start = time.time()
    threads = []
    for i in range(cpu_num):
        start = i * interval
        end = start + interval
        s = threading.Thread(target=save_data, args=(out_path, start, end, reviews_url), name=str(i))
        threads.append(s)
        s.start()

    for thread in threads:
        thread.join()

    inv = time.time() - start
    print("采集完毕，共耗时", inv)
    logging.info("采集完毕，共耗时" + str(inv))


if __name__ == "__main__":
    main()
