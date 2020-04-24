import requests
from lxml import etree
import time
import json
import random
import base64
from fontTools.ttLib import TTFont
import re
import io
from io import BytesIO
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'upgrade-insecure-requests': '1',
    'cookie': 'aQQ_ajkguid=09A0859E-56ED-A4F5-FE95-0F8ABAFBC4AC; wmda_uuid=4a0dbfab14068b19e566debfe70c2dcf; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; 58tj_uuid=73c0cdaa-d302-4b2c-8cf4-1c62d8b6659f; als=0; _ga=GA1.2.96530944.1578966491; propertys=whnmwe-q44kyx_; wmda_uuid=886d70f232fee67c4427552d29fd05b0; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; _gid=GA1.2.1145441305.1579170985; ctid=25; new_uv=6; __xsptplus8=8.6.1579179711.1579179711.1%232%7Csp0.baidu.com%7C%7C%7C%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%25E7%25A7%259F%25E6%2588%25BF%7C%23%23x7AYCEBQRu_RcWofOkvpyL6hkXr4q-wj%23; lps=https%3A%2F%2Fwx.zu.anjuke.com%2F%3Fkw%3D%26k_comm_id%3D%7C; sessid=A809ED45-A40B-7AED-79EB-65E8A3A8064B; twe=2; xzfzqtoken=HQXI0TTk9WZoEbRIsTyBzfB9NK2frYrNrG5pZ1%2FeRDs4Qn3%2FgmY%2FWdnPyFuuP2j2in35brBb%2F%2FeSODvMgkQULA%3D%3D; wmda_session_id_6289197098934=1579222230577-99a50c37-d268-5a72'
    }
name = input('请输入地区：')

#   加密数字解析，返回加密数字
def covert_secret_int(yuanma, base64_str):
    # base64解析转换成二进制  下载到本地ttf文件
    ttf = base64.decodebytes(base64_str.encode())
    #   BytesIO把一个二进制文件当成文件来操作
    zufangFont = TTFont(io.BytesIO(ttf))

    zufangFont.save('58zufang2.ttf')
    zufangFont.saveXML('58zufang2.xml')
    # print(zufangFont.keys())
    # 获取对应关系
    List = zufangFont['cmap'].tables[0].ttFont.getGlyphOrder()
    Listkey = zufangFont['cmap'].tables[0].ttFont.tables['cmap'].tables[0].cmap
    # print(List)
    # print(Listkey)

    Table = {}
    for key, value in Listkey.items():
        # print(hex(key))
        # Table[str(hex(key))[2:].lower()] = str(int(value.replace("glyph0000", "").replace("glyph000", ""))-1)
        Table[key] = str(int(value.replace("glyph0000", "").replace("glyph000", "")) - 1)
    # print("Table: ", Table)
    real_num = Table.get(yuanma)
    return real_num

#将字符串中含有加密数字转换成正常数字并返回
def get_result(yuan_str, base64_str):
    yuanma = ""
    for y_index in range(len(yuan_str)):
        num = covert_secret_int(ord(yuan_str[y_index]), base64_str)
        if num is None:
            yuanma += yuan_str[y_index]
        else:
            yuanma += num
    return yuanma
def parse(url_):
    response = requests.get(url_,headers=headers)
    response.encoding='utf-8'
    return etree.HTML(response.text)
def parse_detail(list_url):
    selector = parse(list_url)
    time.sleep(random.randint(0,1))     #0~1秒爬取一次
    all_list = selector.xpath('//*[@class="zu-itemmod"]')       #当页中全部数据列表
    for sel in all_list:
        url_a = sel.xpath('div[1]/h3/a/@href')[0]       #获取到每一页的URL
        parse_id_detail(url_a)


#爬取每一页中的详细内容
def parse_id_detail(url_a):
    alls = requests.get(url_a,headers=headers)
    alls.encoding='utf-8'
    selector = etree.HTML(alls.text)
    time.sleep(random.randint(0,1))     #0~1秒爬取一次

    # 匹配ttf font
    cmp = re.findall(r";src:url\('(data.*)'\)\sformat\('truetype'\)", alls.text)
    # print("cmp:", cmp)
    try:    #   遇错时分析错误情况，程序继续运行
        base64_str = cmp[0][cmp[0].index('base64,') + 7:]
        # print(base64_str)
        items=[]
        item = {}
        # 房间价格
        price = selector.xpath('string(//*[@class="house-info-zufang cf"]/li[1]/span)')
        price = get_result(price,base64_str)    #调用上方函数解析
        # 房间类型
        type = selector.xpath('string(//*[@class="house-info-zufang cf"]/li[2]/span[2])')
        type = get_result(type,base64_str)  #调用上方函数解析
        # 面积大小
        mianji = selector.xpath('string(//*[@class="house-info-zufang cf"]/li[3]/span[2])')
        mianji = get_result(mianji,base64_str)  #调用上方函数解析
        # 房间朝向
        chaoxiang = selector.xpath('string(//*[@class="house-info-zufang cf"]/li[4]/span[2])')
        #  楼层
        height = selector.xpath('string(//*[@class="house-info-zufang cf"]/li[5]/span[2])')
        #   装修
        zhuangxiu = selector.xpath('string(//*[@class="house-info-zufang cf"]/li[6]/span[2])')
        #   类型
        leixing= selector.xpath('string(//*[@class="house-info-zufang cf"]/li[7]/span[2])')
        #   小区
        place= selector.xpath('string(//*[@class="house-info-zufang cf"]/li[8]/a)')
        places ='无锡'    #   页面中没有标明哪个市，那个憨批非要要没办法自己添一个哈哈，爬哪个市名字改一下就好哦
        #   所属地区
        diqu = selector.xpath('//*[@class="house-info-zufang cf"]/li[8]/a[2]/text()')[0]
        #   要求（男女不限）
        yaoqiu= selector.xpath('string(//*[@class="house-info-zufang cf"]/li[9]/span[2])')
        #   房间编号
        try:    #   因为有些房间数据缺失时会发生报错，给一个try遇到数据缺失使其等于空值‘’
            bianma= selector.xpath('//*[@class="right-info"]/span/text()')[0]
        except:
            bianma=''
        #   发布时间
        try:
            times= selector.xpath('//*[@class="right-info"]/b/text()')[0]
        except:
            times = ''
        times = get_result(times,base64_str)    #调用上方函数解析

        #放进item里面打包保存时有头名
        item['price']=price
        item['type']=type
        item['mianji'] = mianji
        item['chaoxiang'] = chaoxiang
        item['height'] = height
        item['zhuangxiu'] = zhuangxiu
        item['leixing'] = leixing
        item['place'] = place
        item['places'] = places
        item['diqu'] = diqu
        item['yaoqiu'] = yaoqiu
        item['bianma'] = bianma
        item['times'] = times
        items.append(item)
        #   将数据已json数据存储
        with open('all.json','a',encoding='utf-8')as fp:
            fp.write(json.dumps(item,ensure_ascii=False)+",\n")
        print(price,type,mianji,chaoxiang,height,zhuangxiu,leixing,place,places,diqu,yaoqiu,bianma,times)
    except Exception as e:
        print("异常原因：",e)  #输出出错情况
#   全部的URL放入列表中用for循环出全部的URL
url_lists = 'https://'+name+'.zu.anjuke.com/fangyuan/p'
all_url = [url_lists + str(i) for i in range(1,50)]
for url in all_url:
    parse_detail(url)
