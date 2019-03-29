from selenium import webdriver
from selenium.webdriver.common.by import By

import requests

index = "https://finance.sina.com.cn/chanjing/gsnews/2019-01-16/doc-ihqhqcis6564551.shtml"

options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument('--headless')

browser = webdriver.Chrome(options=options)
browser.get(index)
print(browser.page_source)

print(browser.find_element_by_css_selector("a.more").get_attribute())
