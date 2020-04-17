import json

apiurls = []
with open("12.txt", "rb") as f:
    apiurls = f.readlines()
urljson = {}
for i in range(len(apiurls)):
    apiurl = apiurls[i].decode("utf-8")
    ipcode = apiurl.split("\t")
    ip = "{}:{}".format(ipcode[0],ipcode[1])
    # print(apiurl.split("\t"))
    print(ip)
    urljson[str(i)] = ip
print(urljson)
with open("url.json", "w") as f:
    f.writelines(json.dumps(urljson))



