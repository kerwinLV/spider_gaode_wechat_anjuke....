import requests

from lxml import etree
from tools.get_ippools_url import get_ippool_url
from tools.detil_address_name import *
# import threading
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


PROXY = get_ippool_url()
# print(PROXY)
def get_pudong_next_level_res(prxoy):
    url = "https://baike.baidu.com/item/%E6%B5%A6%E4%B8%9C%E6%96%B0%E5%8C%BA/5232458?fromtitle=%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%B5%A6%E4%B8%9C%E6%96%B0%E5%8C%BA&fromid=15403686&fr=aladdin"
    header = {
       "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
    }
    # prxoy = {'https': '58.218.92.170:8400'}
    try:
        res = requests.get(url,headers = header,proxies=prxoy)
        print(res.status_code)
        if res.status_code == 200:
            print("--------200")
            print(prxoy)
            return res
    except Exception as e:
        print(e)
        print("重新再拿一个ip")
        PROXY = get_ippool_url()
        res = get_pudong_next_level_res(PROXY)
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

    for i in data_processing_list:
        try:
            conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
            cur = conn.cursor()
            SQL = "insert into gaodearea_adddres (area_address) value ('%s')"
            cur.execute(SQL%i)
            conn.commit()
            print("插入成功")
        except Exception as e:
            print(e)
            print("提交失败")
        finally:
            cur.close()
            conn.close()



if __name__=='__main__':
    get_res=get_pudong_next_level_res(PROXY)
    respath_data = res_xpath(get_res)
    print(res_xpath(get_res))
    data_processing_list = data_processing(respath_data,addres_name)
    save_sql(data_processing_list)


