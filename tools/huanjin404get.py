import requests
from lxml import etree
import time
import re
import urllib3
from tools.sqlconn import pool

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# from test.test42 import url_list
# {}一级/{}二级/{}名字/{}时间戳
# tupainlujing = "http://www.encollege.cn/imageFile/hjxx/{}/{}/{}/{}.jpg"


def url_list():
    # url = "https://www.encollege.cn/gwapi/article/find?total=23&programaId=%d&page=%d"
    # url = "https://www.encollege.cn/gwapi/article/find?total=42&programaId=%d&page=%d"
    # url = "https://www.encollege.cn/gwapi/article/find?total=828&programaId=%d&page=%d"
    # url = "https://www.encollege.cn/gwapi/article/find?total=209&programaId=%d&page=%d"
    url = "https://www.encollege.cn/gwapi/article/find?total=44&programaId=%d&page=%d"
    page = int(re.findall('\?total=(\d+)', url)[0]) // 20 + 2
    url_list = []
    for i in range(1, 5):
        for j in range(1, page):
            url_list.append(url % (40 + i, j))
            # print(url%(20+i,j))
    return url_list


def getDate(times):
    # print(times)
    timearr = time.localtime(times)
    date = time.strftime("%Y-%m-%d", timearr)
    return date


# url = "https://www.encollege.cn/gwapi/article/find?total=23&programaId=24&page=1"
def get_res(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    }

    res = requests.get(url, headers=headers,verify=False).json()
    items = res["data"]["items"]
    for i in items:
        e = etree.HTML(i["context"])
        proName2 = i["proName"]
        parentName1 = i["parentName"]
        context = i["context"]
        # print(i["context"])
        title = i["title"].replace('"', "")
        # print(title)
        id = i["id"]
        # print(title)
        lujing = e.xpath("//img[@alt]/@src")
        programaId = i["programaId"]
        proParentID = i["proParentID"]
        created = int(time.mktime(time.strptime(i["created"], '%Y-%m-%d %H:%M:%S'))) * 1000
        for j in lujing:
            if "http://www.encollege.cn/imageFile/hjxx/" in j:
                print(j)
                rescode = requests.get(j, headers=headers,verify=False)
                # rescode1 = rescode.status_code
                # print(rescode1)
                # print(j)
                if rescode.status_code != 200:
                    t = re.findall("/(\d+).jpg",j)
                    if t:
                        t = t[0]
                    else:
                        t = ""

                    conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
                    cur = conn.cursor()
                    SQL = 'insert into code_err_huanjin_copy1 (title,url,timeunix,id_id,programaId,created,proParentID,documentsurl,proName2,parentName1) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    cur.execute(SQL, (title, url, t, id, programaId, created, proParentID, j, proName2, parentName1))
                    conn.commit()
                    print("写入成功")
                    cur.close()
                    conn.close()
                else:
                    continue
                # firstnum = re.findall("/documents/(\d+)/(\d+)/",j)[0][0]
                # secondnum = re.findall("/documents/(\d+)/(\d+)/", j)[0][1]
                # if "t=" in j:
                #     t = j.split("?t=")[1]
                #     zuixinglujing = tupainlujing.format(parentName1, proName2, title, t)
                #     print(zuixinglujing)
                #     context = context.replace(j, zuixinglujing)

                # else:
                #     continue
                # except Exception as e:
                #     t = ""
            # else:
            #     continue
            #
        # print(context)
        # data1 = {
        #     "id":id,
        #     "context":context
        # }
        # import json
        # headers = {"Content-Type": "application/json"}
        # # https://www.encollege.cn/gwapi/article/find?programaId=36&temp=1
        # updateurl = "https://www.encollege.cn/gwapi/article/updateContent"
        # res5 = requests.post(updateurl,headers = headers,data=json.dumps(data1))
        # print(res5.text)
        # time.sleep(5)
        # print("----------------------------------------------------------")
        # time.sleep(5)
        # print(firstnum[0][0],firstnum[0][1],t)

        # conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
        # cur = conn.cursor()
        # SQL = 'insert into huanjingdatadeal1 (title,url,firstnum,secondnum,timeunix,id_id,programaId,created,proParentID,documentsurl) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        # cur.execute(SQL, (title,url,firstnum,secondnum,t,id,programaId,created,proParentID,j))
        # conn.commit()
        # print("写入成功")
        # cur.close()
        # conn.close()

        # print(lujing)

    # time.sleep(2)


# print(res["data"]["items"])
# eter = etree.HTML(res.text)
# eterxpth = eter.xpath("//img[@alt]/@src")
# print(eterxpth)


for i in url_list():
    get_res(i)
# for i in eterxpth:
#     firstnum = i.split("/")[2]
#     secondenum = i.split("/")[3]
#     t = i.split("?t=")[1]
#     print(int(t))
#     date1 = getDate(int(t)/1000)
#     print(firstnum,secondenum,date1)
