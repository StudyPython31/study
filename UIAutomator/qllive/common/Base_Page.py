import os
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import exceptions
from appium.webdriver.common.touch_action import TouchAction

class Action(object):
    def __init__(self, driver):
        self.driver = driver

    '''判断元素是否存在'''
    def find_element(self,driver,type,loc):
        try:
            if(type=='id'):
                WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_id(loc))
            elif(type == 'name'):
                WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_name(loc))
            elif (type == 'xpath'):
                WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_xpath(loc))
            elif (type == 'class'):
                WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_class_name(loc))
            return True

        except exceptions.TimeoutException:
            print("未找到%s"%(loc))
            return False
        except exceptions.NoSuchElementException:
            print("未找到%s" % (loc))
            return False


    def find_ById(self,loc):
        try:
            return self.driver.find_element_by_id(loc)
        except exceptions.NoSuchElementException:
            print("未找到%s" % loc)


    def find_ByXpath(self,loc):
        try:
            return self.driver.find_element_by_xpath(loc)
        except exceptions.NoSuchElementException:
            print("未找到%s" % loc)

    def find_ByIndex(self, loc, index):
        try:
            lst = self.driver.find_elements_by_id(loc)
            print(lst)
            return lst[index]
        except exceptions.NoSuchElementException:
            print("未找到%s" % loc)


    def find_ByName(self, loc):
        try:
            return self.driver.find_element_by_name(loc)
        except exceptions.NoSuchElementException:
            print("未找到%s" % loc)

    '''toast提示'''
    def get_toast(self,text):
        msg = '//*[@text=\'{}\']'.format(text)
        toast_element = WebDriverWait(self.driver, 2).until(lambda x:x.find_element_by_xpath(msg))
        return toast_element.text


    def swipe_up(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        dr = TouchAction(self.driver)
        dr.press(x=width*1/2, y=height*3/4).wait(200).move_to(x=width/2, y=height*1/4).release().perform()



    '''获取各项菜单名称'''
    def get_text(self, loc, type=None):
        if(type == 'Xpath'):
            return self.find_ByXpath(loc).text
        else:
            return self.find_ById(loc).text


    def excuteAdbShell(self, s):
        os.system(s)







