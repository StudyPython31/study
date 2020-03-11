import unittest
import time
import HTMLTestRunner


testcase_path = './testcase'
now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
report_path = './report/appium_report_'+now+'.html'


def create_suite():
    uit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_path,pattern='test_*.py')
    for test_suite in discover:
        for test_case in test_suite:
            uit.addTest(test_case)
    return uit

suite = create_suite()
fp = open(report_path,'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='测试结果',description='Appium新建笔记测试结果')
runner.run(suite)
fp.close()