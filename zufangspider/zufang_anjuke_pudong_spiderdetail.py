import requests
from lxml import etree
import pymysql
from DBUtils.PooledDB import PooledDB
import time
import random
import sys
import re


class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


pool = PooledDB(pymysql, 10,
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='ip_proxy_pool',
                charset='utf8'
                )


# 得到一个可以执行SQL语句的光标对象
# cursor = conn.cursor()


def requests_result(houseurl1,area_url, header,proxy):

    print("____requests_result_____")
    # print(proxy)
    houseres = requests.get(houseurl1, headers=header,proxies = proxy)
    areares = requests.get(area_url, headers=header,proxies = proxy)
    # print(res.status_code)
    return houseres,areares


def rexpath(houseres,areares):
    print("_______________rexpath_________")
    try:
        if houseres.status_code == 200 and areares.status_code ==200:
            issaled=0
            res_etree = etree.HTML(houseres.text)
            # print(res_etree)
            bs64_str = re.findall("data:application/font-ttf;charset=utf-8;base64,(.*?)'\) format\('truetype'\)}", houseres.text,re.S)[0]
            print(bs64_str)


            res_xpath = res_etree.xpath('normalize-space(string(/html/body/div[3]/div[2]/div[1]/ul[1]))') # base节点  父节点
            print(res_xpath)
            # if res_xpath[0] == "":
            #     issaled = 1
            #     res_xpath = res_etree.xpath('normalize-space(string(/html/body/div[3]/div[1]/div[1]/dl))').replace(
            #         "：", "").split(" ")  # base节点  父节点
            #     print("res_xpath是空的")
            # # print(res_xpath)
            # # if "所属小区" in res_xpath:
            # #     print(res_xpath.index("小上海新城"))
            # # re_1 = re.findall("房本年限：满五年产权性质：(.*?)唯一住房：是一手房源：否",res_xpath,re.S)
            # # r = res_xpath.split(" ")
            # # print(re_1)
            #
            # if "所属小区" in res_xpath:
            #     local_in = res_xpath.index("所属小区")
            #     # print(local_in)
            #     res_secend_xpath_Belonging_District = res_xpath[local_in + 1]  # 所属小区 1
            #     # print(res_secend_xpath_Belonging_District)
            # else:
            #     res_secend_xpath_Belonging_District = ""
            # #
            # if issaled == 0:
            #     if "房屋户型" in res_xpath:
            #         local_in = res_xpath.index("房屋户型")
            #         # print(local_in)
            #         res_secend_xpath_Housing_type = res_xpath[local_in + 1] + res_xpath[local_in + 2] + res_xpath[
            #             local_in + 2]  # 房屋户型：10
            #         # print(res_secend_xpath_Housing_type)
            #     else:
            #         res_secend_xpath_Housing_type = ""
            # else:
            #     if "房屋户型" in res_xpath:
            #         local_in = res_xpath.index("房屋户型")
            #         # print(local_in)
            #         res_secend_xpath_Housing_type = res_xpath[local_in + 1]  # 房屋户型：10
            #         # print(res_secend_xpath_Housing_type)
            #     else:
            #         res_secend_xpath_Housing_type = ""
            # # if "房屋户型" in res_xpath:
            # #     local_in = res_xpath.index("房屋户型")
            # #     # print(local_in)
            # #     res_secend_xpath_Housing_type = res_xpath[local_in + 1] + res_xpath[local_in + 2] + res_xpath[
            # #         local_in + 2]  # 房屋户型：10
            # #     # print(res_secend_xpath_Housing_type)
            # # else:
            # #     res_secend_xpath_Housing_type = ""
            #
            # if "房屋单价" in res_xpath:
            #     local_in = res_xpath.index("房屋单价")
            #     res_secend_xpath_Housing_unit_price = res_xpath[local_in + 1] + res_xpath[local_in + 2]  # 房屋单价：1
            #     # print(res_secend_xpath_Housing_unit_price)
            # else:
            #     res_secend_xpath_Housing_unit_price = ""
            #
            # if issaled == 0:
            #     if "所在位置" in res_xpath:
            #         local_in = res_xpath.index("所在位置")
            #
            #         res_secend_xpath_Area = res_xpath[local_in + 1].replace("－", "")  # 区 1
            #         res_secend_xpath_zhen = res_xpath[local_in + 2].replace("－", "")  # 镇 1
            #         jinquedizhi_url  = res_etree.xpath('//div[@class="comm-commoninfo"]/h4/a/@href')
            #         if jinquedizhi_url:
            #             jinquedizhi_url = jinquedizhi_url[0]
            #         header = {
            #             "cookie":"sessid=A555D032-5AB0-A703-6418-E4FD19B65B4C; aQQ_ajkguid=A71B6DA6-0CA0-2CE3-F8BA-65E281D74C15; ctid=11; _ga=GA1.2.496016814.1586919064; wmda_new_uuid=1; wmda_uuid=12a0c78b78edc2e2762ffb89fe63e47c; wmda_visited_projects=%3B6289197098934; 58tj_uuid=954de72c-1343-42eb-9998-9927784991c5; als=0; isp=true; search_words=%E5%8D%83%E6%B1%87%E8%8B%91%E5%9B%9B%E6%9D%91%7C%E6%B2%89%E9%A6%99%E8%8B%91%E4%BA%8C%E8%A1%97%E5%9D%8A; lps=http%3A%2F%2Fwww.anjuke.com%2F%7Chttps%3A%2F%2Fcn.bing.com%2F; twe=2; _gid=GA1.2.388161245.1587695466; ajk_member_captcha=3f5375ea4fcbae4e820939e12de51186; wmda_session_id_6289197098934=1587704903698-f547de4d-3c0b-4d2d; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1587000028,1587113689,1587457938,1587705289; Hm_lpvt_c5899c8768ebee272710c9c5f365a6d8=1587705289; browse_comm_ids=1025933%7C7733%7C1006701%7C189499%7C990328; __xsptplusUT_8=1; init_refer=; new_uv=18; new_session=0; ajk_member_verify=lertWBWba%2BrN7bMrwaQC9BP5dZiALQHyKTFUMQy1JGk%3D; ajk_member_verify2=NjkxNzA2NjZ85omL5py6NDExMTUyOTU2NDUwM3wx; __xsptplus8=8.23.1587710699.1587710938.8%232%7Cwww.baidu.com%7C%7C%7C%7C%23%23Z5cEuWDYV2eg2TdkpEn5AzkU40a7d6w-%23; _gat=1; xzfzqtoken=vsuGoivrevQEVef3vQO2t%2BZsdl%2Brs%2BHfSdeQ8SPb%2F7CsyvlaGxIu6Z18UVx80tVZin35brBb%2F%2FeSODvMgkQULA%3D%3D; propertys=xkf6m9-q9a5ly_xk4kqh-q9a1rc_xhevr3-q99tx6_xgjq38-q99twc_x3imd1-q99to9_xay0s9-q94p48_xeajdu-q94p3j_xffcof-q94nof_x62we6-q8xgmk_xdrorb-q8xe91_2ataaw8-q8xbfy_x8fw8s-q8xagj_xfiobx-q8xa2v_xf7c2b-q8x9ve_xfn1y9-q8x9s6_xe14y5-q8x9nd_wz41d7-q8x5ry_2athg9r-q8x3yf_xg8z6y-q8x24u_xfiwxc-q8wzpn_x61fbh-q8wxzi_xch4gn-q8wwga_xdw306-q8wwd2_x8oa6d-q8vi94_xcid36-q8vi73_xf3fop-q8vi6q_xfngfo-q8vb5y_xea01v-q8t6np_; ajkAuthTicket=TT=3cfcafdcd9860d13fcf009e82aafe436&TS=1587710951250&PBODY=nYFIm3HKKWst5ewZunFoKuNyZzZ6M1SYdzNrkyeB9Rqj1eGLukKwRMa5m_i-edjsGseF4VQDzMNW5Qi-GwlqMVvpuLtrOEFHZxQjIWekkkz632j-PfmDu7ImgiT61ov84urmt00vhyRFfCH4_lI1BtVly3V3DG7yb7WVvDpLNwc&VER=2",
            #             "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
            #         print("---------------第三层url-------------------")
            #         print(jinquedizhi_url)
            #         proxy = {"http": "175.43.151.48"}
            #         res_jinque = requests.get(jinquedizhi_url,headers = header,proxies = proxy)
            #         if res_jinque.status_code ==200:
            #             etrjinque = etree.HTML(res_jinque.text)
            #             etradress = etrjinque.xpath("/html/body/div[2]/div[3]/div[1]/h1/span/text()")[0].split("-",2)[2]
            #             print(etradress)
            #         else:
            #             etradress=""
            #         res_secend_xpath_location = etradress  # 所在位置精确地址  1
            #         # print(res_secend_xpath_location)
            #         # print(res_secend_xpath_Area)
            #         # print(res_secend_xpath_zhen)
            #     else:
            #         res_secend_xpath_location = ""  # 所在位置精确地址  1
            #         res_secend_xpath_Area = ""  # 区 1
            #         res_secend_xpath_zhen = ""  # 镇 1
            #
            # else:
            #     if "所在位置" in res_xpath:
            #         local_in = res_xpath.index("所在位置")
            #         # print(res_xpath[local_in + 1].split("-"))
            #         res_secend_xpath_location = res_xpath[local_in + 1].split("-")[2]  # 所在位置精确地址  1
            #         res_secend_xpath_Area = res_xpath[local_in + 1].split("-")[0]  # 区 1
            #         res_secend_xpath_zhen = res_xpath[local_in + 1].split("-")[1]  # 镇 1
            #         # print(res_secend_xpath_location)
            #         # print(res_secend_xpath_Area)
            #         # print(res_secend_xpath_zhen)
            #
            #     else:
            #         res_secend_xpath_location = ""  # 所在位置精确地址  1
            #         res_secend_xpath_Area = ""  # 区 1
            #         res_secend_xpath_zhen = ""  # 镇 1
            # # if "所在位置" in res_xpath:
            # #     local_in = res_xpath.index("所在位置")
            # #     res_secend_xpath_location = res_xpath[local_in + 3]  # 所在位置精确地址  1
            # #     res_secend_xpath_Area = res_xpath[local_in + 1].replace("－", "")  # 区 1
            # #     res_secend_xpath_zhen = res_xpath[local_in + 2].replace("－", "")  # 镇 1
            # #     # print(res_secend_xpath_location)
            # #     # print(res_secend_xpath_Area)
            # #     # print(res_secend_xpath_zhen)
            # #
            # # else:
            # #     res_secend_xpath_location = ""  # 所在位置精确地址  1
            # #     res_secend_xpath_Area = ""  # 区 1
            # #     res_secend_xpath_zhen = ""  # 镇 1
            # #
            # if "建筑面积" in res_xpath:
            #     local_in = res_xpath.index("建筑面积")
            #     res_secend_xpath_construction_area = res_xpath[local_in + 1]
            #     # print(res_secend_xpath_construction_area)
            # else:
            #     res_secend_xpath_construction_area = ""
            #
            # if "参考首付" in res_xpath:
            #     local_in = res_xpath.index("参考首付")
            #     res_secend_xpath_Reference_down_payment = res_xpath[local_in + 1]  # 参考首付：1
            #     # print(res_secend_xpath_Reference_down_payment)
            #
            # else:
            #     res_secend_xpath_Reference_down_payment = ""
            #
            # if "建造年代" in res_xpath:
            #     local_in = res_xpath.index("建造年代")
            #     res_secend_xpath_Years = res_xpath[local_in + 1]  # 建造年代：1
            #     # print(res_secend_xpath_Years)
            # else:
            #     res_secend_xpath_Years = ""
            # if "房屋朝向" in res_xpath:
            #     local_in = res_xpath.index("房屋朝向")
            #     res_secend_xpath_House_orientation = res_xpath[local_in + 1]  # 房屋朝向 1
            #     # print(res_secend_xpath_House_orientation)
            # else:
            #     res_secend_xpath_House_orientation = ""
            #
            # if "房屋类型" in res_xpath:
            #     local_in = res_xpath.index("房屋类型")
            #     res_secend_xpath_housetype = res_xpath[local_in + 1]  # 房屋类型：1
            #     # print(res_secend_xpath_housetype)
            # else:
            #     res_secend_xpath_housetype = ""
            #
            # if "所在楼层" in res_xpath:
            #     local_in = res_xpath.index("所在楼层")
            #     res_secend_xpath_Floor = res_xpath[local_in + 1]  # 所在楼层：1
            #     # print(res_secend_xpath_Floor)
            # else:
            #     res_secend_xpath_Floor = ""
            #
            # if "装修程度" in res_xpath:
            #     local_in = res_xpath.index("装修程度")
            #     res_secend_xpath_Degree_of_decoration = res_xpath[local_in + 1]  # 装修程度：：1
            #     # print(res_secend_xpath_Degree_of_decoration)
            # else:
            #     res_secend_xpath_Degree_of_decoration = ""
            # #
            # if "产权年限" in res_xpath:
            #     local_in = res_xpath.index("产权年限")
            #     res_secend_xpath_Property_rights_years = res_xpath[local_in + 1]  # 产权年限：1
            #     # print(res_secend_xpath_Property_rights_years)
            # else:
            #     res_secend_xpath_Property_rights_years = ""
            #
            # if "配套电梯" in res_xpath:
            #     local_in = res_xpath.index("配套电梯")
            #     res_secend_xpath_Supporting_elevator = res_xpath[local_in + 1]  # 配套电梯：1
            #     # print(res_secend_xpath_Supporting_elevator)
            # else:
            #     res_secend_xpath_Supporting_elevator = ""
            # #
            # if "房本年限" in res_xpath:
            #     local_in = res_xpath.index("房本年限")
            #     res_secend_xpath_Year_of_the_room = res_xpath[local_in + 1]  # 房本年限：1
            #     # print(res_secend_xpath_Year_of_the_room)
            # else:
            #     res_secend_xpath_Year_of_the_room = ""
            # #
            # if "产权性质" in res_xpath:
            #     local_in = res_xpath.index("产权性质")
            #     res_secend_xpath_Property_nature = res_xpath[local_in + 1]  # 产权性质：1
            #     # print(res_secend_xpath_Property_nature)
            # else:
            #     res_secend_xpath_Property_nature = ""
            # #
            # if "唯一住房" in res_xpath:
            #     local_in = res_xpath.index("唯一住房")
            #     res_secend_xpath_Only_housing = res_xpath[local_in + 1]  # 唯一住房：1
            #     # print(res_secend_xpath_Only_housing)
            # else:
            #     res_secend_xpath_Only_housing = ""
            #
            # if "一手房源" in res_xpath:
            #     local_in = res_xpath.index("一手房源")
            #     res_secend_xpath_First_hand_housing = res_xpath[local_in + 1]  # 一手房源：1
            #     # res_secend_xpath_First_hand_housing = ""
            #     # print(res_secend_xpath_First_hand_housing)
            # else:
            #     res_secend_xpath_First_hand_housing = ""

            # resklklkk = res_xpath.xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/div/div[1]/ul/li[12]/div[2]/@class')
            # print("kjahkhskhjkhjk")
            # print(resklklkk)
            # print(type(resklklkk))

            # xinxidict = {
            #     "Belonging_District": res_secend_xpath_Belonging_District,
            #     "Housing_type": res_secend_xpath_Housing_type,
            #     "location": res_secend_xpath_location,
            #     "Area": res_secend_xpath_Area,
            #     "zhen": res_secend_xpath_zhen,
            #     "Years": res_secend_xpath_Years,
            #     "housetype": res_secend_xpath_housetype,
            #     "construction_area": res_secend_xpath_construction_area,
            #     "House_orientation": res_secend_xpath_House_orientation,
            #     "Floor": res_secend_xpath_Floor,
            #     "Degree_of_decoration": res_secend_xpath_Degree_of_decoration,
            #     "Supporting_elevator": res_secend_xpath_Supporting_elevator,
            #     "Only_housing": res_secend_xpath_Only_housing,
            #     "Housing_unit_price": res_secend_xpath_Housing_unit_price,
            #     "Reference_down_payment": res_secend_xpath_Reference_down_payment,
            #     "Year_of_the_room": res_secend_xpath_Year_of_the_room,
            #     "First_hand_housing": res_secend_xpath_First_hand_housing,
            #     "Property_rights_years": res_secend_xpath_Property_rights_years,
            #     "Property_nature": res_secend_xpath_Property_nature
            # }
            #
            # return xinxidict
        else:
            pass

    except Exception as e:
        print(e)




