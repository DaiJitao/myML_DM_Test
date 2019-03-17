from selenium import webdriver

driver = webdriver.PhantomJS()

html = '<!DOCTYPE html><!--STATUS OK-->' \
       '<html>' \
       '<head>' \
       '<meta content="text/html;charset=utf-8" http-equiv="content-type"/>' \
       '<meta content="IE=Edge" http-equiv="X-UA-Compatible"/>' \
       '<link href="//b1.bdstatic.com" rel="dns-prefetch"/>' \
       '<title>百度一下，你就知道</title>'

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print(soup.title.text)

print(soup.title.name)
print(soup.meta.attrs['http-equiv'])
print(soup.html.string)
print(soup.html.text)
print(soup.html.title.string)
print(soup.html.contents)
for i in soup.html.contents:
    print(i)
    print()