# -*- coding: utf-8 -*-

import time, datetime
import json
import requests
import re
import random
import MySQLdb

#设置要爬取的公众号列表
gzlist=['ckxxwx']
# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "123456", "wechat_reptile_data", charset='utf8' )

# 数据的开始日期 - 结束日期
start_data = '20190630';
end_data = '20190430'


# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 获取阅读数和点赞数
def getMoreInfo(link, query):
    pass_ticket = "VllmJYTSgRotAAiQn17Tw1v35AduDOg%252BLCq%252B07qi4FKcStfL%252Fkc44G0LuIvr99HO"
    if query == 'ckxxwx':
        appmsg_token = "1016_%2F%2Bs3kaOp2TJJQ4EKMVfI0O8RhzRxMs3lLy54hhisceyyXmLHXf_x5xZPaT_pbAJgmwxL19F0XRMWtvYH"
        phoneCookie = "rewardsn=; wxuin=811344139; devicetype=Windows10; version=62060833; lang=zh_CN; pass_ticket=VllmJYTSgRotAAiQn17Tw1v35AduDOg+LCq+07qi4FKcStfL/kc44G0LuIvr99HO; wap_sid2=CIvC8IIDElxlWlVuYlBacDF0TW9sUW16WmNIaDl0cVhxYzZnSHljWlB3TmxfdjlDWmItNVpXeURScG1RNEpuNzFUZFNSZWVZcjE5SHZST2tLZnBSdDUxLWhHRDNQX2dEQUFBfjCasIvpBTgNQAE=; wxtokenkey=777"


    mid = link.split("&")[1].split("=")[1]
    idx = link.split("&")[2].split("=")[1]
    sn = link.split("&")[3].split("=")[1]
    _biz = link.split("&")[0].split("_biz=")[1]

    # 目标url
    url = "http://mp.weixin.qq.com/mp/getappmsgext"
    # 添加Cookie避免登陆操作，这里的"User-Agent"最好为手机浏览器的标识
    headers = {
        "Cookie": phoneCookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.1021.400 QQBrowser/9.0.2524.400"
    }

    # 添加data，`req_id`、`pass_ticket`分别对应文章的信息，从fiddler复制即可。
    data = {
        "is_only_read": "1",
        "is_temp_url": "0",
         "appmsg_type": "9",
        'reward_uin_count': '0'
    }
    params = {
        "__biz": _biz,
        "mid": mid,
        "sn": sn,
        "idx": idx,
        "key": '777',
        "pass_ticket": pass_ticket,
        "appmsg_token": appmsg_token,
        "uin": '777',
        "wxtoken": "777"
    }

    # 使用post方法进行提交
    content = requests.post(url, headers=headers, data=data, params=params).json()

    # 提取其中的阅读数和点赞数
    if 'appmsgstat' in content:
        readNum = content["appmsgstat"]["read_num"]
        likeNum = content["appmsgstat"]["like_num"]
    else:
        print('请求参数过期！')


    # 歇10s，防止被封
    time.sleep(10)
    return readNum, likeNum

