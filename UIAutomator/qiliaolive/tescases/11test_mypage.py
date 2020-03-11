import unittest
from pages.create_mypage import CreateMyPage
from common.Base_Page import Action
from common.conSQL import MysqlConnect

from appium_config import AppiumTest

class TestMyPage(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = AppiumTest().get_driver()

    @classmethod
    def tearDownClass(self):
        pass

    def test01_mypagemenu(self):
        mp1 = CreateMyPage(self.driver)
        mp = Action(self.driver)
        sqll = MysqlConnect()
        mp1.firstTimeToMy()
        nickname = sqll.exec_sql_select('SELECT nickname FROM `qy_ql_user` where uid=8324162')
        self.assertEqual(mp.get_text('com.rare.chat:id/nameTv'), nickname[0], msg="昵称显示正确！")
        self.assertEqual(mp.get_text('com.rare.chat:id/noTv'), "ID 8324162", msg="uid显示正确！")
        self.assertEqual(mp.get_text('com.rare.chat:id/fansNumLabel'), "粉丝",msg='粉丝菜单显示正确')
        fanscount =sqll.exec_sql_select('SELECT fans FROM `qy_ql_user` where uid=8324162')
        self.assertAlmostEqual(mp.get_text('com.rare.chat:id/fansNumTv'), str(fanscount[0]),  msg='粉丝数正确')
        self.assertEqual(mp.get_text('com.rare.chat:id/tvMinePhoto'), "我的相册", msg='我的相册菜单显示正确')
        self.assertEqual(mp.get_text('com.rare.chat:id/tvMineVideos'), "我的视频", msg='我的视频属性显示正确')
        self.assertEqual(mp.get_text('com.rare.chat:id/tvMineCircle'), "我的圈子", msg='我的圈子属性显示正确')
        self.assertEqual(mp.get_text("//*[@text='我的钱包']", 'Xpath'), "我的钱包", msg='我的钱包菜单显示正确')
        coin = sqll.exec_sql_select('SELECT coin_remain FROM `qy_ql_capital` where uid=8324162')
        self.assertAlmostEqual(float(mp.get_text('com.rare.chat:id/coinTv')), coin[0], places=1)
        self.assertEqual(mp.get_text('//*[@text="我的会员"]', 'Xpath'), "我的会员", msg='我的会员菜单显示正确')
        self.assertEqual(mp.get_text('//*[@text="尊享特权"]', 'Xpath'), "尊享特权", msg='我的会员菜单显示正确')
        self.assertEqual(mp.get_text('//*[@text="兑换钻石"]', 'Xpath'), "兑换钻石", msg='兑换钻石菜单显示正确')
        self.assertEqual(mp.get_text('//*[@text="申请入驻"]', 'Xpath'), "申请入驻", msg='申请入驻菜单显示正确')
        self.assertEqual(mp.get_text('//*[@text="主播管理"]', 'Xpath'), "主播管理", msg='主播管理菜单显示正确')
        self.assertEqual(mp.get_text('//*[@text="邀请好友"]', 'Xpath'), "邀请好友", msg='好友邀请菜单显示正确')
        self.assertEqual(mp.get_text('//*[@text="得百万钻石奖励"]', 'Xpath'), "得百万钻石奖励", msg='好友邀请菜单显示正确')
        mp.swipe_up()
        self.assertEqual(mp.get_text("com.rare.chat:id/mineCustomService"), "联系客服", msg='联系客服菜单显示正确')
        self.assertEqual(mp.get_text("com.rare.chat:id/mineSeeting"), "设置", msg='设置菜单显示正确')


    def test02_mypagemenu(self):
        mp1 = CreateMyPage(self.driver)
        mp = Action(self.driver)
        mp1.updateNickName('不超过7个字')
        mp1.updateSign('不超过50个字')
        mp1.select_tag('性感','浪漫')
        mp1.saveinfo()
        mp.find_ById('com.rare.chat:id/ctlMineInfo').click()
        self.assertEqual(mp.get_text('com.rare.chat:id/nameTv'), '不超过7个字', msg='昵称修改成功')
        self.assertEqual(mp.get_text('com.rare.chat:id/signTv'), '不超过50个字', msg='昵称修改成功')
        self.assertEqual(mp.get_text('com.rare.chat:id/tv_tag1'),'性感')
        self.assertEqual(mp.get_text('com.rare.chat:id/tv_tag2'), '浪漫')


