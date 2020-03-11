'''元素定位方法封装,https://www.cnblogs.com/yoyoketang/p/7810507.html'''
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Action(object):
     def __init__(self,se_driver):
         self.driver = se_driver
     def get_id(self,loc): #通过ID定位
         try:
             return self.driver.find_element_by_id(loc)
         except Exception as e:
             print('未找到%s'%(self,loc))

     def get_text(self,loc): #通过text定位
         try:
             return self.driver.find_element_by_android_uiautomator('text(\"'+loc+'\")')
         except Exception as e:
             print('未找到%s'%(self,loc))

     #判断元素是否存在
     def isElementExist(self,id):
         try:
             self.get_id(id)
             return True
         except:
             return False

     '''验证toast，存在返回True,不存在返回False'''
     def getToastExit(self,text,timeout=30,poll_frequency=0.5):
         '''is toast exist, return True or False
             :Agrs:
              - driver - 传driver
              - text   - 页面上看到的文本内容
              - timeout - 最大超时时间，默认30s
              - poll_frequency  - 间隔查询时间，默认0.5s查询一次
             :Usage:
              is_toast_exist(driver, "看到的内容")
             '''
         try:
            toast_loc = ('xpath','.//*[contains(@text,"%s")]' % text)
            print(toast_loc)
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.presence_of_element_located(toast_loc))
            return True
         except:
             return False

     '''向上滑动屏幕'''
     def swipeUp(self,t=500,n=1):
         size = self.driver.get_window_size()
         x1 = size['width'] * 0.5
         y1 = size['height'] * 0.75
         y2 = size['height'] * 0.25
         for i in range(n):
             self.driver.swipe(x1,y1,x1,y2,t)

