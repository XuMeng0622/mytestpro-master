'''
Author: 虫师
Date: 2016/11/22
Method:
  *  switch_to.frame()  进入表单
  *  switch_to.default_content()  退出表单至根页面
'''
from selenium import webdriver
import os, time


driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('./web_page/frame.html')
driver.get(file_path)

#先通过 xpth 定位到 iframe
# xf = driver.find_element_by_xpath('//*[@class="if"]') ##方式二:xf = driver.find_element_by_xpath('//*[@id="if"]')
# 再将定位对象传给 switch_to.frame()方法
# driver.switch_to.frame(xf)

# 切换到 iframe（id="if"）
driver.switch_to.frame("nf") ##默认直接去表单的id或者name,如果id和name都没有，则通过xpath定位iframe
# 下面就可以正常的操作元素了
driver.find_element_by_id("kw").send_keys("selenium3.0")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.quit()
