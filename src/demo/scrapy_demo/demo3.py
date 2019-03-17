from pyquery import PyQuery as pq
# pip install pyquery


doc = pq("<html>hello</html>")

print(doc('html').text())

import pymysql as sql

conn = sql.connect(host="localhost", user="root", password="123", port=3306, db='mysql')
print(conn)
curser = conn.cursor()
content = curser.execute("show tables")
print(curser.fetchall())
print(content)

import pymongo
import redis
from selenium import webdriver


url = "https://weibo.com/fengxiaogang?is_hot=1"
browser = webdriver.Chrome()
browser.get("https://weibo.com/fengxiaogang?is_hot=1")
print(browser.page_source)