# encoding=utf-8
# __author__=zhangxiang

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
import getcwd
import os
from Logs.log import log
import time
from Common.configParse import ConfigParse

nowDate = time.strftime('%Y%m%d', time.localtime(time.time()))  # 获取本地时间 转换成日期
myMail = ConfigParse()
email = myMail.get('sender', 'email')  # 发件人邮箱账号
password = myMail.get('sender', 'password')  # 发件人邮箱授权码
username = myMail.get('sender', 'username')  # 发件人姓名
recUserName = myMail.get('receivers','recUserName')  # 收件人姓名
recieveMail = myMail.get('receivers','recieveMail')  # 收件人邮箱
print(recieveMail)
path = getcwd.get_cwd()
file = os.path.join(path, 'report/教育家社区APP接口自动化测试报告.html')


def mail():
    try:
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = formataddr([username, email])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        log.info('发件人姓名：%s' % username)
        log.info('发件人邮箱：%s' % email)
        message['To'] = ';'.join(recUserName)  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        log.info('收件人邮箱：' +recieveMail)
        message['Subject'] = nowDate + "教育家社区APP接口自动化测试报告.html"  # 邮件的主题，也可以说是标题

        # 邮件正文内容
        message.attach(MIMEText('附件为教育家社区APP接口自动化测试报告.html', 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
        log.info('读取附件')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1.add_header("Content-Disposition", "attachment", filename=("gbk", "", "教育家社区APP接口自动化测试报告.html"))
        # 附件名称非中文时的写法
        # att["Content-Disposition"] = 'attachment; filename="test.html")'
        message.attach(att1)
        log.info('添加附件')

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        log.info('连接QQ邮箱smtp服务')
        server.login(email, password)  # 括号中对应的是发件人邮箱账号、授权验证码
        log.info('连接成功')
        server.sendmail(email, recieveMail, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        log.info("邮件发送成功")
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        log.error("邮件发送失败", exc_info=1)
