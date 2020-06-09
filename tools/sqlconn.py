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

pool1 = PooledDB(pymysql, 10,
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='ip_proxy_pool',
                charset='utf8',
                cursorclass = pymysql.cursors.DictCursor
)

pool_pudongaiofang = PooledDB(pymysql, 10,
                 host='localhost',
                 port=3306,
                 user='root',
                 passwd='123456',
                 db='pudongaiofang',
                 charset='utf8',
                 cursorclass=pymysql.cursors.DictCursor
)

pool2 = PooledDB(pymysql, 10,
                host='192.168.1.190',
                port=3306,
                user='dfw9006',
                passwd='mysql570',
                db='school_environment',
                charset='utf8',
                cursorclass = pymysql.cursors.DictCursor
)
firepool = PooledDB(pymysql, 10,
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='fire',
                charset="utf8mb4",
                cursorclass = pymysql.cursors.DictCursor
)
minghangsystempool = PooledDB(pymysql, 10,
                host='192.168.1.190',
                port=3306,
                user='dfw9006',
                passwd='mysql570',
                db='minhangsystem',
                charset='utf8',
                cursorclass = pymysql.cursors.DictCursor
)