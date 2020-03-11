from PO import common
import time
#签到弹框
class SignPage(common.Action):
    #签到弹框
    signbox_loc ='com.xxxx:id/ll_sign_info'
    # 右上角关闭按钮
    closebtn_loc ='com.xxxx:id/btn_close_attendance'
    #签到天数描述
    signdaynum_loc ='com.xxxx:id/tv_sign_day_num'
    # 签到奖励展示
    signone_loc = 'com.xxxx:id/iv_attendance_bg_anim1'
    signtwo_loc = 'com.xxxx:id/iv_attendance_bg_anim2'
    signthree_loc = 'com.xxxx:id/iv_attendance_bg_anim3'
    signfour_loc = 'com.xxxx:id/iv_attendance_bg_anim4'
    signfive_loc = 'com.xxxx:id/iv_attendance_bg_anim5'
    signsix_loc = 'com.xxxx:id/iv_attendance_bg_anim6'
    signseven_loc = 'com.xxxx:id/iv_attendance_bg_anim7'
    #签到按钮
    signBtn_loc = 'com.xxxx:id/btn_attendance'
    #未绑定微信，点击签到弹绑定微信窗口
    wxbox_loc = 'com.xxxx:id/content'
    #关闭绑定微信弹框按钮
    wxclosebox_loc = 'com.xxxx:id/btnExit'
    #暂时没有抓取签到成功的元素


    '''跳转到绑定微信页面'''
    def loginByPhone_link(self):
        self.get_id(self.wxbox_loc).click()
        time.sleep(3)
    '''点击签到弹框内容'''
    def run_caseSign(self):
        self.get_id(self.signBtn_loc).click()
        time.sleep(5)
    def closesign(self):
        self.get_id(self.closebtn_loc).click()