#爬取微信公众号文章，并存在本地文本中
def get_content(query):
    #query为要爬取的公众号名称
    #公众号主页
    url = 'https://mp.weixin.qq.com'
    #设置headers
    header = {
        "HOST": "mp.weixin.qq.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
        }

    #读取上一步获取到的cookies
    with open('cookie.txt', 'r', encoding='utf-8') as f:
        cookie = f.read()
    cookies = json.loads(cookie)
    #登录之后的微信公众号首页url变化为：https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN&token=1849751598，从这里获取token信息
    response = requests.get(url=url, cookies=cookies)
    token = re.findall(r'token=(\d+)', str(response.url))[0]
    time.sleep(2)

    #搜索微信公众号的接口地址
    search_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
    #搜索微信公众号接口需要传入的参数，有三个变量：微信公众号token、随机数random、搜索的微信公众号名字
    query_id = {
        'action': 'search_biz',
        'token' : token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'query': query,
        'begin': '0',
        'count': '5'
        }
    #打开搜索微信公众号接口地址，需要传入相关参数信息如：cookies、params、headers
    search_response = requests.get(search_url, cookies=cookies, headers=header, params=query_id)
    #取搜索结果中的第一个公众号
    lists = search_response.json().get('list')[0]
    #获取这个公众号的fakeid，后面爬取公众号文章需要此字段
    fakeid = lists.get('fakeid')

    #微信公众号文章接口地址
    appmsg_url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'
    #搜索文章需要传入几个参数：登录的公众号token、要爬取文章的公众号fakeid、随机数random
    query_id_data = {
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'action': 'list_ex',
        'begin': '0',#不同页，此参数变化，变化规则为每页加5
        'count': '5',
        'query': '',
        'fakeid': fakeid,
        'type': '9'
        }
    #打开搜索的微信公众号文章列表页
    appmsg_response = requests.get(appmsg_url, cookies=cookies, headers=header, params=query_id_data)


    #获取文章总数
    if appmsg_response.json().get('base_resp').get('ret') == 200013:
        print('搜索公众号文章操作频繁,！！！')
    max_num = appmsg_response.json().get('app_msg_cnt')

    #每页至少有5条，获取文章总的页数，爬取时需要分页爬
    num = int(int(max_num) / 5)
    #起始页begin参数，往后每页加5
    begin = 0  # 根据内容自定义

    while num + 1 > 0 :
        query_id_data = {
            'token': token,
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
            'random': random.random(),
            'action': 'list_ex',
            'begin': '{}'.format(str(begin)),
            'count': '5',
            'query': '',
            'fakeid': fakeid,
            'type': '9'
            }
        print('正在翻页：--------------',begin)
        time.sleep(5)
        #获取每一页文章的标题和链接地址，并写入本地文本中
        query_fakeid_response = requests.get(appmsg_url, cookies=cookies, headers=header, params=query_id_data)
        fakeid_list = query_fakeid_response.json().get('app_msg_list')

        for item in fakeid_list:
            content_link=item.get('link')
            content_title=item.get('title')
            update_time=item.get('update_time')
            timeArray = time.localtime(update_time)
            DataTime = time.strftime("%Y%m%d", timeArray)
            print(DataTime)
            Yearsmonth = time.strftime("%Y%m", timeArray)

            if DataTime <= start_data:
                if DataTime <= end_data:
                    mark = '1'
                    print('END....')
                    break  # 退出

                # 阅读数 点赞数
                readNum, likeNum = getMoreInfo(item['link'], query)
                print(readNum, likeNum, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                mark = '0'
                # SQL 插入语句
                sql = """INSERT INTO `wechat_urls` (`title`, `url`, `data_date`, `gzname`, `read_num`, `like_num`) VALUES ('""" + content_title + """', '""" + content_link+ """', '""" + DataTime+ """', '""" + query+ """', '""" + str(readNum)+ """', '""" + str(likeNum)+ """');"""
                try:
                    # 执行sql语句
                    print(sql)
                    cursor.execute(sql)
                    # 提交到数据库执行
                    db.commit()
                except:
                    # Rollback in case there is any error
                    db.rollback()
            elif DataTime >= start_data:
                mark = '2'
                print('END....')
                break  # 退出
            time.sleep(5)

        if mark == '0':
            num -= 1
            begin = int(begin)
            begin += 5
            time.sleep(3)
        elif mark == '1':
            break  # 退出
        elif mark == '2':
            num -= 1
            begin = int(begin)
            begin += 1
            time.sleep(20)


        # 关闭数据库连接
        # db.close()

if __name__=='__main__':
    try:
        #登录之后，通过微信公众号后台提供的微信公众号文章接口爬取文章
        for query in gzlist:
            #爬取微信公众号文章，并存在本地文本中
            print("开始爬取公众号："+query)
            get_content(query)
            print("爬取完成")
    except Exception as e:
        print(str(e))
