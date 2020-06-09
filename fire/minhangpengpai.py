#-*-coding:utf-8-*-
import requests
import quopri
import time
from lxml import etree

from tools.sqlconn import firepool
header = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}
url = "https://search.cctv.com/search.php?qtext=%E9%97%B5%E8%A1%8C%E6%B6%88%E9%98%B2&sort=relevance&type=web&vtime=&datepid=1&channel=&page=1"
req = requests.get(url,headers=header)
etr = etree.HTML(req.text)
# print(req.text)
licon = etr.xpath('//*[@id="page_body"]/div[5]/div[1]/div[3]/div[3]/div[2]/div[1]/ul/li')
# print(licon)
for lc in licon:
    litit = lc.xpath('string(.//h3/span/a)')
    liconte = lc.xpath('normalize-space(string(.//p[@class="bre"]))')
    cont_url = lc.xpath('.//h3/span/@lanmu1')[0]
    rescon = requests.get(cont_url, headers=header)
    # print(rescon.text)
    cont = etree.HTML(rescon.text)
    # print(rescon.text)
    cont_full = cont.xpath('//div[@class="cnt_bd"]/p/text()')[2]
    # cont_full = quopri.decodestring(cont_full.encode("utf-8"))
    l = "消防员在炎热的天气下执行救火行动后"
    # print(quopri.encodestring(l))
    print(litit)
    print(liconte)
    print(cont_url)
    print(cont_full)
    time.sleep(100)
# def save_sql(text,img,nikename,wherefrom):
#     conn = firepool.connection()
#     cur = conn.cursor()
#     sql = 'insert into minhang (context,img,nikename,wherefrom) values (%s,%s,%s,%s)'
#     cur.execute(sql,(text,img,nikename,wherefrom))
#     conn.commit()
#     cur.close()
#     conn.close()
#     print("写入成功")
#
# for i in range(10,51):
#     url = "https://s.weibo.com/weibo/%E9%97%B5%E8%A1%8C%E6%B6%88%E9%98%B2?topnav=1&wvr=6&page={}".format(i)
#     wherefrom = "微博"
#     header = {
#             "cookie":"SINAGLOBAL=7571495670469.319.1587462306109; un=15988387706; ALF=1622596127; SSOLoginState=1591060128; SCF=AiQdz-vxwsVDDQIOIzvl9CgpPtt68F33VnsoEvN3-hdnoJPo2zg-oa1anG32cexlXLZreljTTZBujQe9hS7prRY.; SUB=_2A25z0dbwDeRhGeNJ6lEU-CrPzzmIHXVQp084rDV8PUNbmtANLXfRkW9NS-F5w3NrrRitC7scCKf8V2Gg_n-mr_1c; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhSZeTDAIy0ICs7ihMuGRBh5JpX5KzhUgL.Fo-NeKef1hB0Sh-2dJLoI7yTxHiPC-4eHntt; SUHB=0S7C7Z1ZJzeq1H; wvr=6; _s_tentry=login.sina.com.cn; UOR=www.51testing.com,widget.weibo.com,www.baidu.com; Apache=7097108010640.043.1591060130620; ULV=1591060130656:7:2:2:7097108010640.043.1591060130620:1591006242966; webim_unReadCount=%7B%22time%22%3A1591061159207%2C%22dm_pub_total%22%3A2%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A3%2C%22msgbox%22%3A0%7D; WBStorage=42212210b087ca50|undefined",
#             "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
#         }
#     res = requests.get(url,headers=header)
#     etree1 = etree.HTML(res.text)
#     allcontent = etree1.xpath('//*[@id="pl_feedlist_index"]/div[1]/div/div/div[1]/div[2]')
#     # print(content)
#     for con in allcontent:
#         conhtml = etree.tostring(con, encoding="utf-8", method='html').decode("utf-8")
#         # print(con)
#         nikename = con.xpath('./p[@node-type="feed_list_content"]/@nick-name')
#         nikename = nikename[0] if nikename else None
#         print(nikename)
#         #获取文字内容
#         if "feed_list_forwardContent" in conhtml:
#             if "feed_list_content_full" in conhtml:
#                 content_full = con.xpath('normalize-space(string(.//p[@node-type="feed_list_content_full"]))')
#                 # print(content_full)
#             else:
#                 content_full = con.xpath('normalize-space(string(.//p[@node-type="feed_list_content"]))')
#                 # print(content_full)
#         else:
#             if "feed_list_content_full" in conhtml:
#                 content_full = con.xpath('normalize-space(string(.//p[@node-type="feed_list_content_full"]))')
#                 # print(content_full)
#             else:
#                 content_full = con.xpath('normalize-space(string(.//p[@node-type="feed_list_content"]))')
#                 # print(content_full)
#         print(content_full)
#         #获取图片内容
#         imgli = con.xpath('.//ul/li/img/@src')
#         imgli = 'https:{}'.format(",https:".join(imgli)) if imgli else None
#         print(imgli)
#         save_sql(content_full,imgli,nikename,wherefrom)
#         #
#         time.sleep(2)





    # print(nikename)
    # time.sleep(100)

# print(content)
# contenthtml = etree.tostring(content,encoding="utf-8", method='html').decode("utf-8")
# print(contenthtml)
# # for i in content:
# nickname = content.xpath('string(//*[@node-type="feed_list_content_full"])')
# feed_list_content = content.xpath('normalize-space(string(//*[@node-type="feed_list_content_full"]))')
# print(feed_list_content)
#
# urlshi = "https://f.video.weibocdn.com/003HaipIlx07w6PltPgc01041200u3Na0E010.mp4?label=mp4_ld&template=640x360.24.0&trans_finger=78679548d3dda0964ec12b81fbdd99c2&Expires=1591070497&ssig=YhuST%2BzVl%2F&KID=unistore,video"
# res1 = requests.get(urlshi,stream=True)
#
# with open('chenyuqi.mp4', "wb") as mp4:
#     for chunk in res1.iter_content(chunk_size=1024 * 1024):#当流下载时，用Response.iter_content或许更方便些。requests.get(url)默认是下载在内存中的，下载完成才存到硬盘上，可以用Response.iter_content　来边下载边存硬盘
#         if chunk:
#             mp4.write(chunk)

# print(res1.text)

