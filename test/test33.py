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
    'Cookie': 'rewardsn=; wxtokenkey=777; wxuin=1195303851; devicetype=Windows10; version=62080085; lang=zh_CN; pass_ticket=4SNkMivOQM6F5MP9wCFOxFdwgdKrKuYC7VOyvMvoI+Eqn5bt2Lijf6LRzyF1U6pi; wap_sid2=CKvH+7kEElxkODJCRVNqMWYyOExTb3VMaG5ORVRlOGF6Rlk3UWt6SVRPYm42ZndWODdvODQzZUVSbjhFbmRja29LeTdGVWliZHZ0Yl9udzdHWWdJYVhMNDNfOHNLaUlFQUFBfjC56oP1BTgNQAE=',
    'X-Requested-With': 'XMLHttpRequest',
}
biz = 'MzI4MTU2NjE3NQ=='  # 公众号id
uin = 'MTE5NTMwMzg1MQ%3D%3D'  # 用户id
key = '1cbf4f3ad1e1f448048255ec2629af1846823aded2fede83c4ff99e59de1364b86577468bc93be0bffa4ae70110064485516cb014b167fbcc49b422b43729b9b944a9b88c015ea995a366575155d56d7'
pass_ticket = '4SNkMivOQM6F5MP9wCFOxFdwgdKrKuYC7VOyvMvoI%252BEqn5bt2Lijf6LRzyF1U6pi'
appmsg_token='1058_Tka4t%2FxgjWflPwwLQqUpaIKXXk9r1ZjePeTDtG97USA8W6fjY_tAugduvkanJ1a4jrvOHV03uNrMv8Bz'

url = "https://mp.weixin.qq.com/mp/getappmsgext"

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
msg_title = "%E6%88%91%E4%BB%AC%E9%83%BD%E6%98%AF%E5%B0%8F%E8%AF%97%E4%BA%BA"
req_id = "2309BCYQOyicfhuFlCQHLb2n"
comment_id = "0"
mid = "2247483655"
sn = "9906c92e7d13c2f3451f06f4ab4bafda"
idx = "1"
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

response = requests.post(url, params=params, data=data, headers=headers, verify=False)

print(response.text)