from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException
from selenium.common.exceptions import NoSuchAttributeException, NoSuchElementException
import time
br = webdriver.Chrome()
# ajax请求
# 1 隐式等待 默认0
br.implicitly_wait(10)

# 2 显示等待
#   等待条件和最长等待时间
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
br.get("https://www.taobao.com")
wait = WebDriverWait(br, 10)
try:
    input1 = wait.until(EC.presence_of_all_elements_located((By.ID, 'q')))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    print(input1, button)
    print(br.get_cookies())
except NoSuchElementException as e:
    print(e.msg)

try:
    print(br.add_cookie({"name": "name", "domain": "www.taobao.com", 'value': "test"}))
    print(br.get_cookies())
    print("delete all cookies...")
    print(br.delete_all_cookies())
    print(br.get_cookies())
except InvalidArgumentException as e:
    print(e.msg)
    print(e)

finally:
    time.sleep(10)
    br.close()
