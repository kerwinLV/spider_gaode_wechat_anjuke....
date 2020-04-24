import json
import requests

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'Host': 'mp.weixin.qq.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1295.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat',
    'X-Requested-With': 'XMLHttpRequest',
}
biz = 'MzI4MTU2NjE3NQ=='   # 公众号id
uin = 'MTE5NTMwMzg1MQ=='   # 用户id
key = '5b5b2f3d00f78fc18740fee1dadc74e2bed3142808d3328cd9ec15' \
      '445d1c9d2378cee1143d49e4fae95a0eaf7316e1df2798d13fdc867454c98cf5dec3a50a66a03bd7dfe42eefff0e9675038e197c64'  # 是个变量
pass_ticket = '4SNkMivOQM6F5MP9wCFOxFdwgdKrKuYC7VOyvMvoI+Eqn5bt2Lijf6LRzyF1U6pi'  # 似乎用处不大

offset = 0
pagesize = 10

proxies = {
    'https': '218.86.87.171:53281'
}

url = "https://mp.weixin.qq.com/mp/profile_ext"
params = {
    "action": "getmsg",
    "__biz": biz,
    "f": "json",
    "offset": offset,
    "count": pagesize,
    "is_ok": 1,
    "scene": 124,
    "uin": uin,
    "key": key,
    "pass_ticket": pass_ticket,
    "wxtoken": "",
    "x5":0,
    # "appmsg_token": appmsg_token,
}
response = requests.get(url, params=params, headers=headers, verify=False)

print(response.text)
