import re

# url = "https://www.encollege.cn/gwapi/article/find?total=209&programaId=36&page=2"
# page = re.findall('\?total=(\d+)',url)[0]
# print(int(page)//20+2)

l= '立足优质高效课堂，培育"匠心匠艺"传人——"上海市教委教研室、语文学科中心组赴环境学校开展调'
a = l.replace('"',"")
# b = l.replace('/[\"]/g', "")
print(a)


