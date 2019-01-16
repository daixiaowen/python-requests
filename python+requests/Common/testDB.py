# encoding=utf-8
# __author__=zhangxiang
from Common.mysql import Mysql

mysql = Mysql()
mysql.connectDB()
sql = "select * from publicdata.users where mobile = '13668277212'"
re = mysql.fetchall(sql)
print(re)
