'''
Author: 虫师
Date: 2016/11/24
Method:
  *  title         获取当前页面title
  *  current_url   获取当前页面URL
  *  text          获得文本信息
'''
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.126.com")

print('Before login================')
# 打印当前页面 title
title = driver.title
print(title)

# 打印当前页面 URL
now_url = driver.current_url
print(now_url)

driver.find_element_by_id('switchAccountLogin').click() ##需要先通过'密码登录'按键切换

iframe = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[3]/div[4]/div[1]/div/iframe')
driver.switch_to.frame(iframe)

# 执行邮箱登录
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("username")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()
time.sleep(5)

print('After login================')
# 再次打印当前页面 title
title = driver.title
print(title)

# 打印当前页面 URL
now_url = driver.current_url
print(now_url)

# 获得登录的用户名
# user = driver.find_element_by_id('spnUid').text
user = driver.find_element_by_xpath('//*[@id="auto-id-1584943945738"]').text
print(user)

driver.quit()
