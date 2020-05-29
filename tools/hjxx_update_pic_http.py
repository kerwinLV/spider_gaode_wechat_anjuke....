import time
from tools.sqlconn import pool2
conn = pool2.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
cur = conn.cursor()
SQL = 'select * from image_library'
cur.execute(SQL)
data = cur.fetchall()
# print(data)
https_url_new = ""
for i in data:
    old_url = i["url"]
    id_1 = i["id"]
    # print("--------------------------old_url---------------------------")
    # print(id(old_url))
    # print(old_url)
    urllist = old_url.split(",")
    for j in urllist:
        if "http://www.encollege.cn/" in j:
            url = j.split("http")[1]
            httpsurl = "https"+url
            old_url = old_url.replace(j,httpsurl)
    # print("--------------------------new_url---------------------------")
    # print(id(old_url))
    # print(old_url)
    # print("===========================url==================================")
    # print(id(i["url"]))
    # print(i["url"])
    if "http://www.encollege.cn/" in i["url"]:
        SQL = 'update image_library set url=%s where id=%s'
        cur.execute(SQL,(old_url,id_1))
        conn.commit()
        print("修改成功")
    else:
        continue
cur.close()
conn.close()