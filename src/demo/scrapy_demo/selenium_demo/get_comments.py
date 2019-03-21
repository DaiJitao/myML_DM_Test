import requests
from requests.exceptions import RequestException
import json
import src.demo.scrapy_demo.selenium_demo.save_load as saveLoad


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


url = "https://www.toutiao.com/api/comment/list/?group_id=6650967291171176967&item_id=6650967291171176967&offset=0&count=5"
from selenium import webdriver


if __name__ == "__main__":
    # url = 'https://www.toutiao.com/a6665857373661299214/'
    url = "https://www.toutiao.com/api/comment/list/?group_id=6650967291171176967&item_id=6650967291171176967&offset=0&count=5" # 评论地址

    # print(get_page_index(url))
    browser = webdriver.Chrome()
    browser.get(url)
    html = browser.page_source
    print(html)
    import time
    time.sleep(5)
    browser.close()
    saveHtml = "./htmlData.pkl"
    saveLoad.save_data(saveHtml, html)