def sql_save(res_xinxi,url_id):
    print("_________sql_save__________________")
    # print(type(url_id))
    # print(url_id)
    try:
        conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
        cur = conn.cursor()
        if res_xinxi["Belonging_District"] != "":
            SQL = "insert into ershou_pudonghouse_detail_second (Belonging_District," \
                  "location,Area,zhen," \
                  "Years,housetype,construction_area," \
                  "House_orientation,Floor,Supporting_elevator," \
                  "Only_housing,Housing_unit_price,Reference_down_payment," \
                  "Year_of_the_room,First_hand_housing,city,Housing_type,Degree_of_decoration,Property_rights_years,Property_nature,href_id) values ('%s'," \
                  "'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','上海市','%s','%s','%s','%s','%d')"
            print("执行SQL")
            cur.execute(SQL % (res_xinxi["Belonging_District"],
                               res_xinxi["location"],
                               res_xinxi["Area"],
                               res_xinxi["zhen"],
                               res_xinxi["Years"],
                               res_xinxi["housetype"],
                               res_xinxi["construction_area"],
                               res_xinxi["House_orientation"],
                               res_xinxi["Floor"],
                               res_xinxi["Supporting_elevator"],
                               res_xinxi["Only_housing"],
                               res_xinxi["Housing_unit_price"],
                               res_xinxi["Reference_down_payment"],
                               res_xinxi["Year_of_the_room"],
                               res_xinxi["First_hand_housing"],
                               res_xinxi["Housing_type"],
                               res_xinxi["Degree_of_decoration"],
                               res_xinxi["Property_rights_years"],
                               res_xinxi["Property_nature"],
                               url_id
                               ))
            print("提交前")
            conn.commit()
            print("已存入成功")
            SQL = 'UPDATE ershou_pudonghouse_detil_url SET isspider=1 where id ="%d"'
            cur.execute(SQL %(url_id))
            conn.commit()
            print("已修改id成功")
        else:
            print("这条数据不存入")
    except Exception as e:
        print(e)
        # pass
    finally:
        cur.close()
        conn.close()


