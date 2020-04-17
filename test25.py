import requests
# from lxml import etree
# url = "https://www.baidu.com"
# proxy = {'https': 'http://182.35.83.31:9999'}
# a = requests.get(url,proxies = proxy)
# print(a.status_code)
#
from tool_get_ip_pool import get_ip
import random
a = get_ip()
b = random.choice(a)

try:
    url = "https://www.baidu.com"
    proxy = {'https': 'http://182.35.83.31:9999'}
    a = requests.get(url,proxies = b)
    print(a.status_code)
except Exception as e:
    print()
# import telnetlib
#
# try:
#     telnetlib.Telnet('182.35.83.31', port='9999', timeout=10)
# except:
#     print('connect failed')
# else:
#     print('success')

# b = etree.HTML(a.text)
# c = b.xpath('//*[@id="content"]/div[3]/div[3]/span[2]/a[4]/@jk')
# print(c)
# if c:
#     print("akjkjsgkjg")
# else:
#     print("5454534435435")