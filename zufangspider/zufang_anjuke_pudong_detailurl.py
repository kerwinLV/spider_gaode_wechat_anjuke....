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


def requests_result(url, header,proxy):
    print("____requests_result_____")
    res = requests.get(url, headers=header,proxies=proxy)
    # print(res.status_code)
    return res


def rexpath(res_result):
    print("_______________rexpath_________")
    if res_result.status_code == 200:
        # print("ajgjgssjh")
        res_result_xpath = etree.HTML(res_result.text)
        # print(res_result_xpath)
        # zufangurl = res_result_xpath.xpath('//*[@id="list-content"]/div/div[@class="zu-info"]')
        res_result_href = res_result_xpath.xpath('//*[@id="list-content"]/div/div[1]/h3/a/@href')
        arae_url = res_result_xpath.xpath('//*[@id="list-content"]/div/div[1]/address/a/@href')
        # // *[ @ id = "houselist-mod-new"] / li[1] / div[2] / div[1] / a
        # print(res_result_href)
        return res_result_href,arae_url

    else:
        pass


def sql_save(res_href,area_url,url_id):
    print("_________sql_save__________________")
    if res_href and area_url:
        if len(res_href)== len(area_url):
            for i in range(0,len(res_href)):
                # print(i)
                try:
                    conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
                    cur = conn.cursor()
                    SQL = "insert into all_updong_zufang_detil_url (href,area_detil_href) values ('%s','%s')"
                    cur.execute(SQL % (res_href[i],area_url[i]))
                    conn.commit()
                    print("写入成功")
                    SQL = 'UPDATE all_updong_zufang_url SET isspider=1 where id ="%d"'
                    cur.execute(SQL %(url_id))
                    conn.commit()
                    print("id修改成功")
                except Exception as e:
                    print(e)
                    break
                finally:
                    cur.close()
                    conn.close()

        else:
            print("两个链接数量不相等很难受")
    else:
        print("未获取到数据")


def select_sql_url():
    try:
        conn = pool.connection()
        cur = conn.cursor()
        SQL = "SELECT id,href FROM all_updong_zufang_url WHERE isspider=0 "
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
    select_sql_url_list = select_sql_url()

    for n in range(0,801):
        this_nex = next(select_sql_url_list)
        url_href = this_nex[1]
        url_id = this_nex[0]
        print(url_href)
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
        }
        print("=======================================")
        proxy = {"http": "175.43.151.48"}
        res = requests_result(url_href, header,proxy)
        # print(res)
        res_href,area_url = rexpath(res)
        print(res_href)
        print(area_url)
        # print(res_href)
        sql_save(res_href,area_url,url_id)
        time_num = random.randint(3, 5)
        time.sleep(time_num)

            # time.sleep(10)

