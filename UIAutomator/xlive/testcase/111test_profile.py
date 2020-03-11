# -*- coding:utf-8 -*-

import unittest,os,time
from PO.myprofilePage import MyprofilePage
from appium_config import DriverClient
from PO.signPage import SignPage
from PO.common import Action
from appium import webdriver

class Myprofile(unittest.TestCase):

   def setUp(self):
      self.driver = DriverClient().getDriver()


   def tearDown(self):

      self.driver.quit()

   '''验证昵称'''

   def test001_myprofile(self):
      ac = Action(self.driver)
      sp = SignPage(self.driver)
      '''如果有签到弹框，则关闭弹框'''
      time.sleep(5)
      if(ac.isElementExist(sp.closebtn_loc)):
          sp.closesign()
      time.sleep(5)
      '''跳转到“我的”页面'''
      mf = MyprofilePage(self.driver)
      mf.getmyprofile_link()
      nn = ac.get_id(mf.nickname_loc).text
      self.assertEquals('1000055',nn)

   '''验证id'''
   def test002_myprofile(self):
      ac = Action(self.driver)
      # sp = SignPage(self.driver)
      # '''如果有签到弹框，则关闭弹框'''
      # time.sleep(5)
      # if(ac.isElementExist(sp.closebtn_loc)):
      #     sp.closesign()
      # time.sleep(5)
      # '''跳转到“我的”页面'''
      mf = MyprofilePage(self.driver)
      # mf.getmyprofile_link()
      nn = ac.get_id(mf.userid_loc).text
      self.assertEquals('ID : 1000055',nn)

   '''验证关注数量'''

   def test003_myprofile(self):
      ac = Action(self.driver)
      # sp = SignPage(self.driver)
      # '''如果有签到弹框，则关闭弹框'''
      # time.sleep(5)
      # if(ac.isElementExist(sp.closebtn_loc)):
      #     sp.closesign()
      # time.sleep(5)
      # '''跳转到“我的”页面'''
      mf = MyprofilePage(self.driver)
      # mf.getmyprofile_link()
      nn = ac.get_id(mf.followcount_loc).text
      self.assertEquals('5', nn)

   '''验证粉丝数量'''

   def test004_myprofile(self):
      ac = Action(self.driver)
      # sp = SignPage(self.driver)
      # '''如果有签到弹框，则关闭弹框'''
      # time.sleep(5)
      # if(ac.isElementExist(sp.closebtn_loc)):
      #     sp.closesign()
      # time.sleep(5)
      # '''跳转到“我的”页面'''
      mf = MyprofilePage(self.driver)
      # mf.getmyprofile_link()
      nn = ac.get_id(mf.fanscount_loc).text
      self.assertEquals('5', nn)

   '''验证主播星级项是否显示'''
   def test005_myprofile(self):
      ac = Action(self.driver)
      # sp = SignPage(self.driver)
      # '''如果有签到弹框，则关闭弹框'''
      # time.sleep(5)
      # if(ac.isElementExist(sp.closebtn_loc)):
      #     sp.closesign()
      # time.sleep(5)
      # # '''跳转到“我的”页面'''
      # mf = MyprofilePage(self.driver)
      # mf.getmyprofile_link()
      nn = ac.get_text('主播星级').is_displayed()
      self.assertEquals(True, nn)

   '''验证主播等级项是否显示'''

   def test006_myprofile(self):
      ac = Action(self.driver)
      # sp = SignPage(self.driver)
      # '''如果有签到弹框，则关闭弹框'''
      # time.sleep(5)
      # if (ac.isElementExist(sp.closebtn_loc)):
      #    sp.closesign()
      # time.sleep(5)
      # '''跳转到“我的”页面'''
      # mf = MyprofilePage(self.driver)
      # mf.getmyprofile_link()
      ac.swipeUp()
      nn = ac.get_text('主播等级').is_displayed()
      self.assertEquals(True, nn)
