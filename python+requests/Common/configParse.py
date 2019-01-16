# encoding=utf-8
# __author__=zhangxiang

import configparser
from Logs.log import log
import getcwd
import os


class ConfigParse:
    '''
    解析ini配置文件
    '''
    path = getcwd.get_cwd()
    config_path = os.path.join(path, 'Config/config.ini')

    def __init__(self):
        self.config = configparser.ConfigParser()  # ConfigParser对象实例
        self.config.read(self.config_path)  # 一启动就读取配置文件

    # 添加指定的节
    def add_section(self, section):
        sections = self.config.sections()
        if section in sections:
            return
        else:
            self.config.add_section(section)

    # 移除指定的节
    def remove_section(self, section):
        return self.config.remove_section(section)

    def get(self, section, option):
        return self.config.get(section, option)

    def set(self, section, option, value):
        if self.config.has_section(section):
            self.config.set(section, option, value)

    # 移除指定节内的指定选项
    def remove_option(self, section, option):
        if self.config.has_section(section):
            return self.config.remove_option(section, option)
        return False

    # 返回节内的键值列表
    def items(self, section):
        return self.config.items(section)

    # 返回所有节的列表
    def sections(self):
        return self.config.sections()

    # 返回节内的键列表
    def options(self, section):
        return self.config.options(section)

    # 获取所有收件人邮箱
    def get_Recievers(self, receivers):
        sum = 0
        recieverList = []
        for i in receivers:
            if sum < len(receivers):
                emails = self.get('receivers', i)
                list.append([emails])
                sum += 1
        return recieverList

    # 获取url
    def getUrl(self, section, option, url=None):
        for sec in self.sections():
            if sec == 'url':
                config_url = self.config.get(sec, 'baseUrl')
                if url != None:
                    curryUrl = config_url + url
                    log.info("请求的url：%s" % curryUrl)
                    return curryUrl
                    print(curryUrl)
                else:
                    return config_url
                    print(config_url)
            else:
                return self.config.get(section, option)
