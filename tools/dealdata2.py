 # -*- coding: utf-8 -*-

import sys
import os
import time
import re
import json
from tools.sqlconn import pool
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir))


def get_hao_l(dataiter):
    for jk in range(0, len(data) + 1):
        i = dataiter[jk]
        id = i[0]
        addresses = i[6]
        if "号" in addresses and "-" not in addresses and "一" not in addresses and "、" not in addresses and "～" not in addresses:
            doorplate = re.findall("上海市.*?(\d+)号", addresses)
            if doorplate:
                conn2 = pool.connection()
                cur2 = conn2.cursor()
                sql1 = 'UPDATE tb_tenxun_copy1 SET doorplate="%s" WHERE id="%s"'
                cur2.execute(sql1 % ("{}号".format(doorplate[0]), id))
                conn2.commit()
                # print("提交成功")
                # print(i[0],i[3],i[1])
                cur2.close()
                conn2.close()
            # print(addresses)
            # print(doorplate)
        elif "-" in addresses:
            doorplate = re.findall("上海市.*?(\d+)-(\d+)号", addresses)
            if doorplate and "N" not in addresses and "L" not in addresses and "G" not in addresses and "F" not in addresses:
                if int(doorplate[0][0]) < int(doorplate[0][1]):
                    print(int(doorplate[0][0]))
                    print(int(doorplate[0][1]))
                    conn2 = pool.connection()
                    cur2 = conn2.cursor()
                    sql1 = 'UPDATE tb_tenxun_copy1 SET doorplate="%s" WHERE id="%s"'
                    cur2.execute(sql1 % ("{}-{}号".format(int(doorplate[0][0]), int(doorplate[0][1])), id))
                    conn2.commit()
                    # print("提交成功")
                    # print(i[0],i[3],i[1])
                    cur2.close()
                    conn2.close()
                    print(addresses)
                    print(doorplate)
        else:
            continue
        # continue
    # return 0
def get_road(dataiter):
    for jk in range(0, len(dataiter) + 1):
        i = dataiter[jk]
        addresses = i[6]
        id = i[0]
        # lane = i[5]
        if "路" in addresses and "区" in addresses:
            road = re.findall("区(.*?)路", addresses)
            print(addresses)
            print(road)
            conn2 = pool.connection()
            cur2 = conn2.cursor()
            print(id, i[3], i[4])
            sql1 = 'UPDATE tb_tenxun_copy1 SET road="%s" WHERE id="%s"'
            cur2.execute(sql1 % ("{}路".format(road[0]), id))
            conn2.commit()
            print("提交成功")
            # print(i[0],i[3],i[1])
            cur2.close()
            conn2.close()
        elif "道" in addresses and "区" in addresses:
            road = re.findall("区(.*?)道", addresses)
            print(addresses)
            print(road)
            conn2 = pool.connection()
            cur2 = conn2.cursor()
            print(id, i[3], i[4])
            sql1 = 'UPDATE tb_tenxun_copy1 SET road="%s" WHERE id="%s"'
            cur2.execute(sql1 % ("{}道".format(road[0]), id))
            conn2.commit()
            print("提交成功")
            # print(i[0],i[3],i[1])
            cur2.close()
            conn2.close()
        elif "街" in addresses and "区" in addresses:
            road = re.findall("区(.*?)街", addresses)
            print(addresses)
            print(road)
            conn2 = pool.connection()
            cur2 = conn2.cursor()
            print(id, i[3], i[4])
            sql1 = 'UPDATE tb_tenxun_copy1 SET road="%s" WHERE id="%s"'
            cur2.execute(sql1 % ("{}街".format(road[0]), id))
            conn2.commit()
            print("提交成功")
            # print(i[0],i[3],i[1])
            cur2.close()
            conn2.close()

