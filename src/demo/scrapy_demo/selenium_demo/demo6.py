from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.zhihu.com/explore"
br = webdriver.Chrome()

br.get(url)
br.execute_script("window.scrollTo(0, document.body.scrollHeight)")
br.execute_script('alert("To Button")') # 下拉框
time.sleep(5)
br.close()
url = "http://www.sina.com.cn/mid/search.shtml?q=%E6%B1%9F%E8%8B%8F%E5%BC%91%E6%AF%8D%E7%94%B7%E5%AD%A9%E8%A2%AB%E6%8A%93"
br.get(url)
time.sleep(5)
html = br.page_source
print(type(html))
print(dir(html))

file = "demo.txt"

print(html)

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
input1 = wait.until(EC.presence_of_all_elements_located(By.ID, 'q'))
button = wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR, '.btn-search'))
print(input1, button)