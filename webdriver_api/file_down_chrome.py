'''
Author: 虫师
Date: 2016/12/1
Method:
  * download.default_directory 指定文件下载路径。
  * profile.default_content_settings.popups 设置0，禁止下载时弹出窗口。
'''
from selenium import webdriver
import os
import time

#创建Chrome浏览器配置对象实例
options = webdriver.ChromeOptions()

#定义弹窗模式和文件存放路径
prefs = {'profile.default_content_settings.popups': 0,
         # 'download.default_directory': os.getcwd() //代表下载文件存储在当前目录下
        'download.default_directory': 'd:\\file_down\\chromedriver_win32.zip' #
         }

#将自定义设置添加到Chrome配置对象实例中
options.add_experimental_option('prefs', prefs)

#启动浏览器
driver = webdriver.Chrome(options=options)
driver.get("http://npm.taobao.org/mirrors/chromedriver/")

driver.find_element_by_link_text("80.0.3987.106/").click()

driver.find_element_by_link_text('chromedriver_win32.zip').click()

time.sleep(3)
driver.quit()
