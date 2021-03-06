'''
Author: 虫师
Date: 2016/11/22
Method:
  * send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
  * send_keys(Keys.SPACE) 空格键(Space)
  * send_keys(Keys.TAB) 制表键(Tab)
  * send_keys(Keys.ESCAPE) 回退键（Esc）
  * send_keys(Keys.ENTER) 回车键（Enter）
  * send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
  * send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
  * send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
  * send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
  * send_keys(Keys.F1) 键盘 F1
  ……
  * send_keys(Keys.F12) 键盘 F12
'''
from selenium import webdriver
# 引入 Keys 模块
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")


# 输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")
time.sleep(3)

# 删除多输入的一个 m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(3)

# 输入空格键+“教程”
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
time.sleep(3)
driver.find_element_by_id("kw").send_keys("教程")
time.sleep(3)

# ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
time.sleep(3)

# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
time.sleep(3)

# ctrl+v 粘贴内容到输入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
time.sleep(3)

# 通过回车键来代替单击操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)

time.sleep(3)
driver.quit()
