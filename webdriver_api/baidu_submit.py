'''
Author: 虫师
Date: 2016/11/22
Method: 
  *  submit()   提交表单内容
'''

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

search = driver.find_element_by_id("kw")
search.send_keys("Selenium3")
search.submit()  #提交表单代替'click()'

time.sleep(10)
driver.quit()
