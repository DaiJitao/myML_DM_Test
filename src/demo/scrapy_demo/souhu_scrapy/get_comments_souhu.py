import pickle
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pyquery import PyQuery as pq
import time
import random

break_time = [1, 2, 3, 1.5, 2.5, 3.5, 2, 2.2, 1.8]


# commentsUrl = doc(".comment-do a").attr('href')  # 评论所在网页地址
# parNum = doc(".comment-do span").text()  # 评论的参与人数
# parNum = int(parNum)

def get_news_url(path = './news_url.pkl'): # 获取素有新闻列表的url, ./news_url.pkl
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
            comment_num = span.eq(1).text()
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
    return comments_url

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

path = "./news_url_in_commnet.pkl"
comment_url = get_news_url(path) # 获取含有评论的url
pprint(comment_url)

