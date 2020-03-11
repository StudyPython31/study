import unittest
from pages.create_page import CreateLoginPage
from common.Base_Page import Action

from appium_config import AppiumTest

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = AppiumTest().get_driver()
        self.driver1 = AppiumTest().get_driver1()

    @classmethod
    def tearDownClass(self):
        pass

    def test_login(self):
        lg = CreateLoginPage(self.driver)

        tst = Action(self.driver)

        lg.change_env()
        lg.login_in('xxxx','123456789')
        #shouye = self.driver.find_element_by_id("com.xxxx:id/ll_tab_home").is_displayed()
        self.assertEqual(tst.get_toast('用户不存在请确认'),"用户不存在请确认")
        lg.login_in('xxxx','12345678')
        self.assertEqual(lg.get_button_text(), "首页", msg="登录成功！")

    def test_login1(self):
        lg1 = CreateLoginPage(self.driver1)
        #tst1 = Action(self.driver1)
        lg1.change_env()
        lg1.login_in('xxxx', '12345678')

