# -*- coding: utf-8 -*-
import time
import re
import random
import json

import requests
import urllib3
import pymysql
from DBUtils.PooledDB import PooledDB

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


pool = PooledDB(pymysql, 10,
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='ip_proxy_pool',
                charset='utf8'
                )
# 西安
# sheetName = "郑州市教工幼儿园"

"""常需要修改"""
# Cookie = "noticeLoginFlag=1; pgv_pvid=7256621674; pgv_pvi=5590167552;" \
#          " RK=RSqBVIDS96; ptcz=febb259247b2456cc3884c97bde35ebc5d7a917e" \
#          "fd2725129180d5002839c0b5; ua_id=WJh9AWtKKFr1RXtiAAAAAA6vPufRh" \
#          "-Dhv6aYtSdPOWU=; pac_uid=0_fdd05521b5da8; noticeLoginFlag=1; " \
#          "bizuin=2399650834; mm_lang=zh_CN; rand_info=CAESICnk6yZEL5h+s" \
#          "UKaSfJuJiwsuCcVgfIf1Kv5bvTd+mCv; slave_bizuin=2399650834; data" \
#          "_bizuin=2399650834; data_ticket=jIkIDPatGtHSrCJeC7RklTbPSS2AxKJ" \
#          "2OHXJKsWrI10YNeWhsl2AYRTOzMBH8UAD; slave_sid=Rk1FTnJ6alZKMW9VNnVC" \
#          "T3BBREtqUVU3bkdaQTk2N0hRdUdlb1V0VTU3UGVvcWxqbGxyQ3M4ODFxb2xBT3dWN" \
#          "XFjZWh2dlpHMTNpQkMyQWdBS09mZFhVNkJuT3ZrSVB6clRyYWdwamZBemM4cF92cE" \
#          "5vb2ZaUG9wUnM0NmxxQVhxd1UyQ0o0Y2ZDY3k0eWUz; slave_user=gh_5235702" \
#          "21b57; xid=e95f4a1eab3ca0a47404732400a0ff1d; openid2ticket_oEsQHj1" \
#          "fpKrIcI9zGY1YXYPExUTk=R8cDqGBXaBpNHyrnklDokwYxvndCTZ4ekQVn7DGUVHU=;" \
#          " rewardsn=; wxtokenkey=777"
# token = "1544570018"
_biz = "MzA5MjUwNzQxNw=="
"""常需要修改"""
get_cookie = "rewardsn=; wxtokenkey=777; wxuin=1195303851; devicetype=android-29; version=27000c50; lang=zh_CN; pass_ticket=PTfr/ubN/sARjW1l8QLf3LmnOFGbc3VNZ9oWERrVbdLPYx5uVWjUq5G2IbynL1I; wap_sid2=CKvH+7kEElxzZGc4RUNvUFIyM1BEenR6OWxsNGhzZWNucHZZQnF0WGkwVURiS21RUU1ZeFhId0laeGNBTFYtNHlVcDgxMmp6VFFEb2VXQ2F4QXdJLS00REhFa2tReU1FQUFBfjDQ6an1BTgNQJVO"
post_cookie= "rewardsn=; wxtokenkey=777; wxuin=1195303851; devicetype=Windows10x64; version=62090072; lang=zh_CN; pass_ticket=PTfr/ubN/sARjW1l8QLf3LmnOFGbc3V+NZ9oWERrVbdLPYx5uVWjUq5G2IbynL1I; wap_sid2=CKvH+7kEElxqdjdQdDZFSVNRbXR5bllOTHNuUGl6M04wTUhjZlFHVUt6QVZLYnd4d0RaYWNweGVmWmY4SDE4S3c4UE9ON1Q4SnB3Z0U2ejVqSGFud0RSWDNILTM1Q01FQUFBfjCG66n1BTgNQAE="
# pass_ticket = "4KzFV%252BkaUHM%252BatRt91i%252FshNERUQyQ0EOwFbc9%252FOe4gv6RiV6%252FJ293IIDnggg1QzC"
get_pass_ticket = "PTfr/ubN/sARjW1l8QLf3LmnOFGbc3V+NZ9oWERrVbdLPYx5uVWjUq5G2IbynL1I"
post_pass_ticket = "PTfr%252FubN%252FsARjW1l8QLf3LmnOFGbc3V%252BNZ9oWERrVbdLPYx5uVWjUq5G2IbynL1I"
# appmsg_token = "999_SVODv6i0%2FSNhK8CliOHzbKOydLO3IWXbnYfk2aiso-KkGL9w9a38IZlJCyOAXYyNJXdGn3zR5PTNWklR"
get_appmsg_token = "1059_wsDf5PaELQ5I7iv2v-mxJc5PwicdMKeL5efWWQ~~"
post_appmsg_token = "1059_bcoImEGbnwlfQRj1wnJRKCXCwA7bWTeRERxe2_PkBv14gwYWuspWCLUbw1dLO8PUZEySu4b9lWXbJc-o"

