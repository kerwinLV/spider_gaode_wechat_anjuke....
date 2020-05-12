import re
l = "http://mp.weixin.qq.com/s?__biz=MzA5MjUwNzQxNw==&amp;mid=202386022&amp;idx=1&amp;sn=1c9fd2401cbe476c211f407bb6ee06a1&amp;scene=27#wechat_redirect"

a = l.split("?")[1].split("&")[2].split("=",1)[1]
print(a)

b = re.findall("__biz=(.*?)&",l)
c = re.findall("amp;mid=(.*?)&",l)
d = re.findall("amp;idx=(.*?)&",l)
e = re.findall("amp;sn=(.*?)&",l)
print(b)
print(c)
print(d)
print(e)

k = []
if k:
    print("ll")
else:
    print("1231")

oo = ['http://store.is.autonavi.com/showpic/5dfbad17e027b64a2591fd65750f1934', 'http://store.is.autonavi.com/showpic/67192e9da9867ec1792feb29dab251f0']

print(",".join(oo))
