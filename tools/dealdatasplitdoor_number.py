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
# SQL = 'select * from tb_gaode_dropdup'
SQL = "SELECT * FROM tb_gaode_dropdup WHERE addresses LIKE '%-%' AND addresses LIKE '%号%' AND addresses LIKE '%路%' AND id NOT IN (20452,20629,23979,28070)"
cur1.execute(SQL)
data = cur1.fetchall()

# dataiter = iter(data)
dataiter = data
cur1.close()
conn.close()
for jk in range(0, len(data) + 1):
    i = dataiter[jk]
    print(i)
    # print(i)
    # for i in add_list:
    i_addres = i[5]
    i_num = re.findall("(\d+)", i_addres)
    if len(i_num) == 2 and int(i_num[0]) < int(i_num[1]):
        # print(i_num)
        for j in range(int(i_num[0]), int(i_num[1]) + 1):
            road = "{}{}号".format(i_addres.split(i_num[0])[0], j)
            print(road)
            time.sleep(1)
            conn2 = pool.connection()
            cur2 = conn2.cursor()
            # print(id, doorplate)
            sql1 = 'INSERT INTO tb_gaode_dropdup ' \
                   '(name,address,doorplate,road,addresses,province,town,' \
                   'area,longitude,latitude,province_code,town_code,' \
                   'area_code,types,test,btype,ctype,stype,status,picture)' \
                   ' VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s",' \
                   '"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'
            cur2.execute(sql1 % (
            i[1], "{}{}号".format(i[4], j), "{}号".format(j), i[4], road, i[7], i[8], i[9], i[10], i[11], i[12], i[13],
            i[14], i[17], i[18], i[19], i[20], i[21], i[22], i[24],))
            conn2.commit()
            print("提交成功")
            # print(i[0],i[3],i[1])
            cur2.close()
            conn2.close()
        # time.sleep(10000)
        conn2 = pool.connection()
        cur2 = conn2.cursor()
        # print(id, doorplate)
        sql1 = 'DELETE FROM tb_gaode_dropdup WHERE id = %s'
        cur2.execute(sql1 % (i[0]))
        conn2.commit()
        print("删除成功")
        # print(i[0],i[3],i[1])
        cur2.close()
        conn2.close()
        #             print("jjjjjjj")
        # print(j)
    #     print(i_)

    else:
        print(i_num)
    # time.sleep(1000)
    # id = i[0]
    # address = i[2]
    # doorplate1 = re.findall("路(.*?)号",address)
    # if doorplate1:
    #     doorplate = doorplate1[0]
    #     conn2 = pool.connection()
    #     cur2 = conn2.cursor()
    #     print(id, doorplate)
    #     sql1 = 'UPDATE tb_gaode SET doorplate="%s" WHERE id="%s"'
    #     cur2.execute(sql1 % ("{}号".format(doorplate), id))
    #     conn2.commit()
    #     print("提交成功")
    #     # print(i[0],i[3],i[1])
    #     cur2.close()
    #     conn2.close()
    # else:
    #     # doorplate=None
    #     continue

    # time.sleep(1000000)