def get_lane(dataiter):
    for jk in range(0, len(dataiter) + 1):
        i = dataiter[jk]
        addresses = i[6]
        id = i[0]
        if "弄" in addresses:
            lane = re.findall(".*?(\d+)弄", addresses)
            print(addresses)
            print(lane)
            if lane:
                conn2 = pool.connection()
                cur2 = conn2.cursor()
                print(id, i[3], i[4])
                sql1 = 'UPDATE tb_tenxun_copy1 SET lane="%s" WHERE id="%s"'
                cur2.execute(sql1 % ("{}弄".format(lane[0]), id))
                conn2.commit()
                print("提交成功")
                # print(i[0],i[3],i[1])
                cur2.close()
                conn2.close()


def get_village(dataiter):
    for jk in range(0, len(dataiter) + 1):
        i = dataiter[jk]
        addresses = i[6]
        id = i[0]
        road = i[16]
        # print(i[16])
        if "镇" in road:
            village = re.findall("(.*?)镇", road)
            print(road)
            print(village)
            if village:
                conn2 = pool.connection()
                cur2 = conn2.cursor()
                # print(id, i[3],i[4])
                sql1 = 'UPDATE tb_tenxun_copy1 SET village="%s" WHERE id="%s"'
                cur2.execute(sql1 % ("{}镇".format(village[0]), id))
                conn2.commit()
                print("提交成功")
                # print(i[0],i[3],i[1])
                cur2.close()
                conn2.close()

def get_address(dataiter):
    for jk in range(0, len(dataiter) + 1):
        i = dataiter[jk]
        addresses = i[6]
        id = i[0]
        road = i[5]
        # print(i[16])
        doorplate = i[8]
        print(i)
        if road and doorplate:
            conn2 = pool.connection()
            cur2 = conn2.cursor()
            # print(id, i[3],i[4])
            sql1 = 'UPDATE tb_tenxun_copy1 SET address="%s" WHERE id="%s"'
            cur2.execute(sql1 % ("{}{}{}{}".format(i[3], road, i[6], doorplate), id))
            conn2.commit()
            print("提交成功")
            # print(i[0],i[3],i[1])
            cur2.close()
            conn2.close()

conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
cur1 = conn.cursor()
SQL = 'select * from tb_tenxun_copy1'
cur1.execute(SQL)
data = cur1.fetchall()
dataiter=data
cur1.close()
conn.close()
# 分离出号
# get_hao_l(dataiter)
# 分离出路
# get_road(dataiter)
# 分离出弄
# get_lane(dataiter)
# 分离出镇
# get_village(dataiter)

# for jk in range(0, len(dataiter) + 1):
#     i = dataiter[jk]
#     addresses = i[6]
#     id = i[0]
#     road = i[5]
#     if "路" not in road:
#         # road = road.replace("路","")
#         conn2 = pool.connection()
#         cur2 = conn2.cursor()
#         # print(id, i[3],i[4])
#         sql1 = 'UPDATE tb_tenxun_copy1 SET road="%s" WHERE id="%s"'
#         cur2.execute(sql1 % ("{}路".format(road), id))
#         conn2.commit()
#         print("提交成功")
#         # print(i[0],i[3],i[1])
#         cur2.close()
#         conn2.close()

