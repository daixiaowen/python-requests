# encoding=utf-8
# __author__=zhangxiang
from Common.jsonParse import JsonParse

ij = {"status": "0", "t": "1545449929509", "set_cache_time": "", "data": [
    {"location": "德国", "titlecont": "IP地址查询", "origip": "193.16.20.16", "origipquery": "193.16.20.16", "showlamp": "1",
     "showLikeShare": 1, "shareImage": 1, "ExtendedLocation": "", "OriginQuery": "193.16.20.16", "tplt": "ip",
     "resourceid": "6006", "fetchkey": "193.16.20.16", "appinfo": "", "role_id": 0, "disp_type": 0}]}
json = JsonParse()
result = []
re = json.get_target_value('resourceid', ij, result)
print(re)
