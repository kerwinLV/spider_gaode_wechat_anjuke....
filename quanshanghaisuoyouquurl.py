import requests
from lxml import etree

import pymysql
from DBUtils.PooledDB import PooledDB

pool = PooledDB(pymysql, 10,
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='ip_proxy_pool',
                charset='utf8'
                )

def get_all_url():
    url = "https://shanghai.anjuke.com/sale/"
    req = requests.get(url)
    print(req.status_code)
    if req.status_code ==200:
        print("hakjhjk")
        req_etree = etree.HTML(req.text)
        req_xpath = req_etree.xpath('//*[@id="content"]/div[3]/div[1]/span[2]/a/@href')
        print(req_etree)
        print(req_xpath)
        req_xpath1 = []
        for i in range(1,len(req_xpath)):
            c = req_xpath[i]+"p{}/#filtersort"
            req_xpath1.append(c)
        return req_xpath1

all_url = get_all_url()
for i in range(0,len(all_url)):
    for j in range(1,51):
        all_url1 = all_url[i].format(j)
        conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
        cur = conn.cursor()
        SQL = "insert into all_shanghai_area_url (href) values ('%s')"
        cur.execute(SQL % (all_url1))
        conn.commit()

        cur.close()
        conn.close()



# a = get_all_url()
# print(a)
# b=[]
# for i in range(1,len(a)):
#     c = a[i]+"p%s/#filtersort"
#     print(c%(5))

#https://shanghai.anjuke.com/sale/minhang/p2/#filtersort