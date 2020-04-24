# encoding=utf-8
# date: 2019/5/15
# __author__ = "Masako"

import re
import json
import time
import html
import requests

from Elise.crawler import Crawler

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class GZHSpider:

    def __init__(self):
        self.biz = ""
        self.uin = ""
        self.key = ""
        self.pass_ticket = ""
        self.proxies = {}
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1295.400 QQBrowser/9.0.2524.400'
                          ' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat',
        }

    def get_art_list(self, offset=0, pagesize=10):
        """
        获取文章列表
        所需参数是调用时的变量，其他参数可以固定，在初始化时设置
        :param offset: int, 偏移量，相当于页码, 可由上一页的位置得到
        :param pagesize: int, 每页条数，默认为10
        :return: 访问到的json数据
        """
        url = "https://mp.weixin.qq.com/mp/profile_ext"
        result = {}
        # offset = page * pagesize
        params = {
            "action": "getmsg",
            "__biz": self.biz,
            "f": "json",
            "offset": offset,
            "count": pagesize,
            "is_ok": 1,
            "scene": '38',
            "uin": self.uin,
            "key": self.key,
            "pass_ticket": self.pass_ticket,
            "wxtoken": "",
        }
        try:
            response = requests.get(url, params=params, headers=self.headers, proxies=self.proxies, verify=False)
        except Exception as e:
            result['code'] = 1
            result['msg'] = str(e)
            return result

        try:
            data = json.loads(response.text)
            data['code'] = 0
            return data
        except json.decoder.JSONDecodeError as e:
            result['code'] = 2
            result['msg'] = str(e)
            return result

    def get_art_page(self, art_url):
        """
        从文章页面获取采集阅读量需要的数据
        :param art_url: str, 文章链接
        :return:
        """
        result = {}
        try:
            response = requests.get(art_url, headers=self.headers, proxies=self.proxies, verify=False)
            # print(response.text)
        except Exception as e:
            result['code'] = 1
            result['msg'] = str(e)
            return result

        # 处理文章错误
        try:
            if '访问过于频繁' in response.text:  # 访问频繁，需换ip
                result['code'] = 4
                result['msg'] = "ip banned"
                return result
            if '无法查看' in response.text:  # 无法查看，被删除或者被违规被举报
                result['code'] = 5
                result['msg'] = "content violation"
                return result
            data = self.parse_art_page(response.text)
        except Exception as e:  # 其他错误导致解析失败
            result['code'] = 2
            result['msg'] = str(e)
            return result

        result['data'] = data
        result['code'] = 0
        return result

    @staticmethod
    def parse_art_page(content):
        """
        解析文章 html
        :param content: 文章页面的html, 字符串
        :return:
        """
        def get_value(s, name):
            value_str = re.findall('var %s = (.*?);' % name, s)[0]
            patten = re.compile('"(.*?)"')
            r_list = re.findall(patten, value_str)
            for i in r_list:
                if i:
                    return i
            else:
                return ''

        # 直接正则获取了
        appmsg_type = re.findall('appmsg_type = "(\d+)"', content)[0]
        msg_title = re.findall('msg_title = "(.*?)"', content)[0]
        req_id = re.findall("req_id = '(.*?)'", content)[0]
        comment_id = re.findall('comment_id = "(.*?)"', content)[0]

        mid = get_value(content, 'mid')
        sn = get_value(content, 'sn')
        idx = get_value(content, 'idx')
        scene = re.findall('var source = "(.*?)"', content)[0]
        publish_time = re.findall('var publish_time = "(.*?)"', content)[0]

        appmsg_like_type = re.findall('appmsg_like_type = "(.*?)"', content)[0]

        params = {
            "appmsg_type": appmsg_type,
            "msg_title": msg_title,
            "publish_time": publish_time,
            "mid": mid,
            "sn": sn,
            "idx": idx,
            "scene": scene,
            "req_id": req_id,
            "comment_id": comment_id,
            "appmsg_like_type": appmsg_like_type,
        }
        return params

    def get_art_about(self, params_data):
        """
        获取阅读量点赞数等相关信息
        :param params_data: dict, 需要的参数
        :return:
        """
        url = "https://mp.weixin.qq.com/mp/getappmsgext"
        result = {}
        # offset = page * pagesize
        params = {
            "mock": "",
            "f": "json",
            "uin": self.uin,
            "key": self.key,
            "pass_ticket": self.pass_ticket,
            "wxtoken": "777",
            "devicetype": "Windows%26nbsp%3B10",
            # "appmsg_token": appmsg_token,
        }
        t = int(time.time())
        # title = requests.utils.quote(title)
        data = {
            # "r": "0.48046619608066976",
            "__biz": self.biz,
            "appmsg_type": "9",  # 复制下来的值，会被覆盖掉
            "mid": "",
            "sn": "",
            "idx": "1",
            "scene": "",
            "title": "",   # 为空，后面覆盖
            "ct": t,
            "abtest_cookie": "",
            "devicetype": "Windows+10",
            "version": "62060728",
            "is_need_ticket": "0",
            "is_need_ad": "0",
            "comment_id": "",
            "is_need_reward": "1",
            "both_ad": "0",
            "send_time": "",
            "msg_daily_idx": "1",
            "is_original": "0",
            "is_only_read": "1",
            "pass_ticket": self.pass_ticket,  # 也可以写死
            "is_temp_url": "0",
            "item_show_type": "0",
            "tmp_version": "1",
            "more_read_type": "0",
            "appmsg_like_type": "2"
        }
        if isinstance(params_data, dict):   # 将传进来的参数和一些写死的参数合并到一个字典
            data.update(params_data)
        headers = {
            # 'CSP': "active",
            'Host': 'mp.weixin.qq.com',
            # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://mp.weixin.qq.com',
            'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1295.400 QQBrowser/9.0.2524.400'
                          ' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat',
        }
        try:
            response = requests.post(url, params=params, data=data, headers=headers, proxies=self.proxies, verify=False)
        except Exception as e:
            result['code'] = 1
            result['msg'] = str(e)
            return result

        try:
            data = json.loads(response.text)
            appmsgstat = data.get('appmsgstat')
            if appmsgstat:
                result['code'] = 0
                result['data'] = data
                return result
            # {'base_resp': {'ret': 302, 'errmsg': 'default'}}
            resp = data.get('base_resp', {})
            ret = resp.get('ret')
            if ret == 302:
                result['code'] = 0  # 先存下来再说
                result['data'] = data
                return result
        except json.decoder.JSONDecodeError as e:
            result['code'] = 2
            result['msg'] = str(e)
            return result

        result['code'] = 3  # 表示登录信息过期
        result['data'] = data
        return result

    def get_art_by_url(self, art_url):
        """
        整合一下获取阅读量的过程
        :param art_url: str， 文章链接
        :return:
        """
        r_0 = self.get_art_page(art_url)
        code = r_0.get('code')
        if code != 0:
            return r_0
        data = r_0.get('data', {})
        r_1 = self.get_art_about(data)
        code = r_1.get('code')
        if code != 0:
            return r_1
        result = r_1
        result['data']['pre_info'] = data
        # 记录采集时间
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        result['data']['c_time'] = t
        return result


