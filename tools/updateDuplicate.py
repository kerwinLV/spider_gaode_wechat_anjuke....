from tools.sqlconn import pool1
import requests
import json

def get_data():
    conn = pool1.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
    cur = conn.cursor()
    SQL = 'SELECT id,title FROM huanjingdatadeal2 WHERE documentsurl NOT LIKE "%t=%"'
    cur.execute(SQL)
    # conn.commit()
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data



def update_data(data):
    for a in data:
        title = a["title"]
        url = "https://www.encollege.cn/gwapi/article/findArticleByTitle"
        headers = {"Content-Type": "application/json"}
        data = {"title":title,"total":0,"size":20,"page":1}
        res = requests.post(url,headers = headers,data=json.dumps(data)).json()
        items = res["data"]["items"]
        # print(len(items))
        for i in items:
            # j = 0
            # j+=1

            # print(i["context"])
            context = i["context"]
            if "http://www.encollege.cn/imageFile" in context:
                print(i["id"])
                context1 = context
                break
            else:
                context1 = None
                continue
        for j in items:
            if context1:
                headers = {"Content-Type": "application/json"}
                data1 = {
                    "id":j["id"],
                    "context":context1
                }
                # https://www.encollege.cn/gwapi/article/find?programaId=36&temp=1
                updateurl = "https://www.encollege.cn/gwapi/article/updateContent"
                res5 = requests.post(updateurl,headers = headers,data=json.dumps(data1))
                print(res5.text)
            else:
                print(j["id"])
                print("这三篇都不存在")
            # print("-----------------------------------------------------------------------------")

# print(get_data())
data = get_data()
update_data(data)