# encoding=utf-8
# __author__=zhangxiang

import configparser
import pymysql
import sys
import getcwd
import os
from Logs.log import log


class Mysql():
    '''配置数据库IP，端口等信息，获取数据库连接'''
    path = getcwd.get_cwd()
    config_path = os.path.join(path, 'Config/config.ini')

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)
        self.host = self.config['db-test']['host']
        self.port = self.config['db-test']['port']
        self.user = self.config['db-test']['user']
        self.password = self.config['db-test']['password']
        self.dbName = self.config['db-test']['dbName']
        self.cursor = None
        self.conn = None

    def connectDB(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=int(self.port), user=self.user, password=self.password,
                                        database=self.dbName)
        except pymysql.Error as e:
            log.error(e)
            return False
            sys.exit()
        self.cursor = self.conn.cursor()
        return True

    # 关闭数据库
    def close(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cursor:
            self.cursor.close()
            self.conn.close()
        return True

    # 执行数据库的sq语句,主要用来做插入操作
    def execute(self, sql, params=None):
        # 连接数据库
        self.connectDB()
        try:
            if self.conn and self.cursor:
                # 正常逻辑，执行sql，提交操作
                self.cursor.execute(sql, params)
                self.conn.commit()
        except pymysql.Error as e:
            log.error("插入数据库失败! sql: %s,params: %s" % (sql, params))
            log.error(e)
            self.close()
            return False
        return True

    # 用来查询表数据
    def fetchall(self, sql, params=None):
        res = ''
        if self.connectDB():
            try:
                self.cursor.execute(sql, params)
                res = self.cursor.fetchall()
            except pymysql.Error as e:
                log.error("查询数据库失败! sql: %s,params: %s" % (sql, params))
                log.error(e)
                self.close()
            return res

    def update(self, sql, params):
        flag = False
        if self.connectDB():
            try:
                self.cursor.execute(sql, params)
                self.conn.commit()
                flag = True
            except pymysql.Error as e:
                flag = False
                log.error("更新数据库失败! sql: %s,params: %s" % (sql, params))
                self.close()
        return flag
