import time
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'https': '218.86.87.171:53281'
}

headers = {
    # 'CSP': 'active',
    'Host': 'mp.weixin.qq.com',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://mp.weixin.qq.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1295.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat',
    'Cookie': 'rewardsn=; wxtokenkey=777; wxuin=1195303851; devicetype=Windows10x64; version=62090072; lang=zh_CN; pass_ticket=YNQmeeth4Iea7oAdusfhwaVh9qhGhAeJaKd11iGI9TeDu2+5yRl0kXl8xH5SAEAi; wap_sid2=CKvH+7kEElw1M29lZDlaZG1aSXh4TUJZOUxBVVRMdjZtSEhsYzRXaDN3enNUQ3BTSXFXVUxLekNZU2owTWxmdmVocXlVVnpVYzVJMW04bl9RWEhVMU5iclExLUZJaU1FQUFBfjD2h6n1BTgNQAE=',
    'X-Requested-With': 'XMLHttpRequest',
}
biz = 'MzA5MjUwNzQxNw=='  # 公众号id
uin = 'MTE5NTMwMzg1MQ%3D%3D'  # 用户id
key = '51e694ee2c80e741697f9927141185bf1e28c006eba8d62f305b23ba7a2d658724ce46f8f7bc37ac10e15e26eff32db54c4596c420feb6b8799648087235a7a0ff853d544a2f25797afca20d140c4dfa'
pass_ticket = 'YNQmeeth4Iea7oAdusfhwaVh9qhGhAeJaKd11iGI9TeDu2%252B5yRl0kXl8xH5SAEAi'
appmsg_token='1059_SYcAhABkqpgJ2ccIwnJRKCXCwA7bWTeRERxe2-9O3JA1Pbdx1UYlZ00mRryhXgdBfSWmjiKfzM1qvp8S'

url = "https://mp.weixin.qq.com/mp/getappmsgext"
mid="2650631926"
# idx= 1
sn="6c131572da091e5c5a914beb735f968e"
# _biz = "MzA5MjUwNzQxNw=="
params = {
    "mock": "",
    "f": "json",
    "uin": uin,
    "key": key,
    "pass_ticket": pass_ticket,
    "wxtoken": "777",
    "devicetype": "Windows&nbsp;10",
    "appmsg_token": appmsg_token,
}

t = int(time.time())
# 以下参数先使用复制的，后续再说获取
appmsg_type = "9"
msg_title = "%E7%9B%9B%E5%A4%A7%E6%AC%A2%E5%BA%864.25%E8%93%9D%E5%B8%A6%E4%B8%8A%E6%B5%B7%E4%BA%94%E5%91%A8%E5%B9%B4%EF%BC%81%E9%A6%96%E5%9C%BA%E2%80%9C%E4%BA%91%E8%AE%B2%E5%BA%A7%E2%80%9D%E5%85%A8%E9%9D%A2%E8%A7%A3%E6%9E%90%E6%89%80%E6%9C%89%E8%AF%BE%E7%A8%8B%EF%BC%8C%E8%A7%A3%E6%83%91%E7%AD%94%E7%96%91"
req_id = "30117ipWyMxiRW4qWYsM6Dbs"
comment_id = "0"
# mid = "2247483655"
# sn = "9906c92e7d13c2f3451f06f4ab4bafda"
# idx = "1"
scene = "38"
appmsg_like_type = "2"

data = {
    # "r": "0.48046619608066976",
    "__biz": biz,  # 公众号id
    "appmsg_type": appmsg_type,  # 信息类型
    "mid": mid,  # 一个参数
    "sn": sn,  # 一个参数
    "idx": "1",
    "scene": scene,  # 一个数字
    "title": msg_title,  # 文章标题
    "comment_id": comment_id,  # 评论id
    "ct": t,  # 时间戳
    "pass_ticket": pass_ticket,  # 一个参数
    "req_id": req_id,  # 一个参数
    "abtest_cookie": "",
    "devicetype": "Windows+10",
    "version": "62060728",
    "is_need_ticket": "0",  # 后面一些标识直接写死
    "is_need_ad": "0",
    "is_need_reward": "1",
    "both_ad": "0",
    "send_time": "",
    "msg_daily_idx": "1",
    "is_original": "0",
    "is_only_read": "1",
    "is_temp_url": "0",
    "item_show_type": "0",
    "tmp_version": "1",
    "more_read_type": "0",
    "appmsg_like_type": "2"
}

# params = {
#         "mock": "",
#         "f": "json",
#         "__biz": _biz,
#         "uin":uin,
#         "key": key,
#         "pass_ticket": pass_ticket,
#         "appmsg_token": appmsg_token,
#         "devicetype": "Windows&nbsp;10",
#         "wxtoken": "777",
#         "x5":0,
#         "clientversion":"62090072",
#     }
# import urllib.parse
# title1 = urllib.parse.quote(title)
# data = {
#     # "r": "0.06183692833270871",
#     "__biz": _biz,
#     "appmsg_type": "9",  # 复制下来的值，会被覆盖掉
#     "mid": mid,
#     "sn": sn,
#     "idx": idx,
#     "scene": "38",
#     "title": title1,  # 为空，后面覆盖
#     "comment_id": "0",
#     "ct": t,
#     "pass_ticket": pass_ticket,  # 也可以写死
#     "req_id": req_id,  # 一个参数
#     "abtest_cookie": "",
#     "devicetype": "Windows+10",
#     "version": "62080085",
#     "is_need_ticket": "0",
#     "is_need_ad": "0",
#     "is_need_reward": "1",
#     "both_ad": "0",
#     "send_time": "",
#     "msg_daily_idx": "1",
#     "is_original": "0",
#     "is_only_read": "1",
#     "is_temp_url": "0",
#     "item_show_type": "0",
#     "tmp_version": "1",
#     "more_read_type": "0",
#     "appmsg_like_type": "2"
# }

response = requests.post(url, params=params, data=data, headers=headers, verify=False)

print(response.text)