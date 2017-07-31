import urllib2

response = urllib2.urlopen("http://www.xiaojukeji.com/index/index")
#print response.read()

response = urllib2.urlopen("http://wx4.sinaimg.cn/mw690/bfdcef89gy1fdd9j7jnsjj208c046q3c.jpg")
f = open("D://data.jpg", 'wb')
f.write(response.read())
