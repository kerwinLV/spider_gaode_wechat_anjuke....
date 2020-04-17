import requests
from lxml import etree
from DBUtils.PooledDB import PooledDB
import pymysql
import re
import sys

class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger(r"C:\kerwin\workspace\requestpro\log.txt")
# url = "https://shanghai.anjuke.com/prop/view/A2016395970?from=filter&spread=commsearch&invalid=1&click_url=https://lego-click.anjuke.com/jump?target=pZwY0ZnlsztdraOWUvYKuaY3mhDLPj-6PiYOuARWsHEOm1nVmhR-mBdhPA76nWP-rAwBm1TKnHTkrjNkn1n3TEDQPjc3PjNOrHD3PHn1PWnYTHD1P1TkTHD1P1TkTHD_nHnKnBkQPjDQTHDdrj0knjmkrHnLrj0Kn1TKwbnVNDnVENGsOsJnOChsOCB4OlvUlmaFOmBgl2AClpAdTHDKn9DKsHDKTHDzPHT1P1NkPW0Qn10LPjE3rHmKP9DKnE7-nHNQnHPhuBY3uyNksHE1rHbVmW--PiYOrH7hm1bOryc1mvDKnHcdnjnLPHTvP1nQrjDQnWcdP9DQnWNkn10dnjmLnWTOnjE3njmYTEDKTEDKsEDKTy6YIZK1rBtf0v66UhICmyb8myOJIyV-shPfUiq1myQ-sLKduAq8uzqknBtKnNn1wNwKn1NVnHn1wiYdEbE3sHPDPDmVPWcLwj0QPYFAwbPATHDzPa3LPz3QPHc8rHnKnTDkTEDQsjD1TgVqTHDknjndTHDknjDvPj9KmWcvPvmLnjEVnW9OnzYYnWI-syDvPjnVmHb1uH6WP1IBmWRhTEDYTEDKnkDzsjDYnHD_PWc1nEDQTyFbnWNknjT1PjTkPHFBrHb&uniqid=pc5e97ca8e7db5f3.71975056&region_ids=7&position=30&kwtype=filter&now_time=1587006094"
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
pool = PooledDB(pymysql, 10,
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='ip_proxy_pool',
                charset='utf8'
                )
url = "https://shanghai.anjuke.com/prop/view/A2016338135?from=filter&spread=commsearch&invalid=1&click_url=https://lego-click.anjuke.com/jump?target=pZwY0ZnlsztdraOWUvYKuaY3mhDLPj-6PiYOuARWsHEOm1nVmhR-mBdhPA76nWP-rAwBm1TKn1nQrEDKnHEzrjE1rjn3rHbzn19YP9DzPHcknTDzPHcknTDQsjD1THc_nHEQnEDQPH9LnjTvnjb1P19YTHcKwbnVNDnVENGsOsJnOChsOCB4OlvUlmaFOmBgl2AClpAdTHDKn9DKsHDKTHDzPj9LrjcdPH0kPHD1PWn1nW9KP9DKnEDdnjcvuAc3mzYYmvn1sHw6mvmVmHN1PBdbm1IhPWTduA7BnvmKnHcYrj03nWNdP1cvPHcLnW91n9DQnWE3P19zPHNLnHb3nHm1rHm3TEDKTEDKsEDKTy6YIZK1rBtf0v66UhICmyb8myOJIyV-shPfUiq1myQ-sLKduAq8uzqknBtKnNn1wNwKn1NVnHn1wiYdEbE3sHPDPDmVPWcLwj0QPYFAwbPATHDzPa3LPz3QPHc8rHnKnTDkTEDQsjD1TgVqTHDknjndTHDknjDvPj9KnWEdrH01uj0VmhNOraYYPjbQsHbdrADVnHTknjmLnhF6uHF6TEDYTEDKnkDzsjDYnHD_nHNdP9DQTy7bPAmLnvcvnWP-nyR-uHE&uniqid=pc5e97ca8e7d8293.83688771&region_ids=7&position=2&kwtype=filter&now_time=1587006094%27)"

res = requests.get(url, headers=header)
    # print(res.status_code)
