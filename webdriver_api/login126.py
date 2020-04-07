'''
Author: 虫师
Date: 2016/11/22
Method:
  *  clear()   清除输入框的内容
  *  send_keys()   输入框输入
  *  click()   点击任何可点击的元素（按钮、链接、复选框等）
  *  switch_to.frame()  进入表单
  *  switch_to.default_content()  退出表单至根页面
'''
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.126.com")
driver.implicitly_wait(10)

driver.find_element_by_id('switchAccountLogin').click() ##需要先通过'密码登录'按键切换

try:
    frame = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[3]/div[4]/div[1]/div/iframe')
    driver.switch_to.frame(frame)
    time.sleep(5)
except Exception as e:
    print(e)

driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("username")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_id("dologin").click()
# driver.switch_to.default_content()
time.sleep(2)
driver.quit()
