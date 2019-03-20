import pymongo
from selenium import webdriver

url = "https://www.toutiao.com/a6669576220562162179/"
browser = webdriver.Chrome()
browser.get(url)

try:
    print(browser.page_source)
except Exception as e:
    print(e.args)
    print(e.msg)
    browser.close()

finally:
    import time
    time.sleep(5)
    browser.close()

