# encoding=utf-8
# __author__=zhangxiang

import logging
import time
import os
import getcwd


def get_log(loggerName):
    # 创建一个logger
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.INFO)

    # 设置日志存放路径，日志文件名
    # 获取本地时间，转换为设置的格式
    nowTime = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    # 设置所有日志和错误日志的存放路径
    path = getcwd.get_cwd()
    # 通过getcwd.py文件的绝对路径来拼接日志存放路径
    allLogPath = os.path.join(path, 'Logs/All_Logs/')
    errorLogPath = os.path.join(path, 'Logs/Error_Logs/')
    # 设置日志文件名
    allLogName = allLogPath + nowTime + '.log'
    errorLogName = errorLogPath + nowTime + '.log'

    # 创建handler
    # 创建一个handler写入所有日志
    allHandler = logging.FileHandler(allLogName)
    allHandler.setLevel(logging.INFO)
    # 创建一个handler写入错误日志
    errorHandler = logging.FileHandler(errorLogName)
    errorHandler.setLevel(logging.ERROR)
    # 创建一个handler输出到控制台
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)

    # 定义日志输出格式
    # 以时间-日志器名称-日志级别-日志内容的形式展示
    allLogFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 以时间-日志器名称-日志级别-文件名-函数行号-错误内容
    errorLogFormatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)s - %(message)s')
    # 将定义好的输出形式添加到handler
    allHandler.setFormatter(allLogFormatter)
    consoleHandler.setFormatter(allLogFormatter)
    errorHandler.setFormatter(errorLogFormatter)

    # 给logger添加handler
    logger.addHandler(allHandler)
    logger.addHandler(errorHandler)
    logger.addHandler(consoleHandler)
    return logger


log = get_log("test")
