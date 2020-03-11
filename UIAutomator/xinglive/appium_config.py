# coding=UTF-8
'''Appium Driver的封装'''
from appium import webdriver



class AppiumTest():
    driver = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            orig = super(AppiumTest,cls)

            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0.1'
            desired_caps['deviceName'] = '732f063'
            desired_caps['app'] = 'D:/UIAutomator/package/app-release.apk'
            desired_caps['appPackage'] = 'com.qixingzhibo.living'
            desired_caps['appActivity'] = 'com.qiyu.live.activity.StartActivity'
            desired_caps['automationName'] = 'uiautomator2'
            desired_caps['noReset'] = 'true'

            cls._instance = orig.__new__(cls, *args, **kwargs)
            cls._instance.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return cls._instance

class DriverClient(AppiumTest):

    def getDriver(self):
        return self.driver