from tools.sqlconn import minghangsystempool

conn = minghangsystempool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
cur = conn.cursor()
sql = 'select * from minhang_fire'
cur.execute(sql)
data = cur.fetchall()
print(data)
cur.close()
conn.close()

for i in data:
    conn = minghangsystempool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
    cur = conn.cursor()
    sql = 'update minhang_fire set longitude=%s,latitude=%s where id=%s'
    if i["location"]:
        cur.execute(sql,(i["location"].split(",")[0],i["location"].split(",")[1],i["id"]))
        conn.commit()
        print("修改")
    cur.close()
    conn.close()