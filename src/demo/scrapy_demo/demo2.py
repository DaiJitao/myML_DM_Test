from selenium import webdriver
b = webdriver.PhantomJS()

b.get("http://www.baidu.com")
print(b.page_source)

html = b.page_source

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup)