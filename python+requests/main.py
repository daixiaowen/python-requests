# encoding=utf-8
# __author__=zhangxiang

import TestCase.test_AppLogin
import getcwd
import Common.sendEmail
import HTMLTestRunnerCN
import unittest

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCase.test_AppLogin.login('test_AppLogin'))
    report_path = getcwd.get_report("report\\",reportName='教育家社区APP接口自动化测试报告.html')
    fp = open(report_path, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestReportCN(
        stream=fp,
        title='教育家社区APP接口自动化测试报告',
        description='报告中描述部分',
        tester='张翔'
    )
    runner.run(suite)
    fp.close()
    Common.sendEmail.mail()
