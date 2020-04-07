from  selenium import webdriver
import time
import threading
from selenium.webdriver import Remote

##该程序的目的是实现多线程分布执行测试用例
def test_baidu(host, browser):
    print('start:%s' %time.ctime())
    print('host:%s, brower:%s' %(host,browser))

    driver = Remote(command_executor=host,
                desired_capabilities={'platform':'ANY',
                                      'browserName':browser,
                                      'version':'',
                                      'javascriptEnabled':True
                                      }
                )

    driver.implicitly_wait(3)
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(browser)
    driver.find_element_by_id('su').click()
    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    lists = {
        # 'http://127.0.0.1:4444/wd/hub': 'chrome',
        'http://127.0.0.1:5555/wd/hub': 'firefox',
        'http://127.0.0.1:5556/wd/hub': 'MicrosoftEdge',
        'http://192.168.1.103:5556/wd/hub':'MicrosoftEdge',
    }

    threads = []
    count = len(lists)

    for host, chrome in lists.items():
        t = threading.Thread(target=test_baidu, args = (host, chrome))
        threads.append(t)

    for i in range(count):
        threads[i].start()

    for i in range(count):
        threads[i].join()

    print('end: %s' % time.ctime())
