import requests
import time
from lxml import etree

from tools.sqlconn import firepool


def save_sql(text,img,nikename,wherefrom,t_time):
    conn = firepool.connection()
    cur = conn.cursor()
    sql = 'insert into anqing_xiaofang_copy1 (context,img,nikename,wherefrom,t_time) values (%s,%s,%s,%s,%s)'
    cur.execute(sql,(text,img,nikename,wherefrom,t_time))
    conn.commit()
    cur.close()
    conn.close()
    print("写入成功")

for i in range(1,47):
    url = "https://s.weibo.com/weibo?q=%E7%81%AB%E7%81%BE%20%E5%A4%AE%E8%A7%86%E6%96%B0%E9%97%BB&Refer=SWeibo_box&page={}".format(i)
    wherefrom = "微博"
    header = {
            "cookie":"SINAGLOBAL=7571495670469.319.1587462306109; un=15988387706; SSOLoginState=1591060128; wvr=6; _s_tentry=login.sina.com.cn; UOR=www.51testing.com,widget.weibo.com,www.baidu.com; Apache=7097108010640.043.1591060130620; ULV=1591060130656:7:2:2:7097108010640.043.1591060130620:1591006242966; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhSZeTDAIy0ICs7ihMuGRBh5JpX5KMhUgL.Fo-NeKef1hB0Sh-2dJLoI7yTxHiPC-4eHntt; ALF=1622783648; SCF=AiQdz-vxwsVDDQIOIzvl9CgpPtt68F33VnsoEvN3-hdnn_rcefyNKpT3ldioRuzMnR-FxgTYWcHVIgG2h2K6wCE.; SUB=_2A25z3PNxDeRhGeNJ6lEU-CrPzzmIHXVQqGO5rDV8PUNbmtANLRjFkW9NS-F5wzktu0tChfD7jZcEbhlnov9kDqYD; SUHB=0WGcrn5A6V0i83; WBStorage=42212210b087ca50|undefined",
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
        }
    res = requests.get(url,headers=header)
    etree1 = etree.HTML(res.text)
    allcontent = etree1.xpath('//*[@id="pl_feedlist_index"]/div[1]/div/div/div[1]/div[2]')
    # print(content)
    for con in allcontent:
        conhtml = etree.tostring(con, encoding="utf-8", method='html').decode("utf-8")
        # print(con)
        nikename = con.xpath('./p[@node-type="feed_list_content"]/@nick-name')
        nikename = nikename[0] if nikename else None
        print(nikename)
        #获取文字内容
        if "feed_list_forwardContent" in conhtml:
            if "feed_list_content_full" in conhtml:
                content_full = con.xpath('normalize-space(string(.//p[@node-type="feed_list_content_full"]))')
                # print(content_full)
            else:
                content_full = con.xpath('normalize-space(string(.//p[@node-type="feed_list_content"]))')
                # print(content_full)
        else:
            if "feed_list_content_full" in conhtml:
                content_full = con.xpath('normalize-space(string(.//p[@node-type="feed_list_content_full"]))')
                # print(content_full)
            else:
                content_full = con.xpath('normalize-space(string(.//p[@node-type="feed_list_content"]))')
                # print(content_full)
        print(content_full)
        if "死" in content_full or "火灾" in content_full:
        #获取图片内容
            imgli = con.xpath('.//ul/li/img/@src')
            imgli = 'https:{}'.format(",https:".join(imgli)) if imgli else None
            t_time = con.xpath('normalize-space(.//p[@class="from"]/a/text())')
            print(t_time)
            print(imgli)
            save_sql(content_full,imgli,nikename,wherefrom,t_time)

        #
        time.sleep(2)





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

