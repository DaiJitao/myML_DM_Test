from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

main_URL = 'https://www.sina.com.cn/'

browser = webdriver.Chrome()
browser.get(main_URL)

input1 = browser.find_element_by_class_name('inp-txt')
input2 = browser.find_element_by_name('SerchKey')
input3 = browser.find_element_by_css_selector("input.inp-txt")
print(input1.text)
print(input2.text)
print(input3.text)
print(input3.get_attribute("class"), input3.get_attribute('name'))
input2.send_keys("腾讯")
print("==========================")
print(input3.location)
print(input3.size)

submit = browser.find_element_by_class_name('submit-second-btn')
print(submit.tag_name)
print(submit.get_attribute('class'))
submit.submit()
time.sleep(5)
browser.close()
