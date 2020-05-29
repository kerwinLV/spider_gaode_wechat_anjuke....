# -*- coding: utf-8 -*-
import requests
import time
from lxml import etree
import random
import re
import json
import urllib3
import pymysql
from DBUtils.PooledDB import PooledDB


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

pool = PooledDB(pymysql, 10,
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='wx',
                charset='utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
)
# 西安
# sheetName = "郑州市教工幼儿园"

"""常需要修改"""
publicName = "绿色上海"  #蓝带LeCordonBleu 绿色上海
Cookie = "pgv_pvid=7256621674; pgv_pvi=5590167552; RK=RSqBVIDS96; ptcz=febb259247b2456cc3884c97bde35ebc5d7a917efd2725129180d5002839c0b5; ua_id=WJh9AWtKKFr1RXtiAAAAAA6vPufRh-Dhv6aYtSdPOWU=; noticeLoginFlag=1; mm_lang=zh_CN; openid2ticket_oEsQHj1fpKrIcI9zGY1YXYPExUTk=HOVR8WGE6H1S2PcSSx+MCCrcoF1hy86fW47oMCM4Kbs=; XWINDEXGREY=0; openid2ticket_oMAvowaj5UMMMPSnqii2UWlfUY34=kZZ2HeJSL40xJa9Evv44wg12ZnVKB+P0fTSdyU1uzXc=; ptui_loginuin=2776971405; tvfe_boss_uuid=f6b4f9ad709069c4; o_cookie=2509456238; pac_uid=1_2509456238; pgv_si=s4734450688; pgv_info=ssid=s4812414900; rewardsn=; wxtokenkey=777; uin=o2509456238; skey=@HggcM5YGR; uuid=a6424fa30cefae7ae94123b7530f3720; rand_info=CAESIOKvf1p3tO5DjJ11gvhBW+FXsJiHBpjRgTiTvndvE78Q; slave_bizuin=3253209904; data_bizuin=3253209904; bizuin=3253209904; data_ticket=SEOPkMp8JY8b6sfKtI5NMSyeMmLcLscV3BBwpX2l+W8LT7r9Rkp/mdmXrJjs8D4G; slave_sid=ZTNYR010M2hqRWVJczg5enY1QVdIVGM1dmlCRkJZV1FKeGJYS2dHazJ5d2t3Nk1MTldjNGRnSjVsM1R6SjNSY2V5Vm16cndqazgySUQxU21WRkhBdFZWTm5ZdnE3OGdpOGQ2TGYydzc1ZU1KUnVVMkdOTGJvYXJnalZhTVY3THBuVHZPR3N3ZlhHeEM1NVQ0; slave_user=gh_724a600181bc; xid=99fb71450c5f5e3a093676c20370c557"
token = "283345490"
fakeid = "MzAwMTMzNzM0NA==" #MzA5MjUwNzQxNw==
"""常需要修改"""

# 目标url
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"

# Cookie = "noticeLoginFlag=1; remember_acct=sisecx; pgv_pvi=7219193856; RK=G5400dGxMt; ptcz=557d79434d3b03505b26caa42def3262945db5b8327b95a0a003cc5513325400; pgv_pvid=2825329760; ua_id=rdfu3R15vwoD0zBWAAAAAEuTMkfxxxLJWgk5F4JZ1rg=; mm_lang=zh_CN; eas_sid=e1G5K3I7Q413H327D8r2D0N0m8; tvfe_boss_uuid=d04d93bc9e7c29dd; o_cookie=1094925362; pac_uid=1_1094925362; noticeLoginFlag=1; pgv_si=s6094909440; uuid=3fcfd3536a1da1617b1c460561fe4ee9; ticket=a42969b394561892ff83833984636cebf5e230e8; ticket_id=gh_bbec56f0be44; cert=kZiwXU4vUjwS4L4VbRFNhQ7wdk1nAg7w; data_bizuin=3279092990; bizuin=3202111501; data_ticket=vS4jc0RF6mPDMY34/PsmRIVOBbvvFgajttGtWY2XrQ7Letj9v+P853t42+JkQ112; slave_sid=ZkZqT2U5SFdCalJNUEhQaV9YWEpQbWRMT3lOWlNZZm9BUExGU0dybjVNZVZxS3d4TFB0YW04dW5VRG94cjA2bmlqd0lBc1FibmJ0cVhOS19TMm1IUWlFSVJZX1RZU3RraG4yMTlBazBZNnhCX2w0aUpNWjMzS2c5WTRJUWhtdmtBOHlmdWsxakFtNDJIc1ph; slave_user=gh_bbec56f0be44; xid=e42471c91cfa65d371d6fe4d219f1c3f; openid2ticket_o_vxyw0uA4Vzrdz952biH10elOaI=blxqkvVWDqz0nohpf5e4CJFqWP8P66HqBtotbbb9bpk=; rewardsn=; wxtokenkey=777"


