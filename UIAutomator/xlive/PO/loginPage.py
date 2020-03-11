'''登陆页面的元素'''
from PO import common
import time
class CreatPage(common.Action):
    loginByPhone_loc ='com.xxxx:id/btnPhone'
    username_loc ='com.xxxx:id/userId'
    password_loc ='com.xxxx:id/passWord'
    loginBtn_loc ='com.xxxx:id/btn_login'

    '''选择手机账号登陆按钮'''
    def loginByPhone_link(self):
        self.get_id(self.loginByPhone_loc).click()
        time.sleep(3)

    def run_caseLogin(self, userid, password):
        self.get_id(self.username_loc).send_keys(userid)
        self.get_id(self.password_loc).send_keys(password)
        self.get_id(self.loginBtn_loc).click()
