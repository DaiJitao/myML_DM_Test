from selenium import webdriver


url = "https://www.zhihu.com/explore"
br = webdriver.Chrome()

br.get(url)
br.execute_script("window.scrollTo(0, document.body.scrollHeight)")
br.execute_script('alert("To Button")')

