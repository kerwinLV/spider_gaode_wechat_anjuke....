import requests
from lxml import etree
from tools.sqlconn import pool
url = "https://lbs.qq.com/service/webService/webServiceGuide/webServiceAppendix"
headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}
res = requests.get(url,headers = headers)

etreepoi = etree.HTML(res.text)
poilist = etreepoi.xpath('//*[@id="__layout"]/div/div[2]/div/div[2]/div/div/article/div/div/table/tbody/tr/td[3]/text()')
print(poilist)
for i in poilist:
    conn2 = pool.connection()
    cur2 = conn2.cursor()
    # print(id, i[3], i[4])
    sql1 = 'insert into tenxun_poi (poi) values ("%s")'
    cur2.execute(sql1 % (i))
    conn2.commit()
    print("提交成功")
    # print(i[0],i[3],i[1])
    cur2.close()
    conn2.close()
# print(etreepoi)