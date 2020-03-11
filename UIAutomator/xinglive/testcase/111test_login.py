
# -*- coding:utf-8 -*-
'''appium用uiautomator2可以定位toast，用xpath，xpath=//*[contains(@text,'手机号或密码xxxx')]'''
#  https://testerhome.com/topics/10077
import unittest,os,time
from PO.loginPage import CreatPage
from appium_config import AppiumTest
from PO.common import Action
from appium import webdriver

class Login(unittest.TestCase):
   def setUp(self):
      self.driver = AppiumTest().getDriver()


   def tearDown(self):
      pass

      # self.driver.quit()



   def test001_login(self):
      time.sleep(10)
      cp = CreatPage(self.driver)
      cp.loginByPhone_link()
      cp.run_caseLogin('1000051','123456789')
      action = Action(self.driver)
      res = action.getToastExit('用户不存在或密码不正确')
      self.assertTrue(res,True)


   def test002_login(self):
      time.sleep(10)
      cp = CreatPage(self.driver)
      cp.loginByPhone_link()
      cp.run_caseLogin('1000055','12345678')
      time.sleep(10)
      action = Action(self.driver)
      self.assertTrue(True,action.isElementExist('com.qixingzhibo.living:id/btn_close_attendance'))











