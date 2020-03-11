from PO import common
import time
#签到弹框
class MyprofilePage(common.Action):

    myprofilebtn_loc = 'com.xxxx:id/layout_people'
    #''com.xxxx:id/iv_tab_me'
    nickname_loc = 'com.xxxx:id/nickname'
    userid_loc = 'com.xxxx:id/tv_user_id'
    # 关注数量
    followcount_loc = 'com.xxxx:id/tv_user_id'
    # 粉丝人数
    fanscount_loc = 'com.xxxx:id/strFans_size'



    head_loc = 'com.xxxx:id/ll_head_view' #点击进入个人主页
    '''跳转按钮'''
    editbtn_loc = 'com.xxxx:id/btn_edit'
    nobilitybtn_loc = 'com.xxxx:id/btn_nobility'
    grandrank_loc = 'com.xxxx:id/ll_grading_rank'
    coinhost_loc = 'com.xxxx:id/btn_coin_hostroy'
    charge_loc = 'com.xxxx:id/ll_charge'
    profit_loc = 'com.xxxx:id/ll_profit'
    phone_loc = 'com.xxxx:id/btn_phone'
    level_loc = 'com.xxxx:id/btn_level'
    starlevel_loc = 'com.xxxx:id/btn_anchor_star_level'
    anchorlevel_loc = 'com.xxxx:id/btn_anchor_level'
    Authentication_loc = 'com.xxxx:id/btnAuthentication'
    family_loc = 'com.xxxx:id/btnMyFamily'
    familystar_loc = 'com.xxxx:id/btnFamilyStarLevel'
    livemgr_loc = 'com.xxxx:id/btn_live_mgr'




    def getmyprofile_link(self):
        self.get_id(self.myprofilebtn_loc).click()
        time.sleep(3)