class GZHCrawler(Crawler):
    def __init__(self, spider):
        Crawler.__init__(self, spider)

    def _stop(self):
        # self.input_que.clear()
        self.input_que.unfinished_tasks = 0  # 清空队列的计数器

    def crawl_list(self):
        while True:
            try:
                offset = self.input_que.get()
                print(offset)  #  打印页码，可以直观看到进度
            except Exception as e:
                time.sleep(1)
                continue

            ret = self.spider.get_art_list(offset=offset)
            code = ret.get('code')
            if code != 0:
                self.input_que.put(offset)
                self.input_que.task_done()
                continue

            status = ret.get('ret')
            if status == -3:  # cookie过期
                print(offset)
                print(ret)

            data_list_str = ret.get('general_msg_list')
            try:
                data = json.loads(data_list_str)
            except Exception as e:
                self.input_que.task_done()
                continue

            art_list = data.get('list')
            for a in art_list:
                # self.out_que.put(a)
                data_info = a.get('app_msg_ext_info', {})
                title = data_info.get('title', '')
                digest = data_info.get('digest', '')
                content_url = data_info.get('content_url', '')
                content_url = html.unescape(content_url)
                fileid = data_info.get('fileid', '')
                author = data_info.get('author', '')
                d = {
                    "title": title,
                    "digest": digest,
                    "content_url": content_url,
                    "fileid": fileid,
                    "author": author,
                    "head": 1
                }
                # print(d)  # 打印结果看看
                if fileid:
                    self.out_que.put(d)
                multi_app_msg_item_list = data_info.get('multi_app_msg_item_list', [])
                for i in multi_app_msg_item_list:
                    title = i.get('title', '')
                    digest = i.get('digest', '')
                    content_url = i.get('content_url', '')
                    content_url = html.unescape(content_url)
                    fileid = i.get('fileid', '')
                    author = i.get('author', '')
                    if fileid:
                        d = {
                            "title": title,
                            "digest": digest,
                            "content_url": content_url,
                            "fileid": fileid,
                            "author": author,
                            "head": 0
                        }
                        self.out_que.put(d)

            is_not_end = ret.get("can_msg_continue", 0)
            next_page = ret.get("next_offset")
            if is_not_end:
                self.input_que.put(next_page)

            self.input_que.task_done()
            time.sleep(5)

    def crawl(self):
        while True:
            try:
                params = self.input_que.get(timeout=0.2)
                print(params)
            except Exception as e:
                time.sleep(1)
                continue

            url = params.get('content_url', '')
            result_data = self.spider.get_art_by_url(url)
            data = result_data.get('data', {})
            code = result_data.get('code')
            if code == 3:  # 登录信息错误，就退出
                # self.input_que.task_done()
                self._stop()
            if code == 4 or code == 5:  # ip被封禁; 内容违规, 就丢弃
                self.input_que.task_done()
                continue
            if code != 0:  # 其他错误重新采集
                self.input_que.put(params)
                self.input_que.task_done()
                continue

            if data:
                data.update(params)
                self.out_que.put(data)
            self.input_que.task_done()
            time.sleep(3)


