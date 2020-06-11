import requests
import json
import time
import random

from tools.sqlconn import pool_pudongaiofang


def get_jcj_ajxx_info():
    conn = pool_pudongaiofang.connection()
    cur = conn.cursor()
    # sql = 'SELECT ja.ID as caseId,ja.AFDZ as address,ja.lasj as startTime,ja.ZYQK as description,rscr.word as word from jcj_ajxx ja LEFT JOIN rule_semantic_case_result rscr on ja.ID = rscr.caseId where  rscr.wordId=203 and rscr.ruleId=1500'
    sql = 'SELECT * FROM jcj_ajxx_copy1 where id_id>38887'
    cur.execute(sql)
    info = cur.fetchall()
    return info



def get_access_token():
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}"

    APIKey = "rPNhLSyCBoFnzI6gVvuTdFXG"

    SecretKey = "CcCUAE0jVuf2MycsFuCt13EGULI8c0iz"
    url = url.format(APIKey,SecretKey)
    access_token = requests.get(url).json()["access_token"]
    return access_token

def get_participle_info(text,access_token):
    header = {
        "Content-Type":"application/json",
    }
    url1 = "https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer?charset=UTF-8&access_token={}".format(access_token)
    body = {
        "text":text
    }
    word = requests.post(url1,headers=header,data=json.dumps(body))
    return word.json()

def save_participle(par_info_item,par_info_text):
    text = par_info_text
    loc_details = ",".join(par_info_item["loc_details"])
    uri = par_info_item["uri"]
    pos = par_info_item["pos"]
    ne=par_info_item["ne"]
    item=par_info_item["item"]
    item_index = par_info_text.index(item)
    basic_words=",".join(par_info_item["basic_words"])
    byte_length=par_info_item["byte_length"]
    formal=par_info_item["formal"]
    # print(type(text),type(loc_details),type(uri),type(pos),type(ne),type(item),type(basic_words),type(byte_length),type(formal))
    if pos != "w":
        conn = pool_pudongaiofang.connection()
        cur = conn.cursor()
        sql = 'insert into participle_copy1 (text,loc_details,uri,pos,ne,item,basic_words,byte_length,formal,item_index) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur.execute(sql,(text,loc_details,uri,pos,ne,item,basic_words,byte_length,formal,item_index))
        conn.commit()
        print("插入成功")
    else:
        pass

# print(type(get_jcj_ajxx_info()))
info = get_jcj_ajxx_info()
access_token = get_access_token()
for i in info:
    # print(i["id"])
    # print(i["ZYQK"])
    if i["ZYQK"]:
        print(i["ZYQK"])
        print(i["id_id"])
    # if i["description"] !=None:
        par_info = get_participle_info(i["ZYQK"],access_token)
        randomtime = random.randint(1,3)
        time.sleep(randomtime)
        # print(par_info)
        par_info_text = par_info["text"]
        par_info_items = par_info["items"]
        for i in par_info_items:
            save_participle(i,par_info_text)
    else:
        continue

    # print(i["ZYQK"])

# print(get_jcj_ajxx_info())