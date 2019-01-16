# encoding=utf-8
# __author__=zhangxiang

from Common.configParse import ConfigParse
import requests

c = ConfigParse()
url = 'http://' + c.getUrl('url', 'baseUrl', url='/user-api/v1/login')
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
response = requests.post(url, data=data, headers=headers)
print(response.status_code)
