import requests
from  requests.exceptions import RequestException

def get_index_page(url):
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

url = 'http://news.sina.com.cn/hotnews/'

print(get_index_page(url))


''' 待完成... '''