# 拿取数据库中的isspider = 0的所有数据并返回生成器
def select_sql_url():
    try:
        conn = pool.connection()
        cur = conn.cursor()
        SQL = "SELECT id,href,area_detil_href FROM all_updong_zufang_detil_url WHERE isspider=0 "
        cur.execute(SQL)
        a = cur.fetchall()
        cur_result = iter(a)
        return cur_result
    except Exception as e:
        print(e)

    finally:
        cur.close()
        conn.close()


if __name__ == '__main__':
    from tool_get_ip_pool import get_ip
    # url = "https://shanghai.anjuke.com/sale/pudong/p{}/#filtersort"
    # sys.stdout = Logger(r"C:\kerwin\workspace\requestpro\log.txt")
    header = {
        "cookie":"sessid=A555D032-5AB0-A703-6418-E4FD19B65B4C; aQQ_ajkguid=A71B6DA6-0CA0-2CE3-F8BA-65E281D74C15; ctid=11; _ga=GA1.2.496016814.1586919064; wmda_new_uuid=1; wmda_uuid=12a0c78b78edc2e2762ffb89fe63e47c; wmda_visited_projects=%3B6289197098934; 58tj_uuid=954de72c-1343-42eb-9998-9927784991c5; als=0; isp=true; search_words=%E5%8D%83%E6%B1%87%E8%8B%91%E5%9B%9B%E6%9D%91%7C%E6%B2%89%E9%A6%99%E8%8B%91%E4%BA%8C%E8%A1%97%E5%9D%8A; lps=http%3A%2F%2Fwww.anjuke.com%2F%7Chttps%3A%2F%2Fcn.bing.com%2F; twe=2; _gid=GA1.2.388161245.1587695466; ajk_member_captcha=3f5375ea4fcbae4e820939e12de51186; wmda_session_id_6289197098934=1587704903698-f547de4d-3c0b-4d2d; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1587000028,1587113689,1587457938,1587705289; Hm_lpvt_c5899c8768ebee272710c9c5f365a6d8=1587705289; browse_comm_ids=1025933%7C7733%7C1006701%7C189499%7C990328; __xsptplusUT_8=1; init_refer=; new_uv=18; new_session=0; ajk_member_verify=lertWBWba%2BrN7bMrwaQC9BP5dZiALQHyKTFUMQy1JGk%3D; ajk_member_verify2=NjkxNzA2NjZ85omL5py6NDExMTUyOTU2NDUwM3wx; __xsptplus8=8.23.1587710699.1587710938.8%232%7Cwww.baidu.com%7C%7C%7C%7C%23%23Z5cEuWDYV2eg2TdkpEn5AzkU40a7d6w-%23; _gat=1; xzfzqtoken=vsuGoivrevQEVef3vQO2t%2BZsdl%2Brs%2BHfSdeQ8SPb%2F7CsyvlaGxIu6Z18UVx80tVZin35brBb%2F%2FeSODvMgkQULA%3D%3D; propertys=xkf6m9-q9a5ly_xk4kqh-q9a1rc_xhevr3-q99tx6_xgjq38-q99twc_x3imd1-q99to9_xay0s9-q94p48_xeajdu-q94p3j_xffcof-q94nof_x62we6-q8xgmk_xdrorb-q8xe91_2ataaw8-q8xbfy_x8fw8s-q8xagj_xfiobx-q8xa2v_xf7c2b-q8x9ve_xfn1y9-q8x9s6_xe14y5-q8x9nd_wz41d7-q8x5ry_2athg9r-q8x3yf_xg8z6y-q8x24u_xfiwxc-q8wzpn_x61fbh-q8wxzi_xch4gn-q8wwga_xdw306-q8wwd2_x8oa6d-q8vi94_xcid36-q8vi73_xf3fop-q8vi6q_xfngfo-q8vb5y_xea01v-q8t6np_; ajkAuthTicket=TT=3cfcafdcd9860d13fcf009e82aafe436&TS=1587710951250&PBODY=nYFIm3HKKWst5ewZunFoKuNyZzZ6M1SYdzNrkyeB9Rqj1eGLukKwRMa5m_i-edjsGseF4VQDzMNW5Qi-GwlqMVvpuLtrOEFHZxQjIWekkkz632j-PfmDu7ImgiT61ov84urmt00vhyRFfCH4_lI1BtVly3V3DG7yb7WVvDpLNwc&VER=2",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
    urlid = select_sql_url()
    # proxy = get_ip()
    for i in range(0, 600):
        # proxy1 = random.choice(proxy)
        url_and_id = next(urlid)
        print("---------------------url---------------------")
        print(url_and_id)
        # print(proxy1)
        # print(url_and_id)

        url_id = url_and_id[0]
        houseurl1 = url_and_id[1]
        area_url = url_and_id[2]
        # url1 = url.format(i)
        # print(url1)
        # print(proxy1)
        proxy = {"http": "175.43.151.48"}
        houseres,areares = requests_result(houseurl1,area_url, header,proxy)
        # print(res)
        res_xinxi = rexpath(houseres,areares)
        print("=----------------数据-----------------------")
        print(res_xinxi)
        # sql_save(res_xinxi,url_id)
        time_num = random.randint(3,5)
        time.sleep(time_num)
