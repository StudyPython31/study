from appium import webdriver

class AppiumTest():

    def __init__(self):

        caps = {}
        caps["platformName"] = "Android"
        caps["plateformVersion"] = "7.1"
        caps["deviceName"] = "OJFEU46LFU594HSS"
        caps["udid"] = 'OJFEU46LFU594HSS'
        caps["appPackage"] = "com.XXXX"
        caps["appActivity"] = '.XXXX'  #".XXXX.ChatStartActivity"
        caps['automationName'] = 'uiautomator2'
        caps['noReset'] = True
        caps['fullReset'] = False

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        #self.driver.wait_activity("XXXX.login.ChatLoginActivity", 5)
        self.driver.implicitly_wait(30)

        caps1 = {}
        caps1["platformName"] = "Android"
        caps1["plateformVersion"] = "7.1"
        caps1["deviceName"] = "a46ed046"
        caps1["udid"] = 'a46ed046'
        caps1["appPackage"] = "XXXX"
        caps1["appActivity"] = 'XXXX'  # ".peiliao.avtivity.ChatStartActivity"
        caps1['automationName'] = 'uiautomator2'
        caps1['noReset'] = True
        caps1['fullReset'] = False

        self.driver1 = webdriver.Remote("http://localhost:4724/wd/hub", caps1)
        # self.driver.wait_activity("XXXX.login.ChatLoginActivity", 5)
        self.driver1.implicitly_wait(30)



    def get_driver(self):
        return self.driver

    def get_driver1(self):
        return self.driver1
