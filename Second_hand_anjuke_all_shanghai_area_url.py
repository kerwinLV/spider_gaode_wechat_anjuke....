import requests
from lxml import etree

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

def get_all_url():
    url = "https://shanghai.anjuke.com/sale/"
    header = {
        "cookie":"sessid=A555D032-5AB0-A703-6418-E4FD19B65B4C; aQQ_ajkguid=A71B6DA6-0CA0-2CE3-F8BA-65E281D74C15; ctid=11; _ga=GA1.2.496016814.1586919064; wmda_uuid=12a0c78b78edc2e2762ffb89fe63e47c; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; 58tj_uuid=954de72c-1343-42eb-9998-9927784991c5; als=0; isp=true; search_words=%E5%8D%83%E6%B1%87%E8%8B%91%E5%9B%9B%E6%9D%91%7C%E6%B2%89%E9%A6%99%E8%8B%91%E4%BA%8C%E8%A1%97%E5%9D%8A; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1587000028,1587113689,1587457938; lps=http%3A%2F%2Fwww.anjuke.com%2F%7Chttps%3A%2F%2Fcn.bing.com%2F; twe=2; wmda_session_id_6289197098934=1587695465955-51cdb4c8-68d1-2b1f; _gid=GA1.2.388161245.1587695466; init_refer=https%253A%252F%252Fcn.bing.com%252F; new_uv=16; new_session=0; ajk_member_captcha=3f5375ea4fcbae4e820939e12de51186; browse_comm_ids=1006701%7C189499%7C990328%7C990260%7C866322; propertys=xhevr3-q99tx6_xgjq38-q99twc_x3imd1-q99to9_xay0s9-q94p48_xeajdu-q94p3j_xffcof-q94nof_x62we6-q8xgmk_xdrorb-q8xe91_2ataaw8-q8xbfy_x8fw8s-q8xagj_xfiobx-q8xa2v_xf7c2b-q8x9ve_xfn1y9-q8x9s6_xe14y5-q8x9nd_wz41d7-q8x5ry_2athg9r-q8x3yf_xg8z6y-q8x24u_xfiwxc-q8wzpn_x61fbh-q8wxzi_xch4gn-q8wwga_xdw306-q8wwd2_x8oa6d-q8vi94_xcid36-q8vi73_xf3fop-q8vi6q_xfngfo-q8vb5y_xea01v-q8t6np_; __xsptplusUT_8=1; __xsptplus8=8.18.1587695469.1587696911.15%233%7Ccn.bing.com%7C%7C%7C%7C%23%23CWYrxn6kIrF_Tspn9RJYFQZhPwTBc3cV%23; xzfzqtoken=QqhncwzkQgnrjSgpb2n7Y%2FPynZEN5JxkTSgDKv1SMofAwpSVLNdP1as3L%2BwHLD8Nin35brBb%2F%2FeSODvMgkQULA%3D%3D",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
    }
    proxy = {"http":"175.43.151.48"}
    req = requests.get(url,headers=header,proxies = proxy)
    print(req.status_code)
    if req.status_code ==200:
        # print("hakjhjk")
        req_etree = etree.HTML(req.text)
        req_xpath = req_etree.xpath('//*[@id="content"]/div[3]/div[1]/span[2]/a[1]/@href')
        # print(req_etree)
        # print(req_xpath)
        req_xpath1 = []
        for i in range(0,len(req_xpath)):
            c = req_xpath[i]+"p{}/#filtersort"
            c= "https://sh.zu.anjuke.com/fangyuan/pudong/p{}"
            req_xpath1.append(c)
        return req_xpath1


if __name__=="__main__":
    all_url = ["https://sh.zu.anjuke.com/fangyuan/pudong/p{}"]
    print("------------all_url--------------")
    print(all_url)
    for i in range(0,len(all_url)):
        for j in range(1,51):
            all_url1 = all_url[i].format(j)
            print("--------------------------------------------")
            print(all_url1)
            conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
            cur = conn.cursor()
            SQL = "insert into all_updong_zufang_url (href) values ('%s')"
            cur.execute(SQL % (all_url1))
            conn.commit()
            print("插入成功")
            cur.close()
            conn.close()



# a = get_all_url()
# print(a)
# b=[]
# for i in range(1,len(a)):
#     c = a[i]+"p%s/#filtersort"
#     print(c%(5))

#https://shanghai.anjuke.com/sale/minhang/p2/#filtersort