from  selenium import webdriver
import time
import threading

##该程序的目的是使用3个线程，分别用不同的浏览器打开百度首页进行关键字搜索
def test_baidu(browser, search):
    print('start:%s' %time.ctime())
    print('brower:%s' %browser)
    if browser == 'chrome':
        driver = webdriver.Chrome()  #不能将driver定义为全局变量，否则会出现某一个线程调用quit()后，这个程序就会崩掉，系统提示WebDriverException: Message: invalid session
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        print('无效的浏览器，请重新输入!!!')

    driver.implicitly_wait(3)
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(search)
    driver.find_element_by_id('su').click()
    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    lists = {'chrome': 'thread', 'firefox': 'webdriver', 'edge': 'edge'}
    threads = []
    count = len(lists)

    for chrome, search in lists.items():
        t = threading.Thread(target=test_baidu, args = (chrome, search))
        threads.append(t)

    for i in range(count):
        threads[i].start()

    for i in range(count):
        threads[i].join()

    print('end: %s' % time.ctime())
