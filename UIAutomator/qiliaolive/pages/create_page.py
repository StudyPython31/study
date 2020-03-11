'''登陆页面'''
from common import Base_Page
import time
from appium.webdriver.common.touch_action import TouchAction

class CreateLoginPage(Base_Page.Action):

    def login_in(self, uid,pwd):
        self.find_ById("com.rare.chat:id/userId").send_keys(uid)
        self.find_ById("com.rare.chat:id/passWord").send_keys(pwd)
        self.find_ById("com.rare.chat:id/btn_login").click()
        time.sleep(3)
        action = TouchAction(self.driver)
        action.tap(x=560, y=600).perform()


    def change_env(self):
        self.find_ById('com.rare.chat:id/btnPhone2').click()
        time.sleep(3)
        el11 = self.find_element(self.driver, "id", "com.rare.chat:id/tv_agreement_ensure")
        print("1111111111111111111")
        if (el11):
            print("22222222")
            self.driver.find_element_by_id("com.rare.chat:id/tv_agreement_ensure").click()
            time.sleep(3)
            self.driver.find_element_by_id('com.rare.chat:id/btnPhone2').click()  # 登录按钮


        print("333333333333")
        # el = self.driver.find_element_by_id("com.rare.chat:id/rlContainer")
        action = TouchAction(self.driver)
        action.long_press(x=560, y=1300, duration=3000).perform()
        # changeenv = self.driver.find_element_by_id("com.rare.chat:id/dev_btn").is_displayed()
        changeenv = self.find_element(self.driver, "id", "com.rare.chat:id/dev_btn")
        # print("444444444444444444444:"+changeenv)
        if (changeenv):
            self.find_ById("com.rare.chat:id/dev_btn").click()
            print("6666666666666666")
            time.sleep(5)
            changeenv1 = self.find_element(self.driver, "id", "com.rare.chat:id/dev_btn")
            if (changeenv1):
                print("7777777777777777")
                action.tap(x=560, y=1600).perform()
                print("5555555")
            else:
                print("88888888888888")
                self.find_ById('com.rare.chat:id/btnPhone2').click()

    def get_button_text(self):
        return self.find_ById("com.rare.chat:id/tv_tab_home").text
