# -*- coding: utf-8 -*-
'''2018年春运火车票抢票
火车票预订时间对照：
2月13日（廿八） 
2月14日（廿九） 
2月15日（除夕） 
2月19日（初四）
2月20日（初五）
2月21日（初六）
2月22日（初七）
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
import time

value_fromstation = '%u5317%u4EAC%u897F%2CBXP'  # 始发站（北京西）
value_tostation = '%u77F3%u5BB6%u5E84%2CSJP'  # 终点站（石家庄）
value_date = '2019-10-1'  # 出发时间


def login_proc(username, password):
    # 打开登录页面 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
    sel = webdriver.Chrome()
    # sel=webdriver.Firefox()
    sel.implicitly_wait(30)
    login_url = 'https://kyfw.12306.cn/otn/login/init'
    sel.get(login_url)
    # sign in the username
    try:
        user_input = sel.find_element_by_id("username")
        user_input.clear()
        user_input.send_keys(username)
        print ("user-id write success!")
    except:
        print ('user-id write error!')
    # sign in the pasword
    try:
        pwd_input = sel.find_element_by_id("password")
        pwd_input.clear()
        pwd_input.send_keys(password)
        print ('pw write success!')
    except:
        print ('pw write error!')

    # Check for Login success
    while True:
        curpage_url = sel.current_url
        if curpage_url != login_url:
            if curpage_url[:-1] != login_url:  # choose wrong verify_pic
                print ('Login finished!')
                break
        else:
            time.sleep(5)
            print (u'------------>等待用户图片验证')
    return sel


def search_proc(sel, train_type='', timer=False):
    print (u'--------->选择车次类型', train_type)
    # 定时抢票时间点
    if timer == True:
        while True:
            current_time = time.localtime()
            if ((current_time.tm_hour == 14) and (current_time.tm_min >= 25) and (
                        current_time.tm_sec >= 00)):
                print (u'开始刷票...')
                break
            else:
                time.sleep(5)
                if current_time.tm_sec % 30 == 0:
                    print (time.strftime('%H:%M:%S', current_time))

    # 打开订票网页
    book_url = 'https://kyfw.12306.cn/otn/leftTicket/init'
    sel.get(book_url)
    # 始发站
    # sel.find_element_by_id('fromStationText').click()
    # from_station = sel.find_element_by_xpath('//*[@id="ul_list1"]/li[32]') # 深圳
    # from_station.click()
    sel.add_cookie({"name": "_jc_save_fromStation", "value": value_fromstation})
    # 终点站
    # sel.find_element_by_id('toStationText').click()
    # sel.find_element_by_id('nav_list3').click()#点击事件
    # tation = sel.find_element_by_xpath('//*[@id="ul_list1"]/li[9]') # 广州
    # to_station.click()
    sel.add_cookie({"name": "_jc_save_toStation", "value": value_tostation})
    # 出发日期
    # date_sel = sel.find_element_by_id('train_date')
    # js = "document.getElementById('train_date').removeAttribute('readonly')" # del train_date readonly property
    # sel.execute_script(js)
    # date_sel.clear()
    # date_sel.send_keys(leave_date)
    sel.add_cookie({"name": "_jc_save_fromDate", "value": value_date})
    sel.refresh()
    # 车次类型选择
    train_type_dict = {'T': '//input[@name="cc_type" and @value="T"]',  # 特快
                       'G': '//input[@name="cc_type" and @value="G"]',  # 高铁
                       'D': '//input[@name="cc_type" and @value="D"]',  # 动车
                       'Z': '//input[@name="cc_type" and @value="Z"]'}  # 直达
    if train_type == 'T' or train_type == 'G' or train_type == 'D' or train_type == 'Z':
        sel.find_element_by_xpath(train_type_dict[train_type]).click()
    else:
        print (u"车次类型异常或未选择!(train_type=%s)" % train_type)


def book_proc(sel, refresh_interval=0):
    # 等待状态查询
    query_times = 0
    time_begin = time.time()
    while True:
        # 循环查询
        time.sleep(refresh_interval)
        # 开始查询 @id="ZE_6c000D281201"
        search_btn = WebDriverWait(sel, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="query_ticket"]')))
        search_btn.click()
        # 扫描查询结果
        try:
            # D6721
            tic_tb_item = WebDriverWait(sel, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="ZY_24000D672106"]')))
            # G381
            # tic_tb_item = WebDriverWait(sel,20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ZE_240000G38107"]')))
            tic_ava_num = tic_tb_item.text
        except:  # 应对查询按钮一次点击后,网站未返回查询结果
            search_btn.click()
            # D6721
            tic_tb_item = WebDriverWait(sel, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="ZY_24000D672106"]')))
            # G381
            # tic_tb_item = WebDriverWait(sel,20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ZE_240000G38107"]')))
            tic_ava_num = tic_tb_item.text

        if tic_ava_num == u'无' or tic_ava_num == u'*':  # 无票或未开售
            query_times += 1
            time_cur = time.time()
            print (u'第%d次查询,总计耗时%s秒' % (query_times, time_cur - time_begin))
            continue
        else:
            # 订票 @id="ticket_6c000D281201"
            sel.find_element_by_xpath('//*[@id="ticket_24000D672106"]/td[13]/a').click()  # D6721
            # sel.find_element_by_xpath('//*[@id="ticket_240000G38107"]/td[13]/a').click()  # G381
            break
    # 判断页面跳是否转至乘客选择页面
    cust_sel_url = 'https://kyfw.12306.cn/otn/leftTicket/init'
    while True:
        if (sel.current_url == cust_sel_url):
            print (u'页面跳转成功!')
            break
        else:
            print (u'等待页面跳转...')
    # 乘车人选择
    while True:
        try:
            sel.find_element_by_xpath('//*[@id="normalPassenger_0"]').click()
            #sel.find_element_by_xpath('//*[@id="normalPassenger_1"]').click()
            break
        except:
            print (u'等待常用联系人列表...')

    # 席别选择
    # 提交订票
    #sel.find_element_by_xpath('//*[@id="submitOrder_id"]').click()
    # 确认订票信息
    while True:
        try:
            sel.switch_to.frame(sel.find_element_by_xpath('//*[@id="body_id"]/iframe[2]'))
            print
            sel.find_element_by_xpath('//*[@id="qr_submit_id"]').click()
            print ('Pass!')
            break
        except:
            print (u'请手动通过图片验证码')
            time.sleep(5)
            break
    return 'yeah'


if __name__ == '__main__':
    # 变量定义
    leave_date = '2018-02-13'
    train_type = 'D'
    refresh_interval = 0.5
    timer = False

    sel = login_proc('19910781498', '你自己的密码')
    search_proc(sel, train_type, timer)
    book_proc(sel, refresh_interval)