req_id = "3013rxv9YmMFLSjIXIzEHxVZ"

get_key = "8c93de3f00d4c98dd133dd8758e28f477841a6b978e200cbf608029a5a2edb7003ba5a50ac7cecd86afbc3d7fe472249b6906fbc820f9f9307fcfb6bae3a60318cbafe2f8f7765237712e3ddab8d0145"
post_key= "1cbf4f3ad1e1f4482569a48ad56b68d2e044e7ad7578bd5a516d6d5624842c5ae48ee5119f00a8f2103058e65f0e21988a3d7d37f2eb5d51634c0c0c13532f869f672313cddcd989513583689187bcf5"

uin = "MTE5NTMwMzg1MQ%3D%3D"
# 使用Cookie，跳过登陆操作
# header = {
#     "Cookie": pcCookie,
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1301.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat",
# }


# 目标url
# url = "https://mp.weixin.qq.com/cgi-bin/appmsg"
url = "https://mp.weixin.qq.com/mp/profile_ext"
#https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzA5MjUwNzQxNw==&f=json&offset=190&count=10&is_ok=1&scene=124&uin=MTE5NTMwMzg1MQ%3D%3D&key=9de0b3367445c6d8bf7eb5527fcc3643c43fa07e5f53cfe6f10056aae2a4df9570f58ba0ccda9b9a0c8a024e0e09ca501b3ca2b93ccbfad73bb58ee6b3681a6d3516c75b4204f64407fb35cb327fb0d3&pass_ticket=YNQmeeth4Iea7oAdusfhwaVh9qhGhAeJaKd11iGI9TeDu2%2B5yRl0kXl8xH5SAEAi&wxtoken=&appmsg_token=1058_1JhJ%252BQQcAp0%252B38WA74d7Tk5UYPPCjk3YfdRGVA~~&x5=0&f=json

# Cookie = "noticeLoginFlag=1; remember_acct=sisecx; pgv_pvi=7219193856; RK=G5400dGxMt; ptcz=557d79434d3b03505b26caa42def3262945db5b8327b95a0a003cc5513325400; pgv_pvid=2825329760; ua_id=rdfu3R15vwoD0zBWAAAAAEuTMkfxxxLJWgk5F4JZ1rg=; mm_lang=zh_CN; eas_sid=e1G5K3I7Q413H327D8r2D0N0m8; tvfe_boss_uuid=d04d93bc9e7c29dd; o_cookie=1094925362; pac_uid=1_1094925362; noticeLoginFlag=1; pgv_si=s6094909440; uuid=3fcfd3536a1da1617b1c460561fe4ee9; ticket=a42969b394561892ff83833984636cebf5e230e8; ticket_id=gh_bbec56f0be44; cert=kZiwXU4vUjwS4L4VbRFNhQ7wdk1nAg7w; data_bizuin=3279092990; bizuin=3202111501; data_ticket=vS4jc0RF6mPDMY34/PsmRIVOBbvvFgajttGtWY2XrQ7Letj9v+P853t42+JkQ112; slave_sid=ZkZqT2U5SFdCalJNUEhQaV9YWEpQbWRMT3lOWlNZZm9BUExGU0dybjVNZVZxS3d4TFB0YW04dW5VRG94cjA2bmlqd0lBc1FibmJ0cVhOS19TMm1IUWlFSVJZX1RZU3RraG4yMTlBazBZNnhCX2w0aUpNWjMzS2c5WTRJUWhtdmtBOHlmdWsxakFtNDJIc1ph; slave_user=gh_bbec56f0be44; xid=e42471c91cfa65d371d6fe4d219f1c3f; openid2ticket_o_vxyw0uA4Vzrdz952biH10elOaI=blxqkvVWDqz0nohpf5e4CJFqWP8P66HqBtotbbb9bpk=; rewardsn=; wxtokenkey=777"



