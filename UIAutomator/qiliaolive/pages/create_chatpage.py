'''语聊'''
from common import Base_Page
import time
from appium.webdriver.common.touch_action import TouchAction
from common.conSQL import MysqlConnect


class CreateChatPage(Base_Page.Action):

    def searchuid(self,searchtext):
        self.find_ById('com.rare.chat:id/ll_voice_chat').click()  #跳到语聊页面

        self.find_ById('com.rare.chat:id/ivSearch').click()
        self.excuteAdbShell('adb shell ime set io.appium.android.ime/.UnicodeIME')
        self.find_ById('com.rare.chat:id/et_chat_search').click()
        self.find_ById('com.rare.chat:id/et_chat_search').send_keys(searchtext)
        self.driver.keyevent(4)
        #self.find_ById('com.rare.chat:id/et_chat_search').click()

        self.driver.keyevent(84)
        # self.driver.press_keycode(84) #模拟键盘搜索键
        time.sleep(2)
        # self.find_ByIndex('com.rare.chat:id/rv_search_result', 0).click()

    def selectrslt(self, index):
        self.find_ByIndex('com.rare.chat:id/rv_search_result', index).click()

    def sendmsg(self,msgs):
        self.find_ById('com.rare.chat:id/tvPrivateChat').click()
        self.find_ById('com.rare.chat:id/etMsgEdit').send_keys(msgs)
        self.find_ById('com.rare.chat:id/btSend').click()
        self.driver.keyevent(4)  # 模拟按下手机键盘的返回,收起键盘


    def getmsg(self,index):
        self.find_ById('com.rare.chat:id/ll_message').click()# 跳到消息页面
        msgindex = self.find_ByIndex('com.rare.chat:id/tv_private_chat_name', index)
        return msgindex.text   #私信内容（文本内容）

    def selectsearchhistory(self, tag):
        self.find_ById('com.rare.chat:id/ll_voice_chat').click()  # 跳到语聊页面
        self.find_ById('com.rare.chat:id/ivSearch').click()
        self.find_ByXpath("//*[@text=\'"+tag+"\']").click()








