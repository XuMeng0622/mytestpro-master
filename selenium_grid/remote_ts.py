from selenium.webdriver import Remote
import time

lists = {
'http://127.0.0.1:4444/wd/hub':'chrome',
'http://127.0.0.1:5555/wd/hub':'firefox',
# 'http://127.0.0.1:5556/wd/hub':'MicrosoftEdge',
'http://192.168.1.103:5556/wd/hub':'MicrosoftEdge',
# 'http://127.0.0.1:5557/wd/hub':'Internet explorer',
}

for host, browser in lists.items():
    print(host, browser)
    driver = Remote(command_executor=host,
                desired_capabilities={'platform':'ANY',
                                      'browserName':browser,
                                      'version':'',
                                      'javascriptEnabled':True
                                      }
                )
    driver.implicitly_wait(3)
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(browser+host)
    driver.find_element_by_id('su').click()

    time.sleep(3)
    #driver.quit()
    driver.close()


