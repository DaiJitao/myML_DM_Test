from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# webdriver.PhantomJS()
# webdriver.Edge()

browser.get("https://www.taobao.com")
print(browser.page_source)
import time
time.sleep(10)
input_first = browser.find_element(By.ID, 'q')
print(input_first)
browser.close()

