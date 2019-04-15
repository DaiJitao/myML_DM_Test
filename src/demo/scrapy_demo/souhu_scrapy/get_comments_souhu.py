import pickle
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from math import ceil
import requests
import os
from pyquery import PyQuery as pq
import time
import random

break_time = [1, 2, 3, 1.5, 2.5, 3.5, 2, 2.2, 1.8]


# commentsUrl = doc(".comment-do a").attr('href')  # 评论所在网页地址
# parNum = doc(".comment-do span").text()  # 评论的参与人数
# parNum = int(parNum)

def get_news_url(path='./news_url.pkl'):  # 获取素有新闻列表的url, ./news_url.pkl
    with open(path, 'rb') as file:
        news_url = pickle.load(file)
    return news_url


def get_cmt_url(news_url):
    '''
    获取有评论的新闻url
    :param news_url:
    :return:
    '''
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)  # 打开浏览器
    comments_url = []
    count = 0
    for url in news_url:  # 新闻详情页地址
        count += 1
        try:
            driver.get(url=url)
            html = driver.page_source
            doc = pq(html, parser="html")
            span = doc(".c-comment-header.clear .right span")
            comment_num = span.eq(1).text()  # 評論數
            if comment_num != "":
                comment_num = int(comment_num)
            print(count, " 正在访问：", url, " num: ", comment_num)
            if comment_num > 0:
                comments_url.append((url, comment_num))
            time.sleep(random.choice(break_time))
        except Exception as e:
            print(e)
            pass
    # return list(tuple)
    return comments_url  # 含有评论的新闻url


def save_url(url):
    '''
    保存含有评论的url
    :param url:
    :return:
    '''
    print("saving...")
    with open("./news_url_in_commnet.pkl", 'wb') as file:
        pickle.dump(url, file)
    print("saved ./news_url_in_commnet.pkl")


# news_url = get_news_url()
# news_url_in_commnet = get_cmt_url(news_url)
# print(news_url_in_commnet)
# save_url(news_url_in_commnet)

def save_data_txt(path, data, mode='wb'):
    with open(path, mode) as file:
        file.write(data)


def mkdir(path):
    ''' 只创建文件夹 '''
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")
    else:
        pass

# for i in range(30):
#     html_path = "F:/data/souhu/" + str(i)
#     mkdir(html_path)

def parse_url(page):
    url = 'http://apiv2.sohu.com/api/comment/list?callback=jQuery112404831113199294317_1554789993279&page_size=10&topic_id=13491784&page_no=2&source_id=mp_290728142&_=1554789993291'
    url = url.replace('page_no=2', page)
    return url

no = 4  # no=3 4 7 9 11 13 16 19 20 21 23 25 26 29未访问 6打不开
def get_comments_from_urls(comment_url):
    global no
    save_path = "F:/data/souhu/" + str(no)
    url, num = comment_url
    cmt_page_no = ceil(num / 10)
    for i in range(cmt_page_no):
        no = str(i + 1)
        page_no = "page_no=" + no
        url = parse_url(page_no)
        print("访问url：", url)
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text.encode('utf-8')
            save_data_txt(save_path+"/data"+ no +'.txt', html)
        else:
            pprint(response.status_code)


path = "./news_url_in_commnet.pkl"
comment_url = get_news_url(path)  # 获取含有评论的url
pprint(comment_url[no])
url_value, num = comment_url[no]
save_data_txt("F:/data/souhu/" + str(no) + "/url.txt", url_value, mode='w')
#get_comments_from_urls(comment_url[no])
