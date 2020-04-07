#-*- coding:utf-8 -*-
import time
from selenium import webdriver

driver = webdriver.Chrome()
success = 0
fail = 0

def get_data_from_txt():
    with open('./test_data.txt', 'rt', encoding='utf-8') as fin:
        data = fin.readlines()
        fin.close()

    return data

def search_webpage(data):
    global success
    global fail
    driver.implicitly_wait(5)
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(data[0])
    driver.find_element_by_id('su').click()
    time.sleep(3)

    #断言，判定网页是否包含关键字
    try:
        assert data[1] in driver.page_source
        success = success + 1
    except AssertionError as e:
        print('%s not in page source' % data[1])
        fail = fail + 1

def out_report():
    print('总共 %r 个测试用例，通过 %r 个，失败 %r 个' %(total, success, fail))

if __name__ == '__main__':
    data_list = get_data_from_txt()
    data_len = len(data_list)
    total = data_len

    if 0 == data_len:
        print('data is null, please add data')
        exit(0)

    for data in data_list:
        data = data.strip('\n').split('||')
        print(data)
        search_webpage(data)

    out_report()
    driver.quit()
