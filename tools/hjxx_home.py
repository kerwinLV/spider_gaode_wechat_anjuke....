import time
import re
import copy

import requests
from lxml import etree

from tools.sqlconn import pool

# from test.test42 import url_list
# {}一级/{}二级/{}名字/{}时间戳
# tupainlujing = "http://www.encollege.cn/imageFile/hjxx/{}/{}/{}/{}.jpg"

# urllist = "https://www.encollege.cn/gwapi/article/find"
# parms = {
#     "programaId":2,
#     "page":1,
# }
# headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
#     }
# resdata = requests.get(urllist,headers =headers,params=parms).json()
# page = resdata["data"]["pageSize"]
#
# print(page)



def parms_list():
    parms_list = []
    for i in range(5,6):
        url = "https://www.encollege.cn/gwapi/article/find"
        parms = {
            "programaId": i,
            "page": 1,
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        }
        resdata = requests.get(url, headers=headers, params=parms).json()
        page = resdata["data"]["pageSize"]
        for j in range(1,page+1):
            parms = copy.deepcopy(parms)
            parms["page"] = j
            # print(parms)
            parms_list.append(parms)
    return parms_list
            # resdata1 = requests.get(url, headers=headers, params=parms).json()


# url_list()
    # url = "https://www.encollege.cn/gwapi/article/find?total=23&programaId=%d&page=%d"
    # url = "https://www.encollege.cn/gwapi/article/find?total=42&programaId=%d&page=%d"
    # url = "https://www.encollege.cn/gwapi/article/find?total=828&programaId=%d&page=%d"
    # url = "https://www.encollege.cn/gwapi/article/find?total=209&programaId=%d&page=%d"
    # url = "https://www.encollege.cn/gwapi/article/find?total=44&programaId=%d&page=%d"
    # page = int(re.findall('\?total=(\d+)', url)[0]) // 20 + 2

        # for i in range(1, 5):
        #     for j in range(1, page):
        #         url_list.append(url % (30+ i, j))
        #         # print(url%(20+i,j))
        # return url_list


def getDate(times):
    # print(times)
    timearr = time.localtime(times)
    date = time.strftime("%Y-%m-%d", timearr)
    return date


# url = "https://www.encollege.cn/gwapi/article/find?total=23&programaId=24&page=1"
def get_res_and_save(parms_list):
    for i in parms_list:
        # print(i)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        }
        url = "https://www.encollege.cn/gwapi/article/find"
        res = requests.get(url, headers=headers,params=i).json()
        items = res["data"]["items"]
        for i in items:
            context = i["context"]
            e = etree.HTML(str(context))
            # print(type(context))
            # print(context)
            proName2 = i["proName"]
            parentName1 = i["parentName"]
            # context = i["context"]
            # print(i["context"])
            title = i["title"]
            # print(title)
            id = i["id"]
            # print(title)
            lujing = e.xpath("//img[@alt]/@src")
            programaId = i["programaId"]
            proParentID = i["proParentID"]
            created = int(time.mktime(time.strptime(i["created"], '%Y-%m-%d %H:%M:%S'))) * 1000
            for j in lujing:
                print(j)
                if "documents" in j:
                    print(j)

                    conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
                    cur = conn.cursor()
                    SQL = 'insert into hjxx_home (title,url,id_id,programaId,created,proParentID,documentsurl,parentName1,proName2) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    cur.execute(SQL, (title, url,  id, programaId, created, proParentID, j,parentName1,proName2))
                    conn.commit()
                    print("写入成功")
                    cur.close()
                    conn.close()
                elif "http://www.encollege.cn/imageFile/hjxx/" in j:
                    res1 = requests.get(j,headers=headers)
                    if res1.status_code !=200:
                        conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
                        cur = conn.cursor()
                        SQL = 'insert into hjxx_home (title,url,id_id,programaId,created,proParentID,documentsurl,parentName1,proName2) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                        cur.execute(SQL, (title, url, id, programaId, created, proParentID, j, parentName1, proName2))
                        conn.commit()
                        print("写入成功")
                        cur.close()
                        conn.close()
                else:
                    continue



if __name__ == "__main__":
    parms_list = parms_list()
    # print(parms_list)
    get_res_and_save(parms_list)










                # firstnum = re.findall("/documents/(\d+)/(\d+)/",j)[0][0]
                # secondnum = re.findall("/documents/(\d+)/(\d+)/", j)[0][1]

                # if "t=" in j:
                    # t = j.split("?t=")[1]
                    # zuixinglujing = tupainlujing.format(parentName1, proName2, title, t)
                    # print(zuixinglujing)
                    # context = context.replace(j, zuixinglujing)

                # else:
                    # continue
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
        # SQL = 'insert into huanjingdatadeal1 (title,url,firstnum,secondnum,timeunix,id_id,programaId,created,proParentID,documentsurl,parentName1,proName2) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
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


# for i in url_list():
#     get_res(i)
# for i in eterxpth:
#     firstnum = i.split("/")[2]
#     secondenum = i.split("/")[3]
#     t = i.split("?t=")[1]
#     print(int(t))
#     date1 = getDate(int(t)/1000)
#     print(firstnum,secondenum,date1)