def test_spider():
    spider = GZHSpider()
    spider.biz = 'MzI4MTU2NjE3NQ=='  # 公众号id

    spider.uin = 'MTE5NTMwMzg1MQ=='  # 微信号id
    spider.key = 'c002f5f6596d8e8dfc78204c7ca39bc6e0a5906fd38d1b8aed1b939346650dbe6e20290d65' \
            'b4e9d48bc5693148cc20e298d62868f9c7c85b8b6a3e9af3859a8d7ddc93d74f7dadcfb9fb7b785539ffc1'
    spider.pass_ticket = '4SNkMivOQM6F5MP9wCFOxFdwgdKrKuYC7VOyvMvoI+Eqn5bt2Lijf6LRzyF1U6pi'

    result_1 = spider.get_art_list()
    # 打印获取到的列表
    print(json.dumps(result_1))
    general_msg_list = result_1.get('general_msg_list', {})
    data_list_json = json.loads(general_msg_list)
    art_list = data_list_json.get('list')
    for article in art_list:
        data_info = article.get('app_msg_ext_info', {})
        content_url = data_info.get('content_url', '')
        content_url = html.unescape(content_url)
        print(content_url)
        result_2 = spider.get_art_by_url(content_url)
        # 打印一下获取到的文章信息
        print(json.dumps(result_2))
        break


def test_crawler():
    s = GZHSpider()
    s.biz = 'MzI4MTU2NjE3NQ=='  # 公众号id
    s.uin = 'MTE5NTMwMzg1MQ=='  # 微信号id
    s.key = 'c002f5f6596d8e8dfc78204c7ca39bc6e0a5906fd38d1b8aed1b939346650dbe6e20290d65' \
            'b4e9d48bc5693148cc20e298d62868f9c7c85b8b6a3e9af3859a8d7ddc93d74f7dadcfb9fb7b785539ffc1'
    s.pass_ticket = '4SNkMivOQM6F5MP9wCFOxFdwgdKrKuYC7VOyvMvoI+Eqn5bt2Lijf6LRzyF1U6pi'
    s.proxies = {   # 设置ip代理
        'https': '218.86.87.171:53281'
    }

    # 采集文章列表
    crawler = GZHCrawler(s)
    crawler.thd_num = 1
    crawler.crawl_func = crawler.crawl_list
    crawler.start_page_list = [0]
    crawler.out_file = 'runoob_list.json'
    crawler.run()

    # 采集文章数据
    crawler.crawl_func = crawler.crawl
    crawler.input_file = 'runoob_list.json'
    crawler.out_file = 'runoob_detail.json'
    crawler.run()


if __name__ == "__main__":
    test_crawler()