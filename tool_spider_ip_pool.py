import json
import requests
# from bs4 import BeautifulSoup
from lxml import etree
# import re
import pymysql

# pymysql.connections()

conn = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='ip_proxy_pool',
    charset='utf8'
)
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()

apiurls = []
with open("url.json", "rb") as f:
    apiurls = f.readlines()

APIURLSJSON1 = {}
pr = []  # ip代理池临时数据
for i in apiurls:
    APIURLSJSON1 = json.loads(i.decode("utf-8"))

    for i in range(0, len(APIURLSJSON1)):
        dictti = {}
        dictti["http"] = APIURLSJSON1[str(i)]
        pr.append(dictti)

print(pr[0])
pa = {'http': '47.96.162.28:1080'}
header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}

def requeststext(url, proxy):
    repuests = requests.get(url,headers=header, proxies=proxy)
    return repuests

#使用代理池
for i in range(20,21):
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
        # print(resulturl)
        # print(resultpost)

        for i in range(0, len(resulturl)):
            ip_post = "{}:{}".format(resulturl[i], resultpost[i])
            # print(ip_post)
            # 定义要执行的SQL语句
            sql = "INSERT INTO ip_pools (type,ip) VALUES ('http', '%s')" % (ip_post)
            # 执行SQL语句
            cursor.execute(sql)
            conn.commit()
        # 关闭光标对象
cursor.close()
        # 关闭数据库连接
conn.close()
