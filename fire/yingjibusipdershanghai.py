# coding=utf-8
# @Time    : 2020/6/11 13:28
# @Author  : kerwin
# @File    : yingjibusipdershanghai.py
import time
import requests
from lxml import etree
from tools.sqlconn import shanghaiyingjipool

def get_res(url,headers):

    res = requests.get(url,headers=headers)
    etr1con = etree.HTML(res.text)
    # print(etr1con)
    li = etr1con.xpath('//*[@id="rightSidebar"]/div[1]/ul/li')
    # print(li)
    for i in li:
        wherefrom = i.xpath('./div[1]/text()')[0].encode("GBK","ignore").decode("GBK","ignore").replace("[","").replace("]","")
        # print(wherefrom)
        title = i.xpath('./div[@class="ssjgy_bt"]/a/text()')[0].encode("GBK","ignore").decode("GBK","ignore")
        print(title)
        Introduction = i.xpath('normalize-space(string(./div[@class="ssjgy_jj"]))').encode("GBK","ignore").decode("GBK","ignore")
        # print(Introduction)
        conurl1 = i.xpath('./div[@class="ssjgy_bt"]/a/@href')
        # print(conurl1)
        time_t = i.xpath('./div[@class="ssjgy_sj"]/text()')[0].split("时间：")[1]
        # print(time_t)
        context = requests.get(conurl1[0],headers=headers)
        context.encoding="utf-8"
        contextete = etree.HTML(context.text)
        contextete1 = contextete.xpath('normalize-space(string(//*[@id="rightSidebar"]))').encode("gbk","ignore").decode("gbk","ignore")
        # print(contextete1)
        contextimg = ",".join(contextete.xpath('//*[@id="ivs_content"]/p/img/@src'))
        # print(contextimg)
        save_sql(title,Introduction,contextete1,contextimg,wherefrom,time_t)
        time.sleep(2)

def save_sql(title,Introduction,context,img,wherefrom,t_time):
    conn = shanghaiyingjipool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
    cur1 = conn.cursor()
    # SQL = 'select * from tb_gaode_dropdup'
    SQL = "insert into shanghaiyingji (title,Introduction,context,img,wherefrom,t_time) values (%s,%s,%s,%s,%s,%s)"
    cur1.execute(SQL,(title,Introduction,context,img,wherefrom,t_time))
    conn.commit()
    print("插入成功")
    # dataiter = iter(data)
    # dataiter = data
    cur1.close()
    conn.close()

        # print("uuuuuuuuuu")
    # print(res.text.encode("GBK","ignore").decode("GBK","ignore"))

if __name__=="__main__":
    headers = {
        "Cookie": "wondersLog_zwdt_sdk=%7B%22persistedTime%22%3A1589333352601%2C%22userId%22%3A%22%22%2C%22superProperties%22%3A%7B%22userType%22%3A2%7D%2C%22updatedTime%22%3A1589511332954%2C%22sessionStartTime%22%3A1589511321038%2C%22sessionReferrer%22%3A%22http%3A%2F%2Fzwdt.sh.gov.cn%2FgovPortals%2Fadministrative%2Flist.jsp%22%2C%22deviceId%22%3A%22ee01eeb8d711cc74a2822925e9d0f1c4-4668%22%2C%22LASTEVENT%22%3A%7B%22eventId%22%3A%22wondersLog_pv%22%2C%22time%22%3A1589511332953%7D%2C%22sessionUuid%22%3A7724806067503468%2C%22costTime%22%3A%7B%7D%7D; bdshare_firstime=1591579336509; _gscu_2063925402=91579336r21e4514; _gscbrs_2063925402=1; Hm_lvt_c7988edc44fdcc575dc4519ebf5a34b4=1591579337,1591771296,1591853130; _pk_ref.170.2f90=%5B%22%22%2C%22%22%2C1591853130%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.170.2f90=*; JSESSIONID=BB3745BDA6F91A1080F09C05A213749A; _gscs_2063925402=t918531291hzauv36|pv:8; _pk_id.170.2f90=ab60c78acb11ddeb.1591579337.8.1591853409.1591853130.; Hm_lpvt_c7988edc44fdcc575dc4519ebf5a34b4=1591853409",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    }
    for j in range(11,36):
        print(j)
        url = "http://yjglj.sh.gov.cn/search/searchResultGJ.jsp?t_id=19&site_id=CMSAJJ&type=&q=%E7%81%AB%E7%81%BE&scope=&categoryId=&ts=&te=&pz=30&st=1&p={}"
        url = url.format(j)
        get_res(url,headers)
        time.sleep(2)


