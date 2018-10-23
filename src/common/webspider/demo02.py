import requests
from urllib import parse #用于编码


"""
r 只能读 
r+ 可读可写，不会创建不存在的文件，从顶部开始写，会覆盖之前此位置的内容
w+ 可读可写，如果文件存在，则覆盖整个文件，不存在则创建
w 只能写，覆盖整个文件，不存在则创建 
a 只能写，从文件底部添加内容 不存在则创建 
a+ 可读可写 从文件顶部读取内容 从文件底部添加内容 不存在则创建
"""
save_file_path = 'E:\pycharm_workspace\myML_DM_Test\src\common\webspider'

def get_url(book_name):
    search_text = parse.quote(book_name)
    url = "https://book.douban.com/subject_search?search_text=" + search_text +  "&cat=1001"
    return url


def get_Html(url, user_agent='wswp', num_retries=2):
    print("downLoading", url)
    headers = {'User-agent': user_agent}
    try:
        res = requests.get(url,headers)
        print(res.status_code)
        print(res.reason)
        print(res.headers)
    except Exception as e:
        print(e)
        if num_retries > 0:
            if res.status_code == 503:
                num_retries -= 1
                return get_Html(url=url, num_retries=num_retries)
    text = res.text
    return text

def save_file(path, name, msg):
    path = path + "\\" + name
    with open(path, 'w', encoding='utf-8') as f:
        f.write(msg)
        f.flush()

name = '情人'
url = get_url(book_name=name)
msg = get_Html(url=url)
save_file(save_file_path, name=name, msg=msg)








