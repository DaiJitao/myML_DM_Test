import re
from urllib.parse import urlparse
from urllib.parse import urlsplit
import urllib.parse

url = 'http://comment5.news.sina.com.cn/comment/skin/default.html?channel=cj&newsid=comos-hqfskcn9473453&group=0'
def get_query(url):
    result = urlsplit(url)
    query = dict(urllib.parse.parse_qsl(result.query))
    return query


if __name__ == "__main__":
    query = get_query(url)
    print(query['channel'])
    print(query['newsid'])

