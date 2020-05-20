import requests
import time
import random

import pymysql
from DBUtils.PooledDB import PooledDB
from lxml import etree
import numpy as np


from tools.get_ippools_url import get_ippool_url
from tools.detil_address_name import *
# import threading


pool = PooledDB(pymysql, 10,
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='ip_proxy_pool',
                charset='utf8'
)


# PROXY = get_ippool_url()
# print(PROXY)
def get_pudong_next_level_res(url,params):
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
        all_area_data= np.concatenate((all_area_data,resjson["pois"]))
        res_count = int(resjson["count"])
        # print("------------res_count--------------")
        # print(res_count)
        if res_count>1:
            if res_count%20!=0:
                res_count_page = res_count//20 +1
            else:
                res_count_page = res_count//20
            for i in range(2,res_count_page+1):
                print("第{}页".format(i))
                params["page"] = i
                res = requests.get(url, headers=header, params=params)
                if res.status_code ==200:
                    resjson = res.json()
                    all_area_data = np.concatenate((all_area_data, resjson["pois"]))
                    # print("--------------all_area_data---------")
                    # print(all_area_data)
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





def res_xpath(res):
    etreeht = etree.HTML(res.text)
    etreresname = etreeht.xpath('//div[@class="content-wrapper"]/div[@class="content"]/div[@class="main-content"]/div[43]/a/text()')
    # etreresurl = etreeht.xpath('//div[@class="content-wrapper"]/div[@class="content"]/div[@class="main-content"]/div[43]/a/@href')
    address_name = ["chuansha", "gaoqiao", "beicai", "heqing", "tangzheng", "caolu", "jinqiao", "gaoxing", "gaodong",
                    "zhangjiang", "sanling", "huinan", "zhoupu", "xinchang", "datuan", "kangqiao", "hangtou", "zhuqiao",
                    "niqiang", "xuanqiao", "shuyuan", "wanxiang", "laokang", "nanhuixincheng"]
    # domain_name = "https://baike.baidu.com{}"
    # etreresurl = [domain_name.format(i) for i in etreresurl]
    etre = dict(zip(address_name,etreresname))
    # print(etre)
    return etre


def data_processing(old_data,address_name):
    # address_name = address_name.split("、")
    detil_addres_name_list = []
    for k,v in old_data.items():
        # print(k,v)
        address_name_list = address_name[k].split("、")
        for i in address_name_list:
            detil_name = "上海市浦东新区{}".format(v+i)
            detil_addres_name_list.append(detil_name)
            # print(detil_name)

    return detil_addres_name_list



def save_sql(data_processing_list,addres_id):
    isupdataid = 0
    for i in data_processing_list:
        try:
            conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
            cur = conn.cursor()
            SQL = "insert into gaodedetil_adddres (name,type,address,location,pname,cityname,adname,area_id) value ('%s','%s','%s','%s','%s','%s','%s','%s')"
            cur.execute(SQL%(i["name"],i["type"],i["address"],i["location"],i["pname"],i["cityname"],i["adname"],addres_id))
            conn.commit()
            print("插入成功")
        except Exception as e:
            isupdataid = 1
            print(e)
            print("提交失败")
        finally:
            cur.close()
            conn.close()
    if isupdataid ==0:
        conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
        cur = conn.cursor()
        SQL = 'UPDATE gaodearea_adddres SET isspider=1 where id ="%d"'
        cur.execute(SQL%addres_id)
        conn.commit()
        cur.close()
        conn.close()
        print("改写id成功")
    else:
        print("不修改此条数据")



def select_address_sql():
    try:
        conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
        cur = conn.cursor()
        SQL = "select id,area_address from gaodearea_adddres where isspider=0"
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
    iter_address_list = select_address_sql()
    for i in range(0,529):
    # for i in range(0, 1):
        iter_address_list_one = next(iter_address_list)
        print(iter_address_list_one)
        addres_name_1 = iter_address_list_one[1]
        addres_id = iter_address_list_one[0]
        # key = "aa976f6c03382d7fb373ea8213b3cc21"
        params = {
            "keywords":"",
            "city":310000,
            "citylimit":True,
            "offset": 20,
            "page":1,
            "key":"dc47a95ea9ae3724f1812ffd78b2c9fd",
            "extensions":"all"
        }
        url = "https://restapi.amap.com/v3/place/text"
        params["keywords"]=addres_name_1
        get_res=get_pudong_next_level_res(url,params)
        timenum = random.randint(10,12)
        time.sleep(timenum)
        # print(get_res)
        # respath_data = res_xpath(get_res)
        # print(res_xpath(get_res))
        # data_processing_list = data_processing(respath_data,addres_name)
        save_sql(get_res,addres_id)


