'''
unittest + selenium 用例
'''
from selenium import webdriver
import unittest, time


class BaiduIde(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.youdao.com"

    def test_baidu_ide(self):
        driver = self.driver
        driver.get(self.base_url)
        # search_text = driver.find_element_by_id("translateContent")
        # search_text.clear()
        # search_text.send_keys("webdriver")
        # driver.find_element_by_xpath('//*[@id="form"]/button').click()
        time.sleep(2)
        self.assertEqual("有道首页", driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
