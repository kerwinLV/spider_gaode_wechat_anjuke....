import requests
from lxml import etree

def get_all_url():
    url = "https://shanghai.anjuke.com/sale/"
    req = requests.get(url)
    print(req.status_code)
    if req.status_code ==200:
        print("hakjhjk")
        req_etree = etree.HTML(req.text)
        req_xpath = req_etree.xpath('//*[@id="content"]/div[3]/div[1]/span[2]/a/@href')
        print(req_etree)
        print(req_xpath)
        req_xpath1 = []
        for i in range(1,len(req_xpath)):
            c = req_xpath[i]+"p{}/#filtersort"
            req_xpath1.append(c)
        return req_xpath1

# a = get_all_url()
# print(a)
# b=[]
# for i in range(1,len(a)):
#     c = a[i]+"p%s/#filtersort"
#     print(c%(5))

#https://shanghai.anjuke.com/sale/minhang/p2/#filtersort