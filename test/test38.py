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

conn = pool.connection()
cur = conn.cursor()
sql = 'insert into all_qudong_area_url (href,isspider) values ("%s","%s")'
cur.execute(sql,('nt="微信公众平台" />\n  <meta property="twitter:description" content="" />\n\n\n        <scrip',1))
conn.commit()
cur.close()
conn.close()
# b = a[0][0]
# print(b)
# c = re.findall("'url': '(.*?)'}",b,re.S)
# print(c)