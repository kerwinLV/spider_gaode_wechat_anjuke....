from DBUtils.PooledDB import PooledDB
import pymysql
pool = PooledDB(pymysql,10,
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='ip_proxy_pool',
    charset='utf8'
)

conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了

cur = conn.cursor()

SQL = "SELECT id,href FROM ershou_pudonghouse_href where isspider=0"
i = "http://1231"
cur.execute(SQL.format(1))
cur_result = cur.fetchall()
# print(cur.fetchall())
# for i in cur_result:
#     print(i[0])
#     print(i[1])
it_cur = iter(cur_result)
print(it_cur)
for i in range(0,12):

    print(next(it_cur)[0])
    print(next(it_cur)[1])
# print(next())


cur.close()

conn.close()