# 使用Cookie，跳过登陆操作
headers = {
    "Cookie": Cookie,
    "Host": "mp.weixin.qq.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
}

"""
需要提交的data
以下个别字段是否一定需要还未验证。
注意修改yourtoken,number
number表示从第number页开始爬取，为5的倍数，从0开始。如0、5、10……
token可以使用Chrome自带的工具进行获取
fakeid是公众号独一无二的一个id，等同于后面的__biz
"""

# type在网页中会是10，但是无法取到对应的消息link地址，改为9就可以了
type = '9'
data1 = {
    "token": token,
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
    "action": "list_ex",
    "begin": "0",
    "count": "5",
    "query": "",
    "fakeid": fakeid,
    "type": type,
}


# https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=10&token=1786288653&lang=zh_CN
# https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin=0&count=5&fakeid=MzI4MTU2NjE3NQ==&type=9&query=&token=1786288653&lang=zh_CN&f=json&ajax=1

# 毫秒数转日期
def getDate(times):
    # print(times)
    timearr = time.localtime(times)
    date = time.strftime("%Y-%m-%d %H:%M:%S", timearr)
    return date


# 最大值365，所以range中就应该是73,15表示前3页
def getAllInfo(url, begin):
    # print("kashkhhhkhkh")
    # 拿一页，存一页
    messageAllInfo = []
    # begin 从0开始，365结束
    data1["begin"] = begin
    # 使用get方法进行提交
    # https://mp.weixin.qq.com/cgi-bin/appmsg?begin=0&count=10&t=media/appmsg_list&type=10&action=list&token=1786288653&lang=zh_CN
    content_json = requests.get(url, headers=headers, params=data1, verify=False).json()
    # time.sleep(10)
    # print("1----------------------------------------------")
    # print(content_json)
    # 返回了一个json，里面是每一页的数据
    # print(content_json)
    if "app_msg_list" in content_json:

        for item in content_json["app_msg_list"]:
            # 提取每页文章的标题及对应的url
            url1 = item['link']
            print("---------------------url---------------------------")
            print(url1)
            # b = getMoreInfo(url,item["title"])
            # print(b)
            readNum, likeNum, content, sn = getMoreInfo(url1, item["title"])
            # readNum, likeNum, comment_count = 0,0,0
            if content !=0:
                info = {
                    "title": item['title'],
                    "readNum": readNum,
                    "likeNum": likeNum,
                    "digest": item['digest'],
                    "date": item['update_time'],
                    "url": url1,
                    "content": content,
                    "sn": sn
                }
                messageAllInfo.append(info)
            else:
                continue
        # print(messageAllInfo)
        # print(begin)
        return messageAllInfo


