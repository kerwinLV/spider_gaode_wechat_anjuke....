import pymysql
from DBUtils.PooledDB import PooledDB
import time
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

pool = PooledDB(pymysql, 10,
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='wx',
                charset='utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
)
t = int(time.time())

conn1 = pool.connection()
cur1 = conn1.cursor()
SQL1 = 'select * from wxcms_article_a where sn=%s'
cur1.execute(SQL1,("2"))
onenum = cur1.fetchone()
if onenum:
    print(onenum)
    print("45335")
    SQL1 = "update wxcms_article_a set publicName=%s,issueTime=%s where sn=%s"
    cur1.execute(SQL1, ("3","1","2"))
    conn1.commit()
else:
    print("akgjsgjg")
    print(onenum)
    SQL1 = "insert into wxcms_article_a (sn) values (%s)"
    cur1.execute(SQL1,("2"))
    conn1.commit()
cur1.close()
conn1.close()

print(t)