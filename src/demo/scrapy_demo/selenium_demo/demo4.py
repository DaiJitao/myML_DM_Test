from selenium import webdriver
browser=webdriver.Chrome()
try:
    browser.get("https://www.zhihu.com/explore")
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    browser.execute_script("alert('To Button')")
    browser.close()
finally:
    browser.close()