# 获取阅读数和点赞数
def getMoreInfo(link, title):
    # print(link)
    print("----------------------------getMoreInfo----------------------------")
    # 获得mid,_biz,idx,sn 这几个在link中的信息
    mid = link.split("&")[1].split("=")[1]
    idx = link.split("&")[2].split("=")[1]
    sn = link.split("&")[3].split("=")[1]
    _biz = link.split("&")[0].split("_biz=")[1]

    # fillder 中取得一些不变得信息
    # req_id = "0614ymV0y86FlTVXB02AXd8p"
    """常需要修改"""
    # pass_ticket = "4KzFV%252BkaUHM%252BatRt91i%252FshNERUQyQ0EOwFbc9%252FOe4gv6RiV6%252FJ293IIDnggg1QzC"
    pass_ticket = "fQQ6olYx2Ak1z37wkk2Di53j5OvW3XGIOeLQFRcft2a2lrpJbe9WspmoXvgzesI%252F"
    # appmsg_token = "999_SVODv6i0%2FSNhK8CliOHzbKOydLO3IWXbnYfk2aiso-KkGL9w9a38IZlJCyOAXYyNJXdGn3zR5PTNWklR"
    appmsg_token = "1063_ByO8MPaHvvwMNH%2B7lfbvi2pgGGphv2fbEIA5TzUGVUSXuaDWYi1lXt0W8CL2YhSSjQQsAMS_RoQdRaPA"
    phoneCookie = "rewardsn=; wxtokenkey=777; wxuin=363110653; devicetype=Windows10x64; version=62090072; lang=zh_CN; pass_ticket=fQQ6olYx2Ak1z37wkk2Di53j5OvW3XGIOeLQFRcft2a2lrpJbe9WspmoXvgzesI/; wap_sid2=CP3Bkq0BElwzQUgwS1NpVjdTVFRqSkpLR1NkVUNvUzliVFl6bDF4VFg2d3FCR3dlR2hlMzhsS2hibkMzXzFmRUtTU2xpeVlrbjNETTNKRzlma3JoalNlVmNLM3cteWNFQUFBfjCBw8H2BTgNQAE="
    req_id = "2909WyN5CYl9yz7VxOqVpnC0"
    key = "2c85d7f27a9b1aff19b5d2bd5f0c1a8b3d0ab69af5cbace0cd235f5ee69ca7c5f0cd46ffebc4772dc0634239194cb7710e7af44797651cb739dacea3bb74dab099ad6d4362df85ecae65c7c72deb8e8d"
    uin = "MzYzMTEwNjUz"
    """常需要修改"""
    # 目标url
    url = "https://mp.weixin.qq.com/mp/getappmsgext"
    # 添加Cookie避免登陆操作，这里的"User-Agent"最好为手机浏览器的标识
    # phoneCookie = "wxtokenkey=777; rewardsn=; wxuin=2529518319; devicetype=Windows10; " \
    #               "version=62060619; lang=zh_CN; pass_ticket=4KzFV+kaUHM+atRt91i/shNERUQ" \
    #               "yQ0EOwFbc9/Oe4gv6RiV6/J293IIDnggg1QzC; wap_sid2=CO/FlbYJElxJc2NLcUFIN" \
    #               "kI4Y1hmbllPWWszdXRjMVl6Z3hrd2FKcTFFOERyWkJZUjVFd3cyS3VmZHBkWGRZVG50d0" \
    #               "F3aFZ4NEFEVktZeDEwVHQyN1NrNG80NFZRdWNEQUFBfjC5uYLkBTgNQAE="
    headers = {
        "Cookie": phoneCookie,
        "Host": "mp.weixin.qq.com",
        "Connection": "keep-alive",
        # "": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.901.400 QQBrowser/9.0.2524.400"
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"
    }

    t = int(time.time())

    params = {
        "mock": "",
        "f": "json",
        "__biz": _biz,
        "uin": uin,
        "key": key,
        "mid": mid,
        # "sn": sn,
        # "idx": idx,
        # "key": "f488c6fef5eafe9df3b4884c84601447488b75476cd7c26116c5427e86704be66818df57ccf6e8710db981ea2e9067fd6adb2080066cc7633e8b1d6fe60c52a812ac2b7af0e792c9c845edec8e62c84b",
        # 常需要修改
        "pass_ticket": pass_ticket,
        "appmsg_token": appmsg_token,
        # "uin": "MjUyOTUxODMxOQ%3D%3D",
        "devicetype": "Windows&nbsp;10",
        "wxtoken": "777",
    }
    import urllib.parse
    title1 = urllib.parse.quote(title)
    data = {
        "r": "0.06183692833270871",
        "__biz": _biz,
        "appmsg_type": "9",  # 复制下来的值，会被覆盖掉
        "mid": mid,
        "sn": sn,
        "idx": idx,
        "scene": "38",
        "title": title1,  # 为空，后面覆盖
        "comment_id": "0",
        "ct": t,
        "pass_ticket": pass_ticket,  # 也可以写死
        "req_id": req_id,  # 一个参数
        "abtest_cookie": "",
        "devicetype": "Windows+10",
        "version": "62080085",
        "is_need_ticket": "0",
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
    """
    添加请求参数
    __biz对应公众号的信息，唯一
    mid、sn、idx分别对应每篇文章的url的信息，需要从url中进行提取
    key、appmsg_token从fiddler上复制即可
    pass_ticket对应的文章的信息，也可以直接从fiddler复制
    """

    # print("-----------------------------parms--------------------------")
    # print(params)
    # print("---------------------------data-----------------------------")
    # print(data)
    # 使用post方法进行提交
    content = requests.post(url, headers=headers, data=data, params=params)
    # print("------------一开始的content----------------")
    # print(content.text)
    content = content.json()
    # 提取其中的阅读数和点赞数
    print("------------------------content------------------------")
    # print(content)
    # print(content["appmsgstat"]["read_num"], content["appmsgstat"]["like_num"])
    print(content)
    if "appmsgstat" in content:
        readNum = content["appmsgstat"]["read_num"]
        print("----------------readNum------------------------")
        print(readNum)

        likeNum = content["appmsgstat"]["like_num"]
        print("-----------------likeNum----------------------------")
        print(likeNum)


        headers1 = {
            # "": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.901.400 QQBrowser/9.0.2524.400"
            "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"
        }
        cont = etree.HTML(requests.get(link, headers=headers1).text)
        cont1 = cont.xpath('//*[@id="js_content"]/section')
        if cont1:
            context = etree.tostring(cont1[0],encoding="utf-8",method='html').decode("utf-8")
        else:
            cont1 = cont.xpath('//*[@id="img-content"]')
            if cont1:
                context = etree.tostring(cont1[0],encoding="utf-8", method='html').decode("utf-8")
            else:
                context = ""
            print("可能是转发")
    else:
        print("没有appmsgstat")
        readNum, likeNum, context=0,0,0
        # context=""
    # print("---------------context-----------------------")
    # print("true:" + str(comment_count))

    # print("error:" + str(content))

    # 歇3s，防止被封
    timenum = random.randint(3,5)
    time.sleep(timenum)
    return readNum, likeNum, context, sn


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
    urlListcount = len(urlList)
    print("------------------------save_------------------------")
    for j in range(0,urlListcount):
        i = urlList[j]
        # print(i)
        # try:
        conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
        cur = conn.cursor()
        sql = 'select * from wxcms_article_origin where sn=%s'
        cur.execute(sql, (i["sn"]))
        origindate = cur.fetchone()
        if origindate:
            sql = "update wxcms_article_origin set linkReading=%s,intPageReadCount=%s where sn=%s"
            cur.execute(sql, (i["likeNum"], i["readNum"], i["sn"]))
            conn.commit()
        else:
            sql = 'insert into wxcms_article_origin (title,intPageReadCount,linkReading,url,content,issueTime,digest,sn,publicName) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(sql, (
            i["title"], i["readNum"], i["likeNum"], i["url"], i["content"], i["date"], i["digest"], i["sn"],publicName))
            conn.commit()
        sql = 'select * from wxcms_article_a where sn=%s'
        cur.execute(sql,(i["sn"]))
        onenum = cur.fetchone()
        if onenum:
            sql = 'select * from wxcms_article_read where aid=%s'
            cur.execute(sql,(onenum["id"]))
            read_list = cur.fetchall()
            if read_list:
                read_list1 = sorted(read_list,key=lambda x: x["readCount"],reverse=True)
                if i["readNum"]>read_list1[0]["readCount"]:
                    sql = 'insert into wxcms_article_read (aid,readCount,created,linkReading) values (%s,%s,%s,%s)'
                    cur.execute(sql, (onenum["id"], i["readNum"], int(time.time()), i["likeNum"]))
                    conn.commit()
                else:
                    pass
            else:
                sql ='insert into wxcms_article_read (aid,readCount,created,linkReading) values (%s,%s,%s,%s)'
                cur.execute(sql, (onenum["id"],i["readNum"],int(time.time()),i["likeNum"]))
                conn.commit()

        else:
            sql = 'insert into wxcms_article_a (title,intPageReadCount,linkReading,url,content,issueTime,digest,sn,publicName) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(sql, (i["title"], i["readNum"], i["likeNum"], i["url"], i["content"], i["date"], i["digest"], i["sn"],publicName))
            last_id = cur.lastrowid
            conn.commit()
            sql = 'insert into wxcms_article_read (aid,readCount,created,linkReading) values (%s,%s,%s,%s)'
            cur.execute(sql, (last_id, i["readNum"], int(time.time()), i["likeNum"]))
            conn.commit()

        print("写入成功")
        # except Exception as e:
        #     print(e)
        #     break
        # finally:
        cur.close()
        conn.close()

    # messageAllInfo = []
    # 爬10页成功，从11页开始
    # 蓝带 185 37  read 3677 a 3585 origin 3585
    # 绿色上海 1720 348 300


if __name__ == '__main__':
    for i in range(0, 8):
        begin = i * 5
        print("第%s页" % i)
        messageAllInfo = getAllInfo(url, str(begin))
        # print(messageAllInfo)
        # putIntoMogo(messageAllInfo)
        save_mysql(messageAllInfo)
        # time.sleep(10000)
