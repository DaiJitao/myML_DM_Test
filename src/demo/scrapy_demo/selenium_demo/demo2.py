from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# webdriver.PhantomJS()
# webdriver.Edge()

browser.get("https://www.taobao.com")

import time

input_first = browser.find_elements_by_css_selector(".J_Cat a-all li")
dd = browser.find_elements(By.ID, "J_Cat")
d2 = browser.find_elements(By.CSS_SELECTOR, "J_Cat")
print(d2)

input = browser.find_element_by_id('q')
input = input.send_keys('iphone')
time.sleep(20)
browser.close()

