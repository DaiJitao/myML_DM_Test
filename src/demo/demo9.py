import urllib.request
import urllib.parse
import json

"""
Host: 192.168.20.53:81
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: application/json
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Length: 83
Connection: keep-alive
Pragma: no-cache
"""
url = 'http://192.168.20.53:81/SearchSvc/CVWebService.svc/Login'
headers = {
    'Host': '192.168.20.53:81',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Accept': 'application/json',
    'Content-type': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'

}

values = {

    "username": "admin",
    "password": "UEBzc3cwcmQ="
}
data = urllib.parse.urlencode(values).encode('utf-8')
request = urllib.request.Request(url, data=data, headers=headers)
html = urllib.request.urlopen(request).read()
print(json.loads(html))