# """
# 需要提交的data
# 以下个别字段是否一定需要还未验证。
# 注意修改yourtoken,number
# number表示从第number页开始爬取，为5的倍数，从0开始。如0、5、10……
# token可以使用Chrome自带的工具进行获取
# fakeid是公众号独一无二的一个id，等同于后面的__biz
# """
#
#
# # type在网页中会是10，但是无法取到对应的消息link地址，改为9就可以了
# type = '9'
# data1 = {
#     "token": token,
#     "lang": "zh_CN",
#     "f": "json",
#     "ajax": "1",
#     "action": "list_ex",
#     "begin": "0",
#     "count": "5",
#     "query": "",
#     "fakeid": fakeid,
#     "type": type,
# }
params1 = {
    "action":"getmsg",
    "__biz":_biz,
    "f":"json",
    "offset":1,
    "count":10,
    "is_ok":1,
    "scene":124,
    "uin":uin,
    "key":get_key,
    "pass_ticket":get_pass_ticket,
    "wxtoken":"",
    "appmsg_token":get_appmsg_token,
    "x5":0,
    # "f":"json",
}
#https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=10&token=1786288653&lang=zh_CN
#https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin=0&count=5&fakeid=MzI4MTU2NjE3NQ==&type=9&query=&token=1786288653&lang=zh_CN&f=json&ajax=1

# 毫秒数转日期
def getDate(times):
    # print(times)
    timearr = time.localtime(times)
    date = time.strftime("%Y-%m-%d %H:%M:%S", timearr)
    return date


# 最大值365，所以range中就应该是73,15表示前3页
def getAllInfo(url,offset):
    header = {
        "Connection": "keep-alive",
        "Cookie": get_cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1301.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat",

        "X-Requested-With": "XMLHttpRequest",

    }
    # 拿一页，存一页
    messageAllInfo = []
    # begin 从0开始，365结束
    if offset !=0:
        params1["offset"] = params1["offset"]*10
    # 使用get方法进行提交
    #https://mp.weixin.qq.com/cgi-bin/appmsg?begin=0&count=10&t=media/appmsg_list&type=10&action=list&token=1786288653&lang=zh_CN
    content_json = requests.get(url, headers=header, params=params1, verify=False).json()
    time.sleep(10)
    print("1----------------------------------------------")
    print(content_json)
    # print(content_json["general_msg_list"])
    # general_msg_list = json.loads(content_json["general_msg_list"])
    # print(type(json.loads(content_json["general_msg_list"])))
    # print(general_msg_list["list"])
    # print(general_msg_list["list"])
    # 返回了一个json，里面是每一页的数据
    if "general_msg_list" in content_json:
        general_msg_list = json.loads(content_json["general_msg_list"])
        # print(type(json.loads(content_json["general_msg_list"])))
        # print(general_msg_list["list"])
        print(general_msg_list["list"])
        print("wojinglaile")
        print(general_msg_list["list"])
        for item in general_msg_list["list"]:
            if "app_msg_ext_info" in item:
                # 提取每页文章的标题及对应的url
                content_url=item["app_msg_ext_info"]["content_url"]
                # url = item['link']
                title = item['app_msg_ext_info']["title"]
                digest=item['app_msg_ext_info']["digest"]
                url = content_url
                print("---------------------url---------------------------")
                print(url,title)
                # b = getMoreInfo(url,item["title"])
                # print(b)
                readNum, likeNum, comment_count = getMoreInfo(url,title)
                # readNum, likeNum, comment_count = 0,0,0
                info = {
                    "title": title,
                    "readNum": readNum,
                    "likeNum": likeNum,
                    'comment_count': comment_count,
                    "digest": digest,
                    "date": getDate(item['comm_msg_info']['datetime']),
                    "url": url
                }
                messageAllInfo.append(info)
            # print(messageAllInfo)


        return messageAllInfo,content_json["can_msg_continue"]



