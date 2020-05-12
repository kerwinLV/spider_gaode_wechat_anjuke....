# -- coding: utf-8 --
import time
import random

import requests
import pymysql
from DBUtils.PooledDB import PooledDB
from lxml import etree
import numpy as np

from tools.get_ippools_url import get_ippool_url
from tools.detil_address_name import *
# import threading
POI = [  '收费站', '桥', '充电站',
        '路侧停车位', '银行', 'ATM', '信用社', '投资理财', '典当行', '写字楼', '住宅区',
        '宿舍', '公司', '园区', '农林园艺', '厂矿', '中央机构', '各级政府', '行政单位',
        '公检法机构', '涉外机构', '党派团体','福利机构', '政治教育机构','高速公路入口',
        '机场出口', '机场入口', '车站出口', '车站入口', '门', '停车场出入口', '岛屿', '山峰', '水系']
p =['中餐厅', '外国餐厅', '小吃快餐店', '蛋糕甜品店', '咖啡厅', '茶座', '酒吧', '星级酒店',
    '快捷酒店', '公寓式酒店', '购物中心', '百货商场', '超市', '便利店', '家居建材', '家电数码',
    '商铺', '集市', '通讯营业厅', '邮局', '物流公司', '售票处', '洗衣店', '图文快印店', '照相馆'
    , '房产中介机构', '公用事业', '维修点', '家政服务', '殡葬服务', '彩票销售点', '宠物服务',
    '报刊亭', '公共厕所', '美容','美发', '美甲', '美体', '公园', '动物园', '植物园', '游乐园', '博物馆', '水族馆',
        '海滨浴场', '文物古迹', '教堂', '风景区', '度假村', '农家院', '电影院', 'KTV',
        '剧院', '歌舞厅', '网吧', '游戏场所', '洗浴按摩', '休闲广场', '体育场馆',
        '极限运动场所', '健身中心', '高等院校', '中学', '小学', '幼儿园', '成人教育',
        '亲子教育', '特殊教育学校', '留学中介机构', '科研机构', '培训机构', '图书馆',
        '科技馆', '新闻出版', '广播电视', '艺术团体', '美术馆', '展览馆', '文化宫',
        '综合医院', '专科医院', '诊所', '药店', '体检机构', '疗养院', '急救中心',
        '疾控中心', '汽车销售', '汽车维修', '汽车美容', '汽车配件', '汽车租赁',
        '汽车检测场', '飞机场', '火车站', '地铁站', '地铁线路', '长途汽车站', '公交车站',
        '公交线路', '港口', '停车场','加油加气站', '服务区', ]

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
        all_area_data= np.concatenate((all_area_data,resjson["results"]))
        res_count = int(resjson["total"])
        # print("------------res_count--------------")
        # print(all_area_data)
        # print(res_count)
        if res_count>1:
            if res_count%10!=0:
                res_count_page = res_count//10 +1
            else:
                res_count_page = res_count//10
            for i in range(1,res_count_page+1):
                print("第{}页".format(i))
                params["page_num"] = i
                res = requests.get(url, headers=header, params=params)
                if res.status_code ==200:
                    resjson = res.json()
                    # print(resjson["results"])
                    all_area_data = np.concatenate((all_area_data, resjson["results"]))

                    # print("--------------all_area_data---------")
                    # print(all_area_data)
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



def save_sql(data_processing_list):
    # isupdataid = 0
    for i in data_processing_list:
        try:
            print("===============i===========")
            print(i)
            # print('============================i["children"],i["photos"]=============')
            # print(i["children"],i["photos"])
            type = i["detail_info"]["tag"]
            conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
            cur = conn.cursor()
            SQL = 'insert into tb_baidu (name,addresses,province,town,area,longitude,latitude,types) value ("%s","%s","%s","%s","%s","%s","%s","%s")'
            cur.execute(SQL%(i["name"],i["address"],i["province"],i["city"],i["area"],i["location"]["lng"],i["location"]["lat"],type))
            conn.commit()
            print("插入成功")
            cur.close()
            conn.close()
        except Exception as e:
            # isupdataid = 1
            print(e)
            print("提交失败")

    # if isupdataid ==0:
    #     conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
    #     cur = conn.cursor()
    #     SQL = 'UPDATE gaodeleimu SET isspider=1 where id ="%d"'
    #     cur.execute(SQL%addres_id)
    #     conn.commit()
    #     cur.close()
    #     conn.close()
    #     print("改写id成功")
    # else:
    #     print("不修改此条数据")



# def select_address_sql():
#     try:
#         conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
#         cur = conn.cursor()
#         SQL = "select id,third from gaodeleimu where isspider=0"
#         cur.execute(SQL)
#         addres = cur.fetchall()
#         iter_address = iter(addres)
#         return iter_address
#         # conn.commit()
#         # print("插入成功")
#     except Exception as e:
#         print(e)
#     finally:
#         cur.close()
#         conn.close()


if __name__=='__main__':
    # iter_address_list = select_address_sql()
    for i in POI:
    # for i in range(0, 1):
    #     iter_address_list_one = next(iter_address_list)
    #     print(iter_address_list_one)
    #     addres_name_1 = iter_address_list_one[1]
    #     addres_id = iter_address_list_one[0]
        # key = "aa976f6c03382d7fb373ea8213b3cc21"
        params = {
            "query":"",
            "region":289,
            "city_limit":True,
            "scope":2,
            "page_size":20,
            "page_num":0,
            "output":"json",
            "ak":"R2TNbbUlYSZporPw0FtGe81tyQdMW3BZ"
        }
        params["query"] = i
        print(i)
        url = "http://api.map.baidu.com/place/v2/search"
        # params["keywords"]=addres_name_1
        get_res=get_shanghai_next_level_res(url,params)
        # print("------------getres=-----------------------")
        # print(get_res)
        # respath_data = res_xpath(get_res)
        # print(res_xpath(get_res))
        # data_processing_list = data_processing(respath_data,addres_name)
        save_sql(get_res)
        # timenum = random.randint(10, 12)
        # time.sleep(10000)


