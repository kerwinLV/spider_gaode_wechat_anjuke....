import requests
from lxml import etree
import pymysql
from DBUtils.PooledDB import PooledDB
import time
import random

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


def requests_result(url, header):
    print("____requests_result_____")
    res = requests.get(url, headers=header)
    # print(res.status_code)
    return res


def rexpath(res_result):
    print("_______________rexpath_________")
    if res_result.status_code == 200:
        print("ajgjgssjh")
        res_result_xpath = etree.HTML(res_result.text)
        # print(res_result_xpath)
        res_result_href = res_result_xpath.xpath('//*[@id="houselist-mod-new"]/li/div[2]/div[1]/a/@href')
        # print(res_result_href)
        return res_result_href


    else:
        pass


def sql_save(res_href):
    print("_________sql_save__________________")
    for i in res_href:
        # print(i)
        try:
            conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
            cur = conn.cursor()
            SQL = "insert into ershou_pudonghouse_href_copy1 (href) values ('%s')"
            cur.execute(SQL % (i))
            conn.commit()
        except Exception as e:
            print(e)
            break
        finally:
            cur.close()
            conn.close()


if __name__ == '__main__':
    from quanshanghaisuoyouquurl import get_all_url
    url_lists = get_all_url()
    print(url_lists)
    for i in range(0,len(url_lists)):
        url = url_lists[i]
        print(url)
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}

        for i in range(1, 51):
            url1 = url.format(i)
            print("=======================================")
            print(url1)
            res = requests_result(url1, header)
            print(res)
            res_href = rexpath(res)
            sql_save(res_href)
            time_num = random.randint(1, 3)
            time.sleep(time_num)
            # time.sleep(10)

