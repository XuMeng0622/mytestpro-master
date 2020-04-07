'''
Author: 虫师
Date: 2016/11/22
Method:
  *  set_window_size()   设置浏览器宽、高
  *  maximize_window()   设置浏览器全屏
'''
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://m.baidu.com")
time.sleep(3)

#设置浏览器宽 480、高 600 显示
driver.set_window_size(480, 600)
time.sleep(3)

#设置浏览器全屏
driver.maximize_window()
time.sleep(3)

driver.quit()