if res.status_code==200:
    issaled = 0
    res_etree = etree.HTML(res.text)
    print(res_etree)
    res_xpath = res_etree.xpath('normalize-space(string(//ul[@class="houseInfo-detail-list clearfix"]))').replace("：","").split(" ") #base节点  父节点
    if res_xpath[0] == "":
        issaled = 1
        res_xpath = res_etree.xpath('normalize-space(string(/html/body/div[3]/div[1]/div[1]/dl))').replace(
            "：", "").split(" ")  # base节点  父节点
        print("res_xpath是空的")
    # print("----------------------------------------------------")
    # print(res_xpath)
    # if "所属小区" in res_xpath:
    #     print(res_xpath.index("小上海新城"))
    # re_1 = re.findall("房本年限：满五年产权性质：(.*?)唯一住房：是一手房源：否",res_xpath,re.S)
    # r = res_xpath.split(" ")
    # print(re_1)
    #['所属小区', '心圆西苑', '房屋户型', '1室', '1厅', '1卫', '房屋单价', '40678', '元/m²', '所在位置', '浦东新区－', '川沙－', '华夏二路1500弄', '\ue003', '建筑面积', '59平方米', '参考首付', '72.00万', '建造年代', '2012年', '房屋朝向', '南', '参考月供', '房屋类型', '普通住宅', '所在楼层', '低层(共15层)', '装修程度', '精装修', '产权年限', '70年产权', '配套电梯', '有', '房本年限', '满五年', '产权性质', '商品房', '唯一住房', '是', '一手房源', '否']

    if "所属小区" in res_xpath:
        local_in = res_xpath.index("所属小区")
        # print(local_in)
        res_secend_xpath_Belonging_District = res_xpath[local_in+1]#所属小区 1
        print(res_secend_xpath_Belonging_District)
    else:
        res_secend_xpath_Belonging_District = ""
    #

    if issaled == 0:
        if "房屋户型" in res_xpath:
            local_in = res_xpath.index("房屋户型")
            # print(local_in)
            res_secend_xpath_Housing_type = res_xpath[local_in+1]+res_xpath[local_in+2]+res_xpath[local_in+2]  # 房屋户型：10
            print(res_secend_xpath_Housing_type)
        else:
            res_secend_xpath_Housing_type = ""
    else:
        if "房屋户型" in res_xpath:
            local_in = res_xpath.index("房屋户型")
            # print(local_in)
            res_secend_xpath_Housing_type = res_xpath[local_in + 1]  # 房屋户型：10
            print(res_secend_xpath_Housing_type)
        else:
            res_secend_xpath_Housing_type = ""


    if "房屋单价" in res_xpath:
        local_in = res_xpath.index("房屋单价")
        res_secend_xpath_Housing_unit_price = res_xpath[local_in+1]+res_xpath[local_in+2]  # 房屋单价：1
        print(res_secend_xpath_Housing_unit_price)
    else:
        res_secend_xpath_Housing_unit_price = ""

    if issaled == 0:
        if "所在位置" in res_xpath:
            local_in = res_xpath.index("所在位置")
            res_secend_xpath_location = res_xpath[local_in+3]       #所在位置精确地址  1
            res_secend_xpath_Area = res_xpath[local_in+1].replace("－","")              #区 1
            res_secend_xpath_zhen = res_xpath[local_in+2].replace("－","")     #镇 1
            print(res_secend_xpath_location)
            print(res_secend_xpath_Area)
            print(res_secend_xpath_zhen)
        else:
            res_secend_xpath_location = ""  # 所在位置精确地址  1
            res_secend_xpath_Area = ""  # 区 1
            res_secend_xpath_zhen = ""  # 镇 1

    else:
        if "所在位置" in res_xpath:
            local_in = res_xpath.index("所在位置")
            print(res_xpath[local_in+1].split("-"))
            res_secend_xpath_location = res_xpath[local_in+1].split("-")[2]       #所在位置精确地址  1
            res_secend_xpath_Area = res_xpath[local_in+1].split("-")[0]             #区 1
            res_secend_xpath_zhen = res_xpath[local_in+1].split("-")[1]     #镇 1
            print(res_secend_xpath_location)
            print(res_secend_xpath_Area)
            print(res_secend_xpath_zhen)

        else:
            res_secend_xpath_location = ""  # 所在位置精确地址  1
            res_secend_xpath_Area = ""  # 区 1
            res_secend_xpath_zhen = ""  #镇 1
    #
    if "建筑面积" in res_xpath:
        local_in = res_xpath.index("建筑面积")
        res_secend_xpath_construction_area = res_xpath[local_in+1]
        print(res_secend_xpath_construction_area)
    else:
        res_secend_xpath_construction_area = ""


    if "参考首付" in res_xpath:
        local_in = res_xpath.index("参考首付")
        res_secend_xpath_Reference_down_payment = res_xpath[local_in+1]    # 参考首付：1
        print(res_secend_xpath_Reference_down_payment)

    else:
        res_secend_xpath_Reference_down_payment=""

    if "建造年代" in res_xpath:
        local_in = res_xpath.index("建造年代")
        res_secend_xpath_Years = res_xpath[local_in+1]  #建造年代：1
        print(res_secend_xpath_Years)
    else:
        res_secend_xpath_Years=""
    if "房屋朝向" in res_xpath:
        local_in = res_xpath.index("房屋朝向")
        res_secend_xpath_House_orientation = res_xpath[local_in+1]  # 房屋朝向 1
        print(res_secend_xpath_House_orientation)
    else:
        res_secend_xpath_House_orientation = ""

    if "房屋类型" in res_xpath:
        local_in = res_xpath.index("房屋类型")
        res_secend_xpath_housetype = res_xpath[local_in+1]  #房屋类型：1
        print(res_secend_xpath_housetype)
    else:
        res_secend_xpath_housetype = ""

    if "所在楼层" in res_xpath:
        local_in = res_xpath.index("所在楼层")
        res_secend_xpath_Floor = res_xpath[local_in+1]  # 所在楼层：1
        print(res_secend_xpath_Floor)
    else:
        res_secend_xpath_Floor=""


    if "装修程度" in res_xpath:
        local_in =res_xpath.index("装修程度")
        res_secend_xpath_Degree_of_decoration = res_xpath[local_in+1]  # 装修程度：：1
        print(res_secend_xpath_Degree_of_decoration)
    else:
        res_secend_xpath_Degree_of_decoration = ""
    #
    if "产权年限" in res_xpath:
        local_in = res_xpath.index("产权年限")
        res_secend_xpath_Property_rights_years = res_xpath[local_in+1]  # 产权年限：1
        print(res_secend_xpath_Property_rights_years)
    else:
        res_secend_xpath_Property_rights_years=""

    if "配套电梯" in res_xpath:
        local_in = res_xpath.index("配套电梯")
        res_secend_xpath_Supporting_elevator = res_xpath[local_in+1]  # 配套电梯：1
        print(res_secend_xpath_Supporting_elevator)
    else:
        res_secend_xpath_Supporting_elevator=""
    #
    if "房本年限" in res_xpath:
        local_in = res_xpath.index("房本年限")
        res_secend_xpath_Year_of_the_room = res_xpath[local_in+1]  # 房本年限：1
        print(res_secend_xpath_Year_of_the_room)
    else:
        res_secend_xpath_Year_of_the_room = ""
    #
    if "产权性质" in res_xpath:
        local_in = res_xpath.index("产权性质")
        res_secend_xpath_Property_nature = res_xpath[local_in+1]  # 产权性质：1
        print(res_secend_xpath_Property_nature)
    else:
        res_secend_xpath_Property_nature=""
    #
    if "唯一住房" in res_xpath:
        local_in=res_xpath.index("唯一住房")
        res_secend_xpath_Only_housing = res_xpath[local_in+1]  # 唯一住房：1
        print(res_secend_xpath_Only_housing)
    else:
        res_secend_xpath_Only_housing = ""

    if "一手房源" in res_xpath:
        local_in =res_xpath.index("一手房源")
        res_secend_xpath_First_hand_housing = res_xpath[local_in+1]  # 一手房源：1
        # res_secend_xpath_First_hand_housing = ""
        print(res_secend_xpath_First_hand_housing)
    else:
        res_secend_xpath_First_hand_housing = ""


    # resklklkk = res_xpath.xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/div/div[1]/ul/li[12]/div[2]/@class')
    # print("kjahkhskhjkhjk")
    # print(resklklkk)
    # print(type(resklklkk))



    xinxidict = {
        "Belonging_District":res_secend_xpath_Belonging_District,
        "Housing_type":res_secend_xpath_Housing_type,
        "location":res_secend_xpath_location,
        "Area":res_secend_xpath_Area,
        "zhen":res_secend_xpath_zhen,
        "Years":res_secend_xpath_Years,
        "housetype":res_secend_xpath_housetype,
        "construction_area":res_secend_xpath_construction_area,
        "House_orientation":res_secend_xpath_House_orientation,
        "Floor":res_secend_xpath_Floor,
        "Degree_of_decoration":res_secend_xpath_Degree_of_decoration,
        "Supporting_elevator":res_secend_xpath_Supporting_elevator,
        "Only_housing":res_secend_xpath_Only_housing,
        "Housing_unit_price":res_secend_xpath_Housing_unit_price,
        "Reference_down_payment":res_secend_xpath_Reference_down_payment,
        "Year_of_the_room":res_secend_xpath_Year_of_the_room,
        "First_hand_housing":res_secend_xpath_First_hand_housing,
        "Property_rights_years":res_secend_xpath_Property_rights_years,
        "Property_nature":res_secend_xpath_Property_nature
    }
    print(xinxidict)
    #
    try:
        conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
        cur = conn.cursor()
        SQL = "insert into ershou_pudonghouse_detail (Belonging_District," \
              "location,Area,zhen," \
              "Years,housetype,construction_area," \
              "House_orientation,Floor,Supporting_elevator," \
              "Only_housing,Housing_unit_price,Reference_down_payment," \
              "Year_of_the_room,First_hand_housing,city,Housing_type,Degree_of_decoration,Property_rights_years,Property_nature) values ('%s'," \
              "'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','上海市','%s','%s','%s','%s')"
        cur.execute(SQL % (xinxidict["Belonging_District"],
                           xinxidict["location"],
                           xinxidict["Area"],
                           xinxidict["zhen"],
                           xinxidict["Years"],
                           xinxidict["housetype"],
                           xinxidict["construction_area"],
                           xinxidict["House_orientation"],
                           xinxidict["Floor"],
                           xinxidict["Supporting_elevator"],
                           xinxidict["Only_housing"],
                           xinxidict["Housing_unit_price"],
                           xinxidict["Reference_down_payment"],
                           xinxidict["Year_of_the_room"],
                           xinxidict["First_hand_housing"],
                           xinxidict["Housing_type"],
                           xinxidict["Degree_of_decoration"],
                           xinxidict["Property_rights_years"],
                           xinxidict["Property_nature"]
                           ))
        conn.commit()
        print("我存入了")
        # conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
        # cur = conn.cursor()
        # SQL = "insert into ershou_pudonghouse_detail (Belonging_District," \
        #       "location,Area,zhen," \
        #       "Years,housetype,construction_area," \
        #       "House_orientation,Floor,Supporting_elevator," \
        #       "Only_housing,Housing_unit_price,Reference_down_payment," \
        #       "Year_of_the_room,First_hand_housing,city,Housing_type,Degree_of_decoration,Property_rights_years,Property_nature) values ('%s'," \
        #       "'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','上海市','%s','%s','%s','%s')"
        # cur.execute(SQL % (res_secend_xpath_Belonging_District,
        #                    res_secend_xpath_location,
        #                    res_secend_xpath_Area,
        #                    res_secend_xpath_zhen,
        #                    res_secend_xpath_Years,
        #                    res_secend_xpath_housetype,
        #                    res_secend_xpath_construction_area,
        #                    res_secend_xpath_House_orientation,
        #                    res_secend_xpath_Floor,
        #                    res_secend_xpath_Supporting_elevator,
        #                    res_secend_xpath_Only_housing,
        #                    res_secend_xpath_Housing_unit_price,
        #                    res_secend_xpath_Reference_down_payment,
        #                    res_secend_xpath_Year_of_the_room,
        #                    res_secend_xpath_First_hand_housing,
        #                    res_secend_xpath_Housing_type,
        #                    res_secend_xpath_Degree_of_decoration,
        #                    res_secend_xpath_Property_rights_years,
        #                    res_secend_xpath_Property_nature
        #                    ))
        # conn.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

    import sys


    class Logger(object):
        def __init__(self, fileN="Default.log"):
            self.terminal = sys.stdout
            self.log = open(fileN, "a")

        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)

        def flush(self):
            pass


    sys.stdout = Logger(r"C:\kerwin\workspace\requestpro\log.txt")  # 保存到D盘
    print('asfasfsaf')
# a = {'Belonging_District': <class 'lxml.etree._ElementUnicodeResult'>,
# 'location': <class 'str'>,
# 'Area': <class 'lxml.etree._ElementUnicodeResult'>,
# 'zhen': <class 'lxml.etree._ElementUnicodeResult'>,
# 'Years': <class 'lxml.etree._ElementUnicodeResult'>,
# 'housetype': <class 'lxml.etree._ElementUnicodeResult'>,
# 'construction_area': <class 'lxml.etree._ElementUnicodeResult'>,
# 'House_orientation': <class 'lxml.etree._ElementUnicodeResult'>,
# 'Floor': <class 'lxml.etree._ElementUnicodeResult'>,
# 'Supporting_elevator': <class 'lxml.etree._ElementUnicodeResult'>,
# 'Only_housing': <class 'lxml.etree._ElementUnicodeResult'>,
# 'Housing_unit_price': <class 'lxml.etree._ElementUnicodeResult'>,
# 'Reference_down_payment': <class 'lxml.etree._ElementUnicodeResult'>,
# 'Year_of_the_room': <class 'lxml.etree._ElementUnicodeResult'>,
# 'First_hand_housing': <class 'lxml.etree._ElementUnicodeResult'>}

# asfasfsaf
