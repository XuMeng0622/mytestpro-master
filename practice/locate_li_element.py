from selenium import webdriver
import time

def locate_li_element():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys('上海悠悠')

    # try:
    driver.find_element_by_xpath('//*[@id="form"]/div/ul/li[2]').click()

    time.sleep(20)
    # except Exception as e:
    #     print(e)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys('上海悠悠')
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="form"]/div/ul/li[2]').click()
