'''
Author: 虫师
Date: 2016/12/1
Method:
  * text：返回 alert/confirm/prompt 中的文字信息。
  * accept()：接受现有警告框。
  * dismiss()：解散现有警告框。
  * send_keys(keysToSend)： 发送文本至警告框。 keysToSend：将文本发送至警告框。
'''
from selenium import webdriver
from time import sleep
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_link_text("设置").click()
# temp = driver.find_element_by_name("tj_settingicon").click() # 执行时会提示element not interactable ???
# driver.find_element_by_class_name("setpref").click() #通过
# driver.find_element_by_link_text('搜索设置').click()

# sleep(2)
# #
# # 保存设置
# driver.find_element_by_class_name("prefpanelgo").click()
# sleep(2)
#
# # 接受警告框
# driver.switch_to.alert.accept()
#
# time.sleep(2)
#
# driver.quit()