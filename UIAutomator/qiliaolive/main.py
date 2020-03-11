import unittest
import HTMLTestRunner
import time


now = time.strftime('%Y_%m_%d %H_%M_%S', time.localtime())

testcase_path = './tescases'
report_path = './report/appium'+ now +'_report.html'


def create_suite():
    uni = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern='test*.py')
    for test_suite in discover:
        for test_case in test_suite:
            uni.addTest(test_case)
    return uni


suite = create_suite()
fp = open(report_path, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title='测试报告', description='appium测试结果')
runner.run(suite)
fp.close()
