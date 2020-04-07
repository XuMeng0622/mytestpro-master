'''
Author: 虫师
Date: 2016/12/1
Method:
  * execute_script() 调用JavaScript操作Web。
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10) #设置隐式等待

#百度页面搜索makeblock
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('makeblock')
driver.find_element_by_id('su').click()

#获取当前window
search_windows = driver.current_window_handle
print(search_windows)

driver.find_element_by_partial_link_text('全球 STEAM 教育解决方案提供商').click()

#获取所有window
all_handles = driver.window_handles

print(all_handles)

for handle in all_handles:
    if handle != search_windows:
        driver.switch_to.window(handle) #切换到makeblock 官网所在的window
        print(driver.title)
        element = driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/ul[1]/li[1]')
        ActionChains(driver).move_to_element(element).perform()
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/ul[1]/li[1]/div/ul/li[3]/div/ul/li[1]').click() #定位3D打印机

for handle in driver.window_handles:
    if handle not in all_handles:
        driver.switch_to.window(handle) #切换到3D打印机所在window
        video = driver.find_element_by_id('makeIdeasTangibleVideo')

        #返回播放文件地址
        url = driver.execute_script('return arguments[0].currentSrc', video)
        print(url)

        driver.find_element_by_id('playVideo2').click()
        time.sleep(15)

        print('pause')
        driver.execute_script('return arguments[0].pause()', video)
        time.sleep(6)

        print('restart')
        driver.execute_script('return arguments[0].play()', video)
        #
        #播放15秒
        time.sleep(10)
        #
        #暂停播放
        driver.execute_script('return arguments[0].pause()', video)
        time.sleep(5)

        print('quit')
        driver.quit()
