from selenium import webdriver
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
input1 = wait.until(EC.presence_of_all_elements_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable(
                                                 (By.CSS_SELECTOR, '.btn-search')
                                              )
                    )
print(input1, button)
br.close()