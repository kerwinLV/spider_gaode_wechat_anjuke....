
import requests
from DBUtils.PooledDB import PooledDB
from lxml import etree
import pymysql
import random
from tool_get_ip_pool import get_ip

# pymysql.connections()

pool = PooledDB(pymysql, 10,
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='ip_proxy_pool',
                charset='utf8'
)

# 得到一个可以执行SQL语句的光标对象
# cursor = conn.cursor()

# apiurls = []
# with open("url.json", "rb") as f:
#     apiurls = f.readlines()
#
# APIURLSJSON1 = {}
# pr = []  # ip代理池临时数据
# for i in apiurls:
#     APIURLSJSON1 = json.loads(i.decode("utf-8"))
#
#     for i in range(0, len(APIURLSJSON1)):
#         dictti = {}
#         dictti["http"] = APIURLSJSON1[str(i)]
#         pr.append(dictti)

# print(pr[0])
get_ip_pool = get_ip()
header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}

def requeststext(url, proxy):
    repuests = requests.get(url,headers=header, proxies=proxy)
    return repuests

#使用代理池

# for i in range(0,2):
for i in range(30,60):
    pa = random.choice(get_ip_pool)
    URL = "https://www.kuaidaili.com/free/inha/{}/".format(i)
    requests_1 = requeststext(URL, pa)
    if requests_1.status_code == 200:
        # print(requests_1.text)
        # soup = BeautifulSoup(requests_1.text,'lxml')
        # td = soup.find_all("#list > table > tbody > tr")

        html = etree.HTML(requests_1.text)
        # print(html)
        resulturl = html.xpath("//*[@id='list']/table/tbody/tr/td[1]//text()")
        resultpost = html.xpath("//*[@id='list']/table/tbody/tr/td[2]//text()")
        resulttype = html.xpath("//*[@id='list']/table/tbody/tr/td[4]//text()")
        print(resulturl)
        print(resultpost)

        for i in range(0, len(resulturl)):
            conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
            cur = conn.cursor()
            ip_post = "{}:{}".format(resulturl[i], resultpost[i])
            # print(ip_post)
            # 定义要执行的SQL语句
            sql = "INSERT INTO ip_pools (type,ip) VALUES ('http','%s')" % (ip_post)
            # 执行SQL语句
            cur.execute(sql)
            conn.commit()
            print("插入成功")
            cur.close()
            conn.close()
            # 关闭光标对象

