import unittest
from appium_config import AppiumTest
from pages.create_chatpage import CreateChatPage

class TestChatpage(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # self.driver = AppiumTest().get_driver()
        self.driver1 = AppiumTest().get_driver1()

    @classmethod
    def tearDown(self):
        pass


    def test_sendmsg(self):
        # ccp = CreateChatPage(self.driver)
        ccp1 = CreateChatPage(self.driver1)
        ccp1.selectsearchhistory('8324162')
        #ccp1.searchuid('8324162')
        ccp1.selectrslt(0)

        second = ccp1.sendmsg("哈哈哈")
        '''
        first = ccp.getmsg(0)
        self.assertEqual(first, second)
        '''






