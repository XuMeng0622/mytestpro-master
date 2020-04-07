'''
Author: 虫师
Date: 2016/11/22
'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# driver.find_element_by_id("kw").send_keys("Selenium3")
# driver.find_element_by_name('wd').send_keys('selenium')
# driver.find_element_by_class_name('s_ipt').send_keys('selenium')
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('腾讯')
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/form/span[1]/input').send_keys('腾讯')
driver.find_element_by_css_selector('#kw').send_keys('selenium')

driver.find_element_by_id("su").click()  ##单击元素

# driver.quit()