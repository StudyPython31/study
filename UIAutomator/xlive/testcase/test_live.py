# -*- coding:utf-8 -*-
import unittest,os,time
from PO.livePage import LiveStartPage
from appium_config import DriverClient
from PO.signPage import SignPage
from PO.common import Action
from appium import webdriver
class Myprofile(unittest.TestCase):

   def setUp(self):
       self.driver = DriverClient().getDriver()


   def tearDown(self):
       pass

      # self.driver.quit()

   def test001_startopenlive(self):
       ac = Action(self.driver)
       sp = SignPage(self.driver)
       '''如果有签到弹框，则关闭弹框'''
       time.sleep(5)
       if (ac.isElementExist(sp.closebtn_loc)):
           sp.closesign()

       ls = LiveStartPage(self.driver)
       ls.startopenlive()
       ls.closeopenliveroom()

   def test002_startprivatelive(self):
       ac = Action(self.driver)
       sp = SignPage(self.driver)
       '''如果有签到弹框，则关闭弹框'''
       time.sleep(5)
       if (ac.isElementExist(sp.closebtn_loc)):
           sp.closesign()


       ls = LiveStartPage(self.driver)
       ls.startprivatelive('8888')