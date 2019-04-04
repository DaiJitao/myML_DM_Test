from urllib.parse import urlencode
from selenium import webdriver
from pyquery import PyQuery as pq
import requests
import pickle

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Host': 'search.sohu.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive'
}


def get_index():
    '''
    访问搜搜结果,站内搜索关键字：'孟晚舟'
    :return:
    '''
    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument('--headless')
    browser = webdriver.Chrome()
    base_url = "http://search.sohu.com/?"
    query_params = {
        'keyword': '孟晚舟', 'source': 'article', 'queryType': 'edit', 'ie': 'utf8',
        'spm': 'smpc.content.search-box.1.1554095697973vlSpr2X'
    }
    index_url = base_url + urlencode(query=query_params)
    # response = requests.get(index_url, headers=headers)
    browser.get(index_url)
    html = browser.page_source
    # browser.
    browser.close()
    return html


def save_index_html(html, save_path, encoding='utf-8'):
    '''
    保存搜索结果列表html
    :param html:
    :param save_path:
    :param encoding:
    :return: None
    '''
    with open(save_path, 'w+', encoding=encoding) as file:
        file.write(html)


def load_index_html(save_path, encoding='utf-8'):
    '''
    读取搜索结果列表html
    :param save_path:
    :param encoding:
    :return:
    '''
    with open(save_path, 'r', encoding=encoding) as file:
        html = file.read()
    return html


save_path = "./all_index_187.txt"  # 存储187个新闻列表的html


# html = get_index()
#  parse_index_html(html)
# print(html)
# save_index_html(html, save_path)


def get_news_url(index_html=None):
    '''
    从搜过结果列表里面，获取新闻详情的url, 提取链接,
    :param index_html:
    :return:
    '''
    if index_html == None:
        index_html = load_index_html(save_path, encoding='utf-8')
    doc = pq(index_html, parser="html")
    content_image = doc('.ArticleFeedContainer .ArticleFeed .ImageNewsCard .ant-card-body')
    context_text = doc('.ArticleFeedContainer .ArticleFeed .TextNewsCard .ant-card-body .TextNewsCardContent')
    news_url = []
    for item in content_image.children('a').items():
        link = item.attr("href")
        news_url.append(link)
    for item_ in context_text.children('a').items():
        link = item_.attr("href")
        news_url.append(link)
    return news_url


news_url = get_news_url()

# 保存新闻列表
with open("./news_url.pkl", 'wb') as file:
    pickle.dump(news_url, file)
