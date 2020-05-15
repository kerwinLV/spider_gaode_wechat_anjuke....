import requests
from lxml import etree
url= "http://mp.weixin.qq.com/s?__biz=MzA5MjUwNzQxNw==&mid=2650631959&idx=1&sn=c050fe4a307dafd2459baa5adef8de94&chksm=8865d361bf125a77b52535a8efefaa85c38507f07306b23c3aa337ed5dbc19fbbe6d47605c18#rd"
headers = {
        #"": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.901.400 QQBrowser/9.0.2524.400"
        "User-Agent":"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"
    }

res = requests.get(url,headers =headers)
ete = etree.HTML(res.text)
a = ete.xpath('//*[@id="js_content"]/section')
# print(a[0].toString)
# print(res.text)
# print(etree.tostring(a[0],method='html'))
print(a)
content = etree.tostring(a[0],encoding="utf-8",method='html').decode("utf-8")
print("--------------------------------------------------------------------------------")
print(content)



# import pymysql
# from DBUtils.PooledDB import PooledDB
#
# pool = PooledDB(pymysql, 10,
#                 host='localhost',
#                 port=3306,
#                 user='root',
#                 passwd='123456',
#                 db='ip_proxy_pool',
#                 charset='utf8mb4'
# )
#
# conn = pool.connection()
# cur = conn.cursor()
# sql = 'insert into lvseshanghai_copy1 (content) values (%s)'
# cur.execute(sql,(res.text))
# conn.commit()
# cur.close()
# conn.close()