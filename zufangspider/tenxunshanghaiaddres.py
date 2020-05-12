# -- coding: utf-8 --
import time
import random
from urllib import parse

import requests
import pymysql
from DBUtils.PooledDB import PooledDB
from lxml import etree
import numpy as np

from tools.get_ippools_url import get_ippool_url
from tools.detil_address_name import *
from tools.sqlconn import pool
# import threading







# PROXY = get_ippool_url()
# print(PROXY)
def get_shanghai_next_level_res(url,params):
    all_area_data = np.zeros(0,dtype=dict)
    # print(url)
    # url = "https://baike.baidu.com/item/%E6%B5%A6%E4%B8%9C%E6%96%B0%E5%8C%BA/5232458?fromtitle=%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%B5%A6%E4%B8%9C%E6%96%B0%E5%8C%BA&fromid=15403686&fr=aladdin"
    header = {
       "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
    }
    # prxoy = {'https': '58.218.92.170:8400'}
    # try:
    res = requests.get(url,params=params)
    # print(res.status_code)
    if res.status_code == 200:
        resjson = res.json()
        # print("--------200")
        # print(resjson)
        #通过np库中的concatenate连接两个array生成一个新的array
        # print(resjson["results"])
        # print(type(resjson["results"]))
        all_area_data= np.concatenate((all_area_data,resjson["data"]))
        res_count = int(resjson["count"])
        # print("------------res_count--------------")
        # print(all_area_data)
        # print(res_count)
        if res_count>1:
            if res_count%20!=0:
                res_count_page = res_count//20 +1
            else:
                res_count_page = res_count//20
            for i in range(2,res_count_page+1):
                print("第{}页".format(i))
                params["page_index"] = i
                res = requests.get(url, headers=header, params=params)
                if res.status_code ==200:
                    resjson = res.json()
                    # print(resjson["results"])
                    all_area_data = np.concatenate((all_area_data, resjson["data"]))

                    # print("--------------all_area_data---------")
                    # print(all_area_data)
                    # print(resjson["data"])
                    time.sleep(1)
    return all_area_data


            # print(prxoy)

    # except Exception as e:
    #     print(e)
    #     print("重新再拿一个ip")
    #     PROXY = get_ippool_url()
    #     res = get_pudong_next_level_res(url,params)
        # # res = requests.get(url, headers=header, proxies=PROXY,timeout=2)
        # print("else")
        # print(PROXY)
        # return res





# def res_xpath(res):
#     etreeht = etree.HTML(res.text)
#     etreresname = etreeht.xpath('//div[@class="content-wrapper"]/div[@class="content"]/div[@class="main-content"]/div[43]/a/text()')
#     # etreresurl = etreeht.xpath('//div[@class="content-wrapper"]/div[@class="content"]/div[@class="main-content"]/div[43]/a/@href')
#     address_name = ["chuansha", "gaoqiao", "beicai", "heqing", "tangzheng", "caolu", "jinqiao", "gaoxing", "gaodong",
#                     "zhangjiang", "sanling", "huinan", "zhoupu", "xinchang", "datuan", "kangqiao", "hangtou", "zhuqiao",
#                     "niqiang", "xuanqiao", "shuyuan", "wanxiang", "laokang", "nanhuixincheng"]
#     # domain_name = "https://baike.baidu.com{}"
#     # etreresurl = [domain_name.format(i) for i in etreresurl]
#     etre = dict(zip(address_name,etreresname))
#     # print(etre)
#     return etre

#
# def data_processing(old_data,address_name):
#     # address_name = address_name.split("、")
#     detil_addres_name_list = []
#     for k,v in old_data.items():
#         # print(k,v)
#         address_name_list = address_name[k].split("、")
#         for i in address_name_list:
#             detil_name = "上海市浦东新区{}".format(v+i)
#             detil_addres_name_list.append(detil_name)
#             # print(detil_name)
#
#     return detil_addres_name_list



def save_sql(data_processing_list,poi_id):
    isupdataid = 0
    for i in data_processing_list:
        try:
            print("===============i===========")
            print(i)
            # print('============================i["children"],i["photos"]=============')
            # print(i["children"],i["photos"])
            # type = i["detail_info"]["tag"]
            conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
            cur = conn.cursor()
            SQL = 'insert into tb_tenxun (province,area,town,addresses,unit,longitude,latitude,cType) value ("%s","%s","%s","%s","%s","%s","%s","%s")'
            cur.execute(SQL%(i["ad_info"]["province"],i["ad_info"]["district"],i["ad_info"]["city"],i["address"],i["title"],i["location"]["lng"],i["location"]["lat"],i["category"]))
            conn.commit()
            print("插入成功")
            cur.close()
            conn.close()

        except Exception as e:
            isupdataid = 1
            print(e)
            print("提交失败")

    if isupdataid ==0:
        conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
        cur = conn.cursor()
        # SQL = 'insert into tb_tenxun (province,area,town,addresses,unit,longitude,latitude,type) value ("%s","%s","%s","%s","%s","%s","%s","%s")'
        SQL = 'UPDATE tenxun_poi SET isspider=1 WHERE id="%s"'
        cur.execute(SQL % (poi_id))
        conn.commit()
        print("修改成功")
        cur.close()
        conn.close()
        print("改写id成功")
    else:
        print("不修改此条数据")



def select_poi_sql():
    try:
        conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
        cur = conn.cursor()
        SQL = "select id,poi from tenxun_poi where isspider=0"
        cur.execute(SQL)
        addres = cur.fetchall()
        iter_address = iter(addres)
        return iter_address
        # conn.commit()
        # print("插入成功")
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()


if __name__=='__main__':
    iter_poi_list = select_poi_sql()
    # for i in POI:
    for i in range(0, 700):
        iter_poi_list_one = next(iter_poi_list)
        # print(iter_address_list_one)
        poi_1 = iter_poi_list_one[1]
        poi_id = iter_poi_list_one[0]
        # key = "aa976f6c03382d7fb373ea8213b3cc21"
        params = {
            "boundary":"region(%E4%B8%8A%E6%B5%B7,0)",
            "keyword":"",
            "page_size":20,
            "page_index":1,
            "orderby":"_distance",
            "key":"SSNBZ-LRZKD-KS243-P437O-OKTH7-IFFU4"
        }
        print(poi_1)
        poi_1 = parse.quote(poi_1)
        params["keyword"] = poi_1

        url = "https://apis.map.qq.com/ws/place/v1/search"
        # params["keywords"]=addres_name_1
        get_res=get_shanghai_next_level_res(url,params)
        print(get_res)
        # print("------------getres=-----------------------")
        # print(get_res)
        # respath_data = res_xpath(get_res)
        # print(res_xpath(get_res))
        # data_processing_list = data_processing(respath_data,addres_name)
        save_sql(get_res,poi_id)
        # time.sleep(1000)
        # timenum = random.randint(10, 12)
        # time.sleep(10000)


