# coding=utf-8
# @Time    : 2020/6/16 10:33
# @Author  : kerwin
# @File    : seleniumtest.py

import time
import datetime
import re
from selenium import webdriver
from lxml import etree
from zhon.hanzi import punctuation
# from requests.cookies import RequestsCookieJar
import requests
from tools.sqlconn import shanghaiyingjipool

class COOKIE(object):
    url = 'https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt='
    def __init__(self):
        self.browser = webdriver.Chrome()
    def getcookie(self):
        self.browser.get(self.url)
        self.browser.implicitly_wait(15)
        self.browser.find_element_by_xpath('//*[@id="loginName"]').clear()
        self.browser.find_element_by_xpath('//*[@id="loginName"]').send_keys('15988387706')
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="loginPassword"]').clear()
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="loginPassword"]').send_keys('lyt0105@')
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="loginAction"]').click()
        time.sleep(7)
        # cookie_dic={}
        cookies = self.browser.get_cookies()
        self.browser.close()
        # print(cookies)
        cookiestr = ""
        # jar = RequestsCookieJar()
        for cookie in cookies:
            if "name" in cookie.keys() and "value" in cookie.keys():
                cookiestr = cookiestr + cookie["name"]+"="+cookie["value"]+"; "
        # print(cookiestr)
                # jar.set(cookie["name"],cookie["value"])
                # cookie_dic[cookie["name"].encode('utf-8')]=cookie["value"].encode('utf-8')
        # print(jar)
        # print(cookie_dic)


        return cookiestr


def get_msnage(cookiestr,url1):
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
                "Cookie":cookiestr,
    }
    re1 = requests.get(url1,headers=headers)
    # re1.encoding = "utf-8"
    etem = etree.HTML(re1.text.replace('<?xml version="1.0" encoding="UTF-8"?>',''))
    context = etem.xpath('//div[starts-with(@id, "M_")]')
    # print(context)
    for con in context:
        msg = con.xpath('string(./div/span[@class="ctt"])').replace(":","")
        ct = con.xpath('string(./div/span[@class="ct"])')
        ct = ct.encode("gbk", "ignore").decode("gbk", "ignore")
        ct = ct.split("来自")[0]
        print(ct)
        if "年" not in ct and "-" not in ct and "今" not in ct:
            year1 = datetime.datetime.now().year
            ct = (str(year1)+"年"+ct).replace("年","-").replace("月","-").replace("日","")
            # ct = ct.encode("gbk", "ignore").decode("gbk", "ignore")
            # print(ct)
        elif "今天" in ct:
            totime = datetime.date.today()
            ct = ct.replace("今天",totime.strftime("%Y-%m-%d"))
            # ct = ct.encode("gbk","ignore").decode("gbk","ignore")
            # print(ct)
        nikename = con.xpath('./div/a[1]/text()')[0]
        wherefrom = "新浪微博"
        ctlen = len(ct.split(":"))
        if ctlen==2:
            ct = int(time.mktime(time.strptime(ct, '%Y-%m-%d %H:%M')))
        else:
            ct = int(time.mktime(time.strptime(ct, '%Y-%m-%d %H:%M:%S')))
        release_time = ct
        # msg = re.sub(r"[%s]+" % punctuation, "", msg.decode("utf-8"))
        # print(msg.encode("gbk","ignore").decode("gbk","ignore"))
        storage_time =int(time.time())
        # print(ct)
        # print(nikename)
        save_sql(msg,nikename,wherefrom,release_time,storage_time)


def save_sql(text,img,nikename,wherefrom,t_time):
    conn = shanghaiyingjipool.connection()
    cur = conn.cursor()
    sql = 'insert into anqing_xiaofang_a (context,nikename,wherefrom,release_time,storage_time) values (%s,%s,%s,%s,%s)'
    cur.execute(sql,(text,img,nikename,wherefrom,t_time))
    conn.commit()
    cur.close()
    conn.close()
    print("写入成功")

if __name__=="__main__":
    co = COOKIE()
    # co.getcookie()
    cookiestr = co.getcookie()

    url1 = "https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%E7%81%AB%E7%81%BE&advancedfilter=1&nick=%E5%A4%AE%E8%A7%86%E6%96%B0%E9%97%BB&endtime=20200616&sort=time&page={}"
    for i in range(6,90):
        print(i)
        url2 = url1.format(i)
        print(url2)
        get_msnage(cookiestr,url2)
        time.sleep(2)

    # print(re1.text.encode("gbk","ignore").decode("gbk","ignore"))