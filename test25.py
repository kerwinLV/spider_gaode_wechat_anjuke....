import requests
from lxml import etree
url = "https://shanghai.anjuke.com/sale/"
a = requests.get(url)
b = etree.HTML(a.text)
c = b.xpath('//*[@id="content"]/div[3]/div[3]/span[2]/a[4]/@jk')
print(c)
if c:
    print("akjkjsgkjg")
else:
    print("5454534435435")