from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import pickle

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument('--headless')
login_url = "https://passport.csdn.net/login"
browser = webdriver.Chrome()
browser.get("https://weibo.com/newsxh?topnav=1&wvr=6&topsug=1&is_hot=1")
print(browser.page_source)
def login():
    browser.delete_all_cookies()
    browser.get(login_url)

    intput_name = browser.find_element_by_id('all')
    input_pwd = browser.find_element_by_id("pwd")
    lgn_btn = browser.find_element_by_class_name('btn')
    print(lgn_btn)
    intput_name.send_keys("976185561@qq.com")
    input_pwd.send_keys("csdndjt123")
    lgn_btn.click()
    print(browser.current_url)
    pickle.dump(browser.get_cookie(), open('cookies.pkl', 'wb'))
    print("cookies : ", browser.get_cookie())


import time
time.sleep(5)
browser.quit()