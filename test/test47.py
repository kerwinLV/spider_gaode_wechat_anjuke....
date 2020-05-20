l = [{'id': 2, 'aid': 2, 'readCount': 925, 'linkReading': '7', 'created': '1589443112'},{'id': 2, 'aid': 5, 'readCount': 925, 'linkReading': '7', 'created': '1589443112'},{'id': 2, 'aid': 3, 'readCount': 925, 'linkReading': '7', 'created': '1589443112'}]
#
# l1 = sorted(l,key = lambda x: x["a"],reverse=True)
# print(l1)
import pymysql
from DBUtils.PooledDB import PooledDB

pool = PooledDB(pymysql, 10,
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='wx',
                charset='utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
)

conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
cur = conn.cursor()
sql = 'select * from wxcms_article_read where aid=%s'
cur.execute(sql, (2))
origindate = cur.fetchall()
l1 = sorted(origindate,key = lambda x: x["readCount"],reverse=True)
print(l1)
# print(type(origindate[0]))
cur.close()
conn.close()