import requests
url= "https://mp.weixin.qq.com/s?__biz=MzAwMTMzNzM0NA==&mid=2652096511&idx=2&sn=ab162f9e836c1ccba3cc00ad638ea6bb&chksm=813c5690b64bdf867f23540170ea7c52de9af27ce00ea585016a9e3c1c7c81285910e6a799d5#rd"
headers = {
        #"": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.901.400 QQBrowser/9.0.2524.400"
        "User-Agent":"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"
    }

res = requests.get(url,headers =headers )
# print(res.text)



import pymysql
from DBUtils.PooledDB import PooledDB

pool = PooledDB(pymysql, 10,
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='ip_proxy_pool',
                charset='utf8mb4'
)

conn = pool.connection()
cur = conn.cursor()
sql = 'insert into lvseshanghai_copy1 (content) values (%s)'
cur.execute(sql,(res.text))
conn.commit()
cur.close()
conn.close()