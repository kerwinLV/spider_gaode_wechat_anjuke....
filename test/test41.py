import requests
from lxml import etree
import time
# from test.test42 import url_list
def url_list():
    url = "https://www.encollege.cn/gwapi/article/find?total=23&programaId=%d&page=%d"
    # url1 = ["https://www.encollege.cn/gwapi/article/find?total=42&programaId=26&page=2"]

    url_list = []
    for i in range(1,5):
        for j in range(1,3):
            url_list.append(url%(20+i,j))
            # print(url%(20+i,j))
    return url_list


# url = "https://www.encollege.cn/gwapi/article/find?total=23&programaId=24&page=1"
def get_res(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
    }

    res = requests.get(url,headers=headers).json()
    items = res["data"]["items"]
    for i in items:
        e = etree.HTML(i["context"])
        # print(i["context"])
        print(i["title"])
        print(e.xpath("//img[@alt]/@src"))

    # time.sleep(2)
# print(res["data"]["items"])
# eter = etree.HTML(res.text)
# eterxpth = eter.xpath("//img[@alt]/@src")
# print(eterxpth)


def getDate(times):
    # print(times)
    timearr = time.localtime(times)
    date = time.strftime("%Y-%m-%d", timearr)
    return date

for i in url_list():
    print(i)
# for i in eterxpth:
#     firstnum = i.split("/")[2]
#     secondenum = i.split("/")[3]
#     t = i.split("?t=")[1]
#     print(int(t))
#     date1 = getDate(int(t)/1000)
#     print(firstnum,secondenum,date1)