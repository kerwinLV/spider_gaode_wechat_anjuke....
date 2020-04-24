import requests
from lxml import etree

url = "https://shanghai.anjuke.com/community/view/990328?from=propview"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
}

a = requests.get(url)
print(a.status_code)
b = etree.HTML(a.text)
c = b.xpath('/html/body/div[2]/div[3]/div[1]/h1/span/text()')
print(c)