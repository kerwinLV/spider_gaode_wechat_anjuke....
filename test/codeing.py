# import codecs
# with open("javatest.java",encoding="utf-8") as f:
#     # print(f.read())
#     g =f.read()
#     # print(g)
#
# reader = codecs.getreader('gbk')(g)
# # print(reader)
# # data = reader.read(10)
# print(dir(reader))
# print(reader)
#
# l = "价格世界各国"
# print(l.encode("utf-8"))

import requests
from lxml import etree
import re
import time
import urllib3
url = "https://www.encollege.cn/gwapi/article/find?total=828&programaId=32&page=5"
# res = requests.get(url).json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
    }
print("res")
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
            # print(j)
            print(j)
            rescode = requests.get(j, headers=headers,verify=False)
            rescode1 = rescode.status_code
            # print(rescode1)
            # print(j)
            if rescode1 != 200:
                t = re.findall("/(\d+).jpg",j)
                if t:
                    t = t[0]
                else:
                    t = ""

                # conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
                # cur = conn.cursor()
                # SQL = 'insert into code_err_huanjin (title,url,timeunix,id_id,programaId,created,proParentID,documentsurl,proName2,parentName1) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                # cur.execute(SQL, (title, url, t, id, programaId, created, proParentID, j, proName2, parentName1))
                # conn.commit()
                # print("写入成功")
                # cur.close()
                # conn.close()
            else:
                continue