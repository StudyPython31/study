'''直播按钮开播'''
from PO import common
import time
class LiveStartPage(common.Action):
    livebtn_loc = 'com.qixingzhibo.living:id/img_live' #直播按钮
    liveopen_loc = 'com.qixingzhibo.living:id/iv_start_live' #公开直播按钮
    liveprivate_loc = 'com.qixingzhibo.living:id/iv_private_space' #私密直播按钮
    '''开始直播页面'''
    startlivebtn_loc = 'com.qixingzhibo.living:id/startLive' #开始直播
    pwd_loc = 'com.qixingzhibo.living:id/tv_import_password' #私密直播密码
    comfirmbtn_loc = 'com.qixingzhibo.living:id/btn_affirm_password' #私密直播确认按钮
    closelive_loc = 'com.qixingzhibo.living:id/ivClose' #关闭直播间
    closecomfirm_loc = 'com.qixingzhibo.living:id/tvSure'#关闭直播间弹框确认按钮
    livestopbtn_loc = 'com.qixingzhibo.living:id/btnConfirm' #直播结束页面

    def startopenlive(self):
        self.get_id(self.livebtn_loc).click()
        self.get_id(self.liveopen_loc).click()
        self.get_id(self.startlivebtn_loc).click()

    def startprivatelive(self,pwd):
        self.get_id(self.livebtn_loc).click()
        self.get_id(self.liveprivate_loc).click()
        self.get_id(self.pwd_loc).send_keys(pwd)
        self.get_id(self.comfirmbtn_loc).click()
        self.get_id(self.startlivebtn_loc).click()

    def closeopenliveroom(self):
        self.get_id(self.closelive_loc).click()
        self.get_id(self.closecomfirm_loc).click()
        self.get_id(self.livestopbtn_loc).click()






