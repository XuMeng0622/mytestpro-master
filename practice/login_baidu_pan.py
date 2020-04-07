# -*- coding:utf-8 -*-

import time
from selenium import webdriver

def login(username, password):
    driver.implicitly_wait(10)
    driver.get('https://pan.baidu.com/')
    # cookie1 = driver.get_cookies()
    # print(cookie1)
    driver.add_cookie({'name':'Login_UserNumber', 'value':'546266734@qq.com'})
    driver.add_cookie({'name': 'Login_Passwd', 'value': 'x2603331413'})
    driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__footerULoginBtn"]').click()
    driver.find_element_by_name('userName').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_id('TANGRAM__PSP_4__submitWrapper').click()

    cookie1 = driver.get_cookies()
    print(cookie1)

if __name__ == '__main__':
    username = '546266734@qq.com'
    password = 'x2603331413'

    driver = webdriver.Chrome()
    login(username, password)

