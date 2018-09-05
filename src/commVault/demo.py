#coding:utf-8
import json
import http.client
import urllib
from urllib import parse, request

Accept = 'application/json'
Contenttype = 'application/json'

def getToken():
    url = 'http://192.168.20.53:81/SearchSvc/CVWebService.svc/Login'
    body = {"mode":"Webconsole","username":"admin","password":"UEBzc3cwcmQ="}
    # body = json.dumps(body)
    data = urllib.parse.urlencode(body).encode('utf-8')
    print(data)
    headers_dict = {'Accept':Accept, 'Content-type':Contenttype}
    # req = request.Request(url=url, data=data, headers=headers_dict) # , method='POST'
    conn = http.client.HTTPConnection(url)
    res = request.urlopen(req)
    ret = res.read()
    jsonData = json.loads(ret)
    print(jsonData)




getToken()


