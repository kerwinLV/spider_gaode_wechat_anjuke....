import requests


def get_ippool_url():
    """

    :return: 获取一个ip代理
    """
    proxy = {}
    ip_pool_url = "http://http.tiqu.alicdns.com/getip3?num=1&type=2&pro=&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=1&lb=1&sb=0&pb=4&mr=1&regions=&gm=4"
        #          "http://http.tiqu.alicdns.com/getip3?num=1&type=2&pro=&city=0&yys=0&port=11&time=1&ts=1&ys=1&cs=1&lb=1&sb=0&pb=4&mr=1&regions=&gm=4"
    pool_res = requests.get(ip_pool_url)
    if pool_res.json()["data"]:
        proxy["https"] = "{}:{}".format(pool_res.json()["data"][0]["ip"],pool_res.json()["data"][0]["port"])
        print("拿到一个ip")
        print(proxy)
    else:
        proxy = {}
    return proxy

