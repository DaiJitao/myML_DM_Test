from selenium import webdriver
#
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
url = "https://weibo.com/newsxh?topnav=1&wvr=6&topsug=1&is_hot=1"
try:
    browser.get(url=url)
    print(browser.page_source)
except Exception:
    pass
finally:
    browser.close()