from selenium import webdriver
browser=webdriver.Chrome()
# browser=webdriver.PhantomJS()
url = "http://www.baidu.com"


query = """
                var keywordInput = document.getElementById("kw") ;  // 根据全局唯一的ID获取输入框对象
                keywordInput.value = "selenium" ;
                setTimeout(function() {
                    // 延迟 5 秒点击查询按钮（setTimeout是异步执行）
                    var queryBtn = document.getElementById("su") ;  // 根据全局唯一的ID获取查询按钮对象
                    queryBtn.click() ;
                } , 5000) ;
                """

try:
    browser.get(url)
    browser.implicitly_wait(10)
    browser.execute_script(query)
    # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # browser.execute_script("alert('To Button')")
    #browser.close()
    html = browser.page_source
    print(html)

finally:
    import time
    time.sleep(20)
    browser.close()

