from src.demo.Sina_Data_Collection.collection.comments_crawler import get_query
import time
import json
import logging

logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                    filename='log/new.log',
                    filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志# a是追加模式，默认如果不写的话，就是追加模式
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'  # 日志格式
                    )


# 装饰器修饰
def count_time(func):
    def inner(url, page):
        s = time.time()
        url = func(url, page)
        e = time.time()
        inv = e - s
        print("采集完毕，共耗时", inv)
        return url

    return inner


@count_time
def get_url(page, url):
    # 评论URL
    query = get_query(url)
    channel = query['channel']
    newsid = query['newsid']
    _url = 'http://comment.sina.com.cn/page/info?version=1&format=json&channel=' + channel \
           + '&newsid=' + newsid \
           + '&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=10&t_size=3&h_size=3&thread=1&uid=unlogin_user&callback=jsonp_1553578475928&_=1553578475928'
    _url = _url.replace("page=1", page)
    return _url


def deco(func):
    def _deco(a, b):
        print("before myfunc() called.")
        ret = func(a, b)
        print("  after myfunc() called. result: %s" % ret)
        return ret

    return _deco


@deco
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a + b


def reviews_parser(content, save_path, save_file_name):
    start_index = content[0:30].index('(') + 1
    str = content[start_index:-1]
    json_data = json.loads(str)  # dict
    cmntlist = json_data['result']['cmntlist']
    return cmntlist


if __name__ == '__main__':
    logging.debug("dddgggb")
    logging.info("infofo")
