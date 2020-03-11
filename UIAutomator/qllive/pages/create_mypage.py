'''我的页面'''
from common import Base_Page
import time
from appium.webdriver.common.touch_action import TouchAction
from common.conSQL import MysqlConnect

class CreateMyPage(Base_Page.Action):

    def firstTimeToMy(self):
        self.find_ById('com.xxxx:id/rl_me').click()
        ta = self.find_element(self.driver, 'id', 'com.xxxx:id/iv_dialog_img')  #是否有邀请页面弹窗
        if(ta):
            TouchAction(self.driver).tap(x=100, y=400).perform()  #点击空白区域，隐藏弹窗

    '''编辑资料---修改昵称'''
    def updateNickName(self, nickname):
        self.find_ById('com.xxxx:id/ctlMineInfo').click() #点击我的信息跳转到编辑资料页面
        '''修改头像手动回归,选择地区、生日手动回归'''
        #修改昵称
        self.find_ById('com.xxxx:id/nameTv').click()
        self.find_ById('com.xxxx:id/et_input').clear()
        self.find_ById('com.xxxx:id/et_input').send_keys(nickname)
        self.find_ById('com.xxxx:id/tv_title_other').click()
        time.sleep(1)

    def updateSign(self, sign):
        self.find_ById('com.xxxx:id/signTv').click()
        sign1 = self.find_ById('com.xxxx:id/et_input')
        sign1.clear()
        sign1.send_keys(sign)
        self.find_ById('com.xxxx:id/tv_title_other').click()


    def get_sex(self):
        sex = MysqlConnect().exec_sql_select('SELECT xxx FROM `xxx` where uid=xxx')[0]
        sex1 = '女'
        if(sxx == 1):
            xx = "男"
        return sex1

    def select_tag(self, tag, tag1=None):
        addtag = self.find_ById('com.xxxx:id/tv_tag_add')
        addtag.click()
        self.find_ByXpath("//*[@text=\'"+tag+"\']").click()
        if(tag1 is not None):
            self.find_ByXpath("//*[@text=\'"+tag1+"\']").click()
        self.find_ById('com.xxxx:id/tv_title_other').click()


    def saveinfo(self):
        self.find_ById('com.xxxx:id/saveBtn').click()


















