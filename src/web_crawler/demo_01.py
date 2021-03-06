#coding:utf-8

from urllib import request
from urllib import error


def download(url, num_retries = 2):
    print("downloading...", url)
    try:
        html = request.urlopen(url)
    except error.URLError as e:
        print("download error: ", e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                print("Try again %d times..." %num_retries)
                return download(url, num_retries - 1)
    return html

html = download("http://www.baidu.com", 2)

# from bs4 import BeautifulSoup
# bsObj = BeautifulSoup(html.read())
# print(bsObj.head.link)

html = download("")

http: // localhost: 8086 / sentimentPloarity / sentimentPloarityCar?taskData = {
	"taskId": "S:20190614121212334:3212",
	"count": 2,
	"data": [
		{
			"assetId": "4378847782428538",
			"siteId": "",
			"siteName": "",
			"channelId": "",
			"channel": "",
			"title": "",
			"content": "中文文本内容",
			"infoType": ""
		}
	]
}
