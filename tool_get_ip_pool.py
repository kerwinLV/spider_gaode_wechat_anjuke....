from DBUtils.PooledDB import PooledDB
import pymysql
import random
pool = PooledDB(pymysql, 10,
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='ip_proxy_pool',
                charset='utf8'
)

def get_ip():
    conn = pool.connection()
    cur = conn.cursor()
    SQL = "SELECT type,ip FROM ip_pools"
    cur.execute(SQL)
    result = cur.fetchall()
    cur.close()
    conn.close()
    # print(result)
    ip_list = []
    for i in result:
        ip_dict = {}
        ip_dict[i[0]] = i[1]
        ip_list.append(ip_dict)
    return ip_list


# print(random.choice(get_ip()))