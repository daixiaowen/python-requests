# encoding=utf-8
# __author__=zhangxiang

import unittest
from Logs.log import log
from Common.configParse import ConfigParse
from Common.request import HttpRequest


class login(unittest.TestCase):
    def test_AppLogin(self):
        '''app登录'''
        case_name = 'app登录'
        log.info("执行测试用例：%s" % case_name)
        try:
            login = HttpRequest()
            cfg = ConfigParse()
            url = 'http://' + cfg.getUrl('url', 'baseUrl', url='/user-api/v1/login')
            print(url)
            data = {"mobile": "13668277212", "login_type": 1, "user_pass": "aw/eAJHzBuQ8hnB/GN7vmg=="}
            headers = {
                'appid': 'sdwe12e12e2e1212',
                'phonetype': 'iPhone 6s',
                'ostype': '2',
                'refersource': 'AppStore',
                'os': 'ios 12.1',
                'devicecode': '008F504E-A670-41B4-ADD3-403EC6981E26',
                'versionname': '3.0.0',
                'versioncode': '20',
                'User-Agent': '%E6%95%99%E8%82%B2%E5%AE%B6%E7%A4%BE%E5%8C%BA/20 CFNetwork/975.0.3 Darwin/18.2.0',
                'Cookie': 'PHPSESSID=2buijfqibnocr73ael86tom4h4',
                'Content-Type': 'application/json'
            }
            response = login.post_json(url, data, headers)
            print(response)
            test = self.assertEqual(response.status, 200)
            if test:
                log.info("测试通过")
        except BaseException as e:
            log.error("测试用例执行出错: %s,错误信息为：%s" % (case_name, e), exc_info=1)
            raise


if __name__ == '__main__':
    login.test_AppLogin()
