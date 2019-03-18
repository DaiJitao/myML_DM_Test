from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
webdriver.PhantomJS()
# browser = webdriver.Firefox()
# webdriver.PhantomJS()
# webdriver.Edge()

browser.get("https://www.baidu.com")
print(browser.page_source)
import time
time.sleep(10)
input_first = browser.find_element_by_class_name("bg")
print(input_first)

browser.close()