# 获取阅读数和点赞数
def getMoreInfo(link,title):
    header = {
        "Cookie": post_cookie,
        'Host': 'mp.weixin.qq.com',
        'Origin': 'https://mp.weixin.qq.com',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1301.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Accept-Encoding":"gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4"
    }
    # print(link)
    print("----------------------------getMoreInfo----------------------------")
    # 获得mid,_biz,idx,sn 这几个在link中的信息
    # link = link.split("?")[1]
    mid = re.findall("amp;mid=(.*?)&",link)[0]
    idx = re.findall("amp;idx=(.*?)&",link)[0]
    sn = re.findall("amp;sn=(.*?)&",link)[0]
    _biz = re.findall("__biz=(.*?)&",link)[0]
    print(mid,idx,sn,_biz)

    # fillder 中取得一些不变得信息
    t = int(time.time())
    # params = {
    #     "mock": "",
    #     "f": "json",
    #     "uin": uin,
    #     "key": key,
    #     "pass_ticket": pass_ticket,
    #     "wxtoken": "777",
    #     "devicetype": "Windows&nbsp;10",
    #     "appmsg_token": appmsg_token,
    # }
    params = {
        "f": "json",
        "mock": "",
        "uin":uin,
        "key": post_key,
        "pass_ticket": post_pass_ticket,
        "wxtoken": "777",
        "devicetype": "Windows&nbsp;10&nbsp;x64",
        "clientversion":"62090072",
        "__biz":_biz,
        "appmsg_token": post_appmsg_token,
        "x5":"0",
        "f":"json",
    }
    import urllib.parse
    title1 = urllib.parse.quote(title)
    data = {
        "r": "0.7611613251745863",
        "__biz": _biz,
        "appmsg_type": "9",  # 复制下来的值，会被覆盖掉
        "mid": mid,
        "sn": sn,
        "idx": idx,
        "scene": "38",
        "title": title1,  # 为空，后面覆盖
        "ct": t,
        "abtest_cookie": "",
        "devicetype": "Windows 10 x64",
        "version": "62090072",
        "is_need_ticket": "0",
        "is_need_ad": "0",
        "comment_id": "1310521142813278211",
        "is_need_reward": "1",
        "both_ad": "0",
        "reward_uin_count": "0",
        "send_time": "",
        "msg_daily_idx": "1",
        "is_original": "0",
        "is_only_read": "1",
        "req_id": req_id,  # 一个参数
        "pass_ticket": post_pass_ticket,  # 也可以写死
        "is_temp_url": "0",
        "item_show_type": "0",
        "tmp_version": "1",
        "more_read_type": "0",
        "appmsg_like_type": "2",
        "related_video_sn":"",
        "vid":"",
        "is_pay_subscribe": "0",
        "pay_subscribe_uin_count":"0",
        "has_red_packet_cover":"0"
    }
    """
    添加请求参数
    __biz对应公众号的信息，唯一
    mid、sn、idx分别对应每篇文章的url的信息，需要从url中进行提取
    key、appmsg_token从fiddler上复制即可
    pass_ticket对应的文章的信息，也可以直接从fiddler复制
    """


    print("-----------------------------parms--------------------------")
    print(params)
    print("---------------------------data-----------------------------")
    print(data)
    # 使用post方法进行提交
    content = requests.post(url, headers=header, params=params,data=data , verify=False)
    print("------------一开始的content----------------")
    print(content.text)
    content = content.json()
    # 提取其中的阅读数和点赞数
    print("------------------------content------------------------")
    print(content)
    # print(content["appmsgstat"]["read_num"], content["appmsgstat"]["like_num"])
    try:
        readNum = content["appmsgstat"]["read_num"]
        print("----------------readNum------------------------")
        print(readNum)
    except Exception as e:
        print("------------------readNumerr-----------------")
        print(e)
        readNum = 0
    try:
        likeNum = content["appmsgstat"]["like_num"]
        print("-----------------likeNum----------------------------")
        print(likeNum)
    except Exception as e:
        print("-----------------likeNumerr----------------------------")
        print(e)
        likeNum = 0
    try:
        contentresq = requests.get(link,headers = header).text
        comment_count = content
        print("---------------comment_count-----------------------")
        print("true:" + str(comment_count))
    except:
        comment_count = 0
        print("error:" + str(comment_count))

    # 歇3s，防止被封
    time.sleep(3)
    return readNum, likeNum, comment_count


