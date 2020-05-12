# -*- coding: utf-8 -*-
import time
import re
import json
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

conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
cur1 = conn.cursor()
SQL = 'select * from gaodedatadeal where id >= 85660'
cur1.execute(SQL)
data = cur1.fetchall()
# dataiter = iter(data)
dataiter=data
for jk in range(0,len(data)+1):
    i = dataiter[jk]
    # print(i)
    # print(i[10])
    address,photo,name = i[3],i[10],i[1]
    #photostr = []
    photostr = re.findall("'url': '(.*?)'}", photo, re.S)
    urlstr = ",".join(photostr)
    conn2= pool.connection()
    cur2 = conn2.cursor()
    sql1 = 'UPDATE tb_gaode SET picture="%s" WHERE address="%s" AND name="%s"'
    cur2.execute(sql1 % (urlstr, address,name))
    conn2.commit()
    print("提交成功")
    print(i[0],i[3],i[1])
    cur2.close()
    conn2.close()

cur1.close()
conn.close()
