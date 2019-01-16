# encoding=utf-8
# __author__=zhangxiang

import unittest
import requests
import json
from Logs.log import log
import getcwd
import os

path = getcwd.get_cwd()
config_path = os.path.join(path, 'Config/config.ini')


class HttpRequest(unittest.TestCase):

    def get(self, url, params=None, headers=None, files=None):
        '''封装get方法，return响应码和响应内容'''
        try:
            response = requests.get(url, params=params, headers=headers, files=files)
            log.info("请求的内容：%s" % params)
            status_code = response.status_code  # 获取返回的状态码
            log.info("获取返回的状态码:%d" % status_code)
            response_json = response.json()  # 响应内容，json类型转化成python数据类型
            log.info("响应内容：%s" % response_json)
            return status_code, response_json  # 返回响应码，响应内容
        except BaseException as e:
            log.error("请求失败！", exc_info=1)

    def post(self, url, data, headers):
        '''封装post请求，return响应码和响应内容'''
        try:
            response = requests.post(url=url, data=data, headers=headers, files=None)
            log.info("请求的url:%s" % url)
            log.info("请求的内容：%s" % data)
            status_code = response.status_code  # 获取返回的状态码
            log.info("获取返回的状态码:%d" % status_code)
            response_json = response.json()  # 响应内容，json类型转化成python数据类型
            log.info("响应内容：%s" % response_json)
            return status_code, response_json  # 返回响应码，响应内容
        except BaseException as e:
            log.error("请求失败！", exc_info=1)  # exc_info=1错误信息等级

    def post_json(self, url, data, headers):
        '''封装post方法，并用json格式传值，return响应码和响应内容'''
        try:
            data = json.dumps(data).encode('utf-8')  # python数据类型转化为json数据类型
            response = requests.post(url=url, data=data, headers=headers)
            log.info("请求的内容：%s" % data)
            status_code = response.status_code  # 获取返回的状态码
            log.info("获取返回的状态码:%d" % status_code)
            response = response.json()  # 响应内容，json类型转化成python数据类型
            log.info("响应内容：%s" % response)
            return status_code, response  # 返回响应码，响应内容
        except BaseException as e:
            log.error("请求失败！", exc_info=1)

    def getKword(self, dict1, keyObject, default=None):
        ''' 遍历嵌套字典，得到想要的value
            dict1所需遍历的字典
            keyObject 所需value的键'''
        for k, v in dict1.items():
            if k == keyObject:
                return v
            else:
                if type(v) is dict:
                    result = self.getKword(v, keyObject, default)  # 递归
                    if result is not default:
                        return result
