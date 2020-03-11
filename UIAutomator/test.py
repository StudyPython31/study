# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
import unittest,time
import HTMLTestRunner

from appium.webdriver.common.touch_action import TouchAction


class Login(unittest.TestCase):
    def setUp(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "CEEE5T4DFYLVHEGE"
        caps["appPackage"] = "com.xxxx"
        #caps["appActivity"] = "xxxx"
        caps["appActivity"] = "xxxx"
        caps['automationName'] = 'uiautomator2'
        caps['noReset'] = 'true'
        caps['fullReset'] = 'fullReset'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.wait_activity("XXXX", 5)

    def tearDown(self):
        self.driver.quit()

    def findElement(self,driver,id):
        try:
            #self.driver.find_element_by_id("com.xxxx:id/dev_btn").is_displayed()
            WebDriverWait(driver,2).until(lambda diver:driver.find_element_by_id(id))
            return True
        except exceptions.TimeoutException:
            return False
        except exceptions.NoSuchElementException:
            return False


    def test001_login(self):
        el1 = self.driver.find_element_by_id("com.xxxx:id/btnPhone2")
        time.sleep(3)
        el1.click()

        #el11 = self.driver.find_element_by_id("com.xxxx:id/tv_agreement_ensure").is_displayed()
        el11 = self.findElement(self.driver,"com.xxxx:id/tv_agreement_ensure")
        print("1111111111111111111")
        if(el11):
            print("22222222")
            el12 = self.driver.find_element_by_id("com.com.xxxx:id/tv_agreement_ensure")
            el12.click()
            time.sleep(3)
            el1.click()

        print("333333333333")
        #el = self.driver.find_element_by_id("com.com.xxxx:id/rlContainer")
        action = TouchAction(self.driver)
        action.long_press(x=560,y=1300,duration=3000).perform()
        #changeenv = self.driver.find_element_by_id("com.xxxx:id/dev_btn").is_displayed()
        changeenv = self.findElement(self.driver,"com.xxxx:id/dev_btn")
        #print("444444444444444444444:"+changeenv)
        if(changeenv):
            self.driver.find_element_by_id("com.xxxx:id/dev_btn").click()
            print("6666666666666666")
            time.sleep(5)
            if(changeenv):
                print("7777777777777777")
                action.tap(x=560,y=1600).perform()
                print("5555555")
            else:
                print("88888888888888")
                el1.click()
        #self.driver.find_element_by_id("com.xxxx:id/dev_btn").click()

        el2 = self.driver.find_element_by_id("com.xxxx:id/userId")
        el2.send_keys("XXX")
        el3 = self.driver.find_element_by_id("com.xxxx:id/passWord")
        el3.send_keys("12345678")
        el4 = self.driver.find_element_by_id("com.xxxx:id/btn_login")
        el4.click()
        time.sleep(3)
        action.tap(x=560, y=600).perform()
        print("9999999999")

        shouye = self.driver.find_element_by_id("com.xxxx:id/ll_tab_home").is_displayed()
        #huati = self.driver.find_element_by_id("com.xxxx:id/ll_voice_chat")
        #
        self.assertTrue(shouye)
suite = unittest.TestSuite()
suite.addTest(Login('test001_login'))


now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
report_file = ".\\report\\appium_report_"+now+".html"
fp = open(report_file,'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Appium测试报告',description='登录')
runner.run(suite)
fp.close()


