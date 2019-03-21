import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode
import json


def get_page_index(offset):
    data = {
        'aid' : 24, # 协助count
        'app_name': 'web_search', 'count': 20,
        'offset': offset,
        'autoload': 'true',
        'keyword': '街拍',
        'cur_tab': 1, 'en_qc': 1,
        'format': 'json'}
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(data)
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


def save_html():
    file = "F:/data.txt"
    with open(file, 'wb') as f:
        html = get_page_index(0)
        print(type(html.encode('utf-8')))
        f.write(html.encode('utf-8'))

def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')



def get_page_detail(url):
    pass
    # print("请求详情页 "， )



def main():
    html = get_page_index(0)
    for url in parse_page_index(html):
        print(url)

if __name__ == "__main__":
    main()