# 分离出address
get_address(dataiter)






    # print(i[16])
    # doorplate = i[8]
    # print(i)
    # if road and doorplate:
    #     conn2 = pool.connection()
    #     cur2 = conn2.cursor()
    #     # print(id, i[3],i[4])
    #     sql1 = 'UPDATE tb_tenxun_copy1 SET address="%s" WHERE id="%s"'
    #     cur2.execute(sql1 % ("{}{}{}{}".format(i[3],road,i[6],doorplate), id))
    #     conn2.commit()
    #     print("提交成功")
    #     # print(i[0],i[3],i[1])
    #     cur2.close()
    #     conn2.close()
    # if lane ==None:
    #     lane = ""
    #
    # if ("浦东新区" not in address and "上海" not in address) and "路" in address and "镇" not in address:
    #     print(address)
    #     road = re.findall("(.*?)路",address)
    #     if len(road) <=1:
    #         conn2 = pool.connection()
    #         cur2 = conn2.cursor()
    #         print(id, i[3],i[4])
    #         sql1 = 'UPDATE tb_baidu_address SET road="%s" WHERE id="%s"'
    #         cur2.execute(sql1 % ("{}路".format(road[0]), id))
    #         conn2.commit()
    #         print("提交成功")
    #         # print(i[0],i[3],i[1])
    #         cur2.close()
    #         conn2.close()
    #     else:
    #         continue







        # time.sleep(1)


    # address = i[6]
    # lane = i[5]
    # if lane ==None:
    #     lane = ""
    # if i[3] and i[4]:
    #     conn2 = pool.connection()
    #     cur2 = conn2.cursor()
    #     print(id, i[3],i[4])
    #     sql1 = 'UPDATE tb_baidu_address SET address="%s" WHERE id="%s"'
    #     cur2.execute(sql1 % ("{}{}{}".format(i[4],lane,i[3]), id))
    #     conn2.commit()
    #     print("提交成功")
    #     # print(i[0],i[3],i[1])
    #     cur2.close()
    #     conn2.close()
    # if ("浦东新区" not in address and "上海" not in address) and "路" in address and "镇" not in address:
    #     print(address)
    #     road = re.findall("(.*?)路",address)
    #     if len(road) <=1:
    #         conn2 = pool.connection()
    #         cur2 = conn2.cursor()
    #         print(id, i[3],i[4])
    #         sql1 = 'UPDATE tb_baidu_address SET road="%s" WHERE id="%s"'
    #         cur2.execute(sql1 % ("{}路".format(road[0]), id))
    #         conn2.commit()
    #         print("提交成功")
    #         # print(i[0],i[3],i[1])
    #         cur2.close()
    #         conn2.close()
    #     else:
    #         continue
    #
    # else:
    #     continue

    # doorplate = i[3]
    # if doorplate:
    #     if "弄" in doorplate:
    #         # lane = re.findall("(\d+)弄", address)
    #         doorplate = doorplate.split("弄")[1]
    #         print(address)
    #         print(doorplate)
    #         if doorplate:
    #             print("111")
    #             conn2 = pool.connection()
    #             cur2 = conn2.cursor()
    #             print(id, i[3],i[4])
    #             sql1 = 'UPDATE tb_baidu_address SET doorplate="%s" WHERE id="%s"'
    #             cur2.execute(sql1 % ("{}".format(doorplate), id))
    #             conn2.commit()
    #             print("提交成功")
    #             # print(i[0],i[3],i[1])
    #             cur2.close()
    #             conn2.close()
    #         else:
    #             continue
    #     else:
    #         continue
    # doorplate1 = re.findall("路(.*?)号",address)
    # print(address)
    # if "镇" in address and "镇路" not in address:
    #     # print(address)
    #     if "浦东新区" in address or "上海" in address:
    #         # print(i[6])
    #         # print("1111")
    #         lane = re.findall("新区(.*?)镇",address)
    #         if lane:
    #             # print(address)
    #             # print(lane)
    #             # print(len(lane[0]))
    #             if len(lane[0]) > 3:
    #                 lane = ""
    #             else:
    #                 lane = lane
    #
    #         else:
    #             lane = ""
    #         # print(i[6])
    #         # print(lane)
    #     else:
    #         # print(address)
    #         lane = re.findall("(.*?)镇", address)
    #         if lane:
    #             # print(address)
    #             # print(lane)
    #             # print(len(lane[0]))
    #             if len(lane[0]) > 3:
    #                 lane = ""
    #             else:
    #                 lane = lane
    # else:
    #     lane = ""
    # # print(address)
    # # print(lane)
    # if lane:



        # print(lane)
        # if i[3] and i[4]:
        #     # doorplate = doorplate1[0]
        # conn2 = pool.connection()
        # cur2 = conn2.cursor()
        # print(id, i[3],i[4])
        # sql1 = 'UPDATE tb_baidu_address SET lane="%s" WHERE id="%s"'
        # cur2.execute(sql1 % ("{}镇".format(lane[0]), id))
        # conn2.commit()
        # print("提交成功")
        # # print(i[0],i[3],i[1])
        # cur2.close()
        # conn2.close()
    # else:
    #     # doorplate=None
    #     continue

    # time.sleep(1000000)

