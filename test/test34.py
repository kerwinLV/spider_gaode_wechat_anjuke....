import requests
from lxml import etree
import re
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
proxy = {"http": "175.43.151.48"}
url = "https://shanghai.anjuke.com/prop/view/A2029684545?from=filter&spread=commsearch&invalid=1&click_url=https://lego-click.anjuke.com/jump?target=pZwY0ZnlsztdraOWUvYKuaYLuW7WmW9vnzYOuHbQsHEYmyDVmW0kuaYknH9dPh7bmh7BnHTKnHTQnHm3PWNLTEDQPjEvrHTOP1mkPW0vrj01THndnjTkTHndnjTkTHD_nHnKnBkQPjDQTHDdrj0LnjN1rj03Pj9KnE7AEzdEEzdKibfb8C1hBmfhBs4MoufG9cM-BFxCCpWGCUNKnEDQTEDVnEDKnHcdn1NzrjEznWmLPW0knHD3PTDvTEDQTH0dPjNOmW6WsymdPWnVPAw-uaYOnhN3syNYuHbOrHTYP1IhP9DQnWN1PHc3PjczrjTzPHEzPHbzTHDzPHndnW9YnWcLn1bvnHNLPjEKTEDKTEDVTEDKpZwY0Znlszq1pA78uv66piO6UhGdpvN8mvqVsLP6UANf0ZRbUvOMsLTQskDQrNF7E1FjridjwjDzsHwAn1mVrNndPiYzEbN1P1IanYmvnWmKnHcYsW0LsWDdnB3OnkDkTHTKTHD_nHnKXLYKnHTkn1NKnHTknHmYrTD1n1n1PynYnaYznWR6sHwhuHNVmW9Qmid-njRWnWuWPh7-uWbKTHEKTED1THc_nHEQnikvnWn3THDKmWDknjELnAn1n1cknADzn9&uniqid=pc5ea2762c95dba1.48619688&region_ids=7&position=1&kwtype=filter&now_time=1587705388"
res = requests.get(url,headers = header,proxies=proxy)
# print(res.text)
if res.status_code ==200:
    # url = re.findall('<a href="(.*?)" target="_blank"class="comm-jd-link2">小区详情&gt;</a>小区概况</h4>',res.text,re.S)
    # print(url)
    etr = etree.HTML(res.text)
    print(etr.xpath('//div[@class="comm-commoninfo"]/h4/a'))
    deurl = etr.xpath('//div[@class="comm-commoninfo"]/h4/a/@href')
    print(deurl)