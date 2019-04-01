from urllib.parse import urlencode
from selenium import webdriver
import pyquery as pq
import requests

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
    with open(save_path, 'w+', encoding=encoding) as file:
        file.write(html)

def parse_index_html(html):
    doc = pq(html)
    a = doc(".ImageNewsCardContent a")
    print(a.attr('href'))

save_path = "./index_html.txt"
html = get_index()
parse_index_html(html)
# print(html)
# save_index_html(html, save_path)



