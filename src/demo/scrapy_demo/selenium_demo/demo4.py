from selenium import webdriver
# browser=webdriver.Chrome()
browser=webdriver.PhantomJS()
url = "https://weibo.com/huaweiweibo?is_hot=1#1552906379483"
try:
    browser.get(url)
    # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # browser.execute_script("alert('To Button')")
    #browser.close()
    html = browser.page_source
    print(html)

finally:
    import time
    time.sleep(20)
    browser.close()

