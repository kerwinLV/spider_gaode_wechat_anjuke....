a = """
<p style="text-align:center"><img alt="" src="http://www.encollege.cn/imageFile/2020-05-17/0/1589694394108--3.0" style="height:145px; width:229px" />
<img alt="" src="http://www.encollege.cn/imageFile/2020-05-17/0/1589694445550--4.0" s
tyle="height:147px; width:229px" /><img alt="" src="/documents/10179/44603/666.jpg/
0e75407e-1393-4199-a2d3-3f5849395e81" style="height:145px; width:229px" /><img alt="" src="/documents/10179/44603/777.jpg/43b28ad3-cf32-44ff-a4ad-584f3d3b36bd" style="height:147px; width:229px" /></p>
"""
import re


rea = re.findall('(documents.*?/>)',a,re.S)
# print(rea)
for i in rea:
    dom = '<img alt="" src="/{}'.format(i)
    print("-----------------------------------------------")
    print(dom)
    # if dom in a:
    #     print("13212131313")

    a = a.replace(dom,"")
    # print(a)
print(a)

# print("-----------------------------------------------")
# print(a)
# for i in rea:
#     if "documents" in i:
#         print(i)
# print(rea)
# print(a)
#
# k ="""<img alt="" src="/documents/10179/44603/777.jpg/43b28ad3-cf32-44ff-a4ad-584f3d3b36bd" style="height:147px; width:229px" />"""
#
# h ="""<img alt="" src="/documents/10179/44603/777.jpg/43b28ad3-cf32-44ff-a4ad-584f3d3b36bd" style="height:147px; width:229px" />"""
#
# if h == k:
#     print(111111)