# encoding=utf-8
# __author__=zhangxiang


'''封装钉钉群发消息'''
import requests, json
import datetime

#
# time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

Dingtalk_access_token = "https://oapi.dingtalk.com/robot/send?access_token=752bdd570ad6abd8c0df79cf5af705231bdd9e1ff31d75924c1523ef775fc2f3"
header = {
    "Content-Type": "application/json",
    "Charset": "UTF-8"
}


def send_text(content):
    # 钉钉配置
    url = Dingtalk_access_token
    data = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "at": {
            "isAtAll": True
        }
    }

    response = requests.post(url, data=json.dumps(data), headers=header)
    if response.status_code == 200:
        return True
    else:
        return False


def send_link(picUrl, title, text):
    url = Dingtalk_access_token
    data = {
        "msgtype": "link",
        "link": {
            "messageUrl": url,
            "picUrl": picUrl,
            "title": title,
            "text": text,
        },
        "at": {
            "isAtAll": True
        }
    }
    response = requests.post(url, data=json.dumps(data), headers=header)
    if response.status_code == 200:
        return response
    else:
        return False


if __name__ == "__main__":
    # send_text("记得打卡哦")
    send_link(r"https://www.pgyer.com/TgY7",
              "{} Android包".format(now), "请扫描二维码下载使用！")
