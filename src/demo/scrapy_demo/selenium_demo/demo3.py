from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import time

browser = webdriver.Chrome()

try:
    browser.get("https://www.baidu.com")
    input1 = browser.find_element_by_id('su')
    print(input1.tag_name)
    input1.send_keys("python")
    input1.send_keys(Keys.ENTER)
    # wait = WebDriverWait(browser, 10)
    # wait.until(ec.presence_of_all_elements_located(By.ID, 'content_left'))
    print(browser.current_url)
    # print(browser.get_cookie())
    # print(browser.page_source)
    time.sleep(5)

except Exception:
    print(Exception)
finally:
    browser.close()