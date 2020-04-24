import urllib.parse
g = "%E6%88%91%E4%BB%AC%E9%83%BD%E6%98%AF%E5%B0%8F%E8%AF%97%E4%BA%BA"
a = urllib.parse.quote(g)
# a = g.decode("utf-8")
print(a)