# 最大值365，所以range中就应该是73,15表示前3页
# def getAllInfo(url, begin):
#     # 拿一页，存一页
#     messageAllInfo = []
#     # begin 从0开始，365结束
#     data1["begin"] = begin
#     # 使用get方法进行提交
#     #https://mp.weixin.qq.com/cgi-bin/appmsg?begin=0&count=10&t=media/appmsg_list&type=10&action=list&token=1786288653&lang=zh_CN
#     content_json = requests.get(url, headers=headers, params=data1, verify=False).json()
#     time.sleep(10)
#     print("1----------------------------------------------")
#     print(content_json)
#     # 返回了一个json，里面是每一页的数据
#     if "app_msg_list" in content_json:
#
#         for item in content_json["app_msg_list"]:
#             # 提取每页文章的标题及对应的url
#             url = item['link']
#             print("---------------------url---------------------------")
#             print(url)
#             # b = getMoreInfo(url,item["title"])
#             # print(b)
#             readNum, likeNum, comment_count = getMoreInfo(url,item["title"])
#             # readNum, likeNum, comment_count = 0,0,0
#             info = {
#                 "title": item['title'],
#                 "readNum": readNum,
#                 "likeNum": likeNum,
#                 'comment_count': comment_count,
#                 "digest": item['digest'],
#                 "date": getDate(item['update_time']),
#                 "url": item['link']
#             }
#             messageAllInfo.append(info)
#         # print(messageAllInfo)
#         return messageAllInfo


# 写入数据库
def save_mysql(urlList):
    print("------------------------save_------------------------")
    for i in urlList:
        print(i)
        try:
            conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
            cur = conn.cursor()
            SQL = 'insert into gongzhonghao (title,read_num,likeNum,content_url,content) values ("%s","%s","%s","%s","%s")'
            cur.execute(SQL % (i["title"], i["readNum"],i["likeNum"],i["url"],i["comment_count"]))
            conn.commit()
            print("写入成功")

        except Exception as e:
            print(e)
            break
        finally:
            cur.close()
            conn.close()




def main():
    # messageAllInfo = []
    # 爬10页成功，从11页开始
    for i in range(0, 500):
    #     # begin = i * 5
    #     offset = i*10
        offset = i
        print("这是页数乘10")
        print(offset)
        messageAllInfo,can_msg_continue = getAllInfo(url,offset)
        # print("第%s页" % i)
        print(messageAllInfo)
        # putIntoMogo(messageAllInfo)
        # save_mysql(messageAllInfo)
        # timenum = random.randint(10,13)
        time.sleep(10000)
        if can_msg_continue==0:
            break


if __name__ == '__main__':
    main()
