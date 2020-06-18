import pymysql
from DBUtils.PooledDB import PooledDB

def get_pool():
    pool = PooledDB(pymysql, 10,
                    host='localhost',
                    port=3306,
                    user='root',
                    passwd='123456',
                    db='ip_proxy_pool',
                    charset='utf8'
    )
    return pool

def get_pool1():
    pool1 = PooledDB(pymysql, 10,
                    host='localhost',
                    port=3306,
                    user='root',
                    passwd='123456',
                    db='ip_proxy_pool',
                    charset='utf8',
                    cursorclass = pymysql.cursors.DictCursor
    )
    return pool1

def get_pool_pudongaiofang():
    pool_pudongaiofang = PooledDB(pymysql, 10,
                     host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     db='pudongaiofang',
                     charset='utf8',
                     cursorclass=pymysql.cursors.DictCursor
    )
    return pool_pudongaiofang

def get_pool2():
    pool2 = PooledDB(pymysql, 10,
                    host='192.168.1.190',
                    port=3306,
                    user='dfw9006',
                    passwd='mysql570',
                    db='school_environment',
                    charset='utf8',
                    cursorclass = pymysql.cursors.DictCursor
    )
    return pool2

def get_firepool():
    firepool = PooledDB(pymysql, 10,
                    host='localhost',
                    port=3306,
                    user='root',
                    passwd='123456',
                    db='fire',
                    charset="utf8mb4",
                    cursorclass = pymysql.cursors.DictCursor
    )
    return firepool

def get_minghangsystempool():
    minghangsystempool = PooledDB(pymysql, 10,
                    host='192.168.1.190',
                    port=3306,
                    user='dfw9006',
                    passwd='mysql570',
                    db='minhangsystem',
                    charset='utf8',
                    cursorclass = pymysql.cursors.DictCursor
    )
    return minghangsystempool

def get_pudongsystembpool():
    pudongsystembpool = PooledDB(pymysql, 10,
                    host='192.168.1.190',
                    port=3306,
                    user='dfw9006',
                    passwd='mysql570',
                    db='pudongsystem_b',
                    charset='utf8',
                    cursorclass = pymysql.cursors.DictCursor
    )
    return pudongsystembpool

def get_shanghaiyingjipool():
    shanghaiyingjipool = PooledDB(pymysql, 10,
                    host='localhost',
                    port=3306,
                    user='root',
                    passwd='123456',
                    db='fire',
                    charset="utf8mb4",
                    cursorclass = pymysql.cursors.DictCursor
    )
    return shanghaiyingjipool