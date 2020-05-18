import pymysql
import time
import datetime
from DBUtils.PooledDB import PooledDB
import json
pool = PooledDB(pymysql, 10,
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='ip_proxy_pool',
                charset='utf8',
                cursorclass = pymysql.cursors.DictCursor

)

def get_data():
    conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
    cur1 = conn.cursor()
    SQL = 'select * from code_err_huanjin_copy2_copy1'
    cur1.execute(SQL)
    data = cur1.fetchall()
    # print(data)
    cur1.close()
    conn.close()
    return data

def save_date(data):
    for i in data:
        # timeunix = int(i["timeunix"])/1000
        # str_timeunix = datetime.datetime.fromtimestamp(timeunix)
        created= int(i["created"])/1000
        str_created =  datetime.datetime.fromtimestamp(created)
        conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
        cur1 = conn.cursor()
        SQL = 'update huanjingdatadeal2 set str_created=%s where id=%s'
        cur1.execute(SQL,(str_created,i["id"]))
        conn.commit()
        print("提交成功")
        cur1.close()
        conn.close()
        # time.sleep(10)
data = get_data()
print(type(data[0]))
data1 = json.dumps(data,ensure_ascii=False)
with open("aaa.json",encoding="utf-8",mode="w") as f:
    f.writelines(data1)
# print(json.dumps(data))
# save_date(data)
