import requests
import json


url = "http://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzIzNjg1NDk3Mg==&f=json&offset=10&count=10&is_ok=1&scene=124&uin=MTE5NTMwMzg1MQ%3D%3D&key=d6279d11ce075bb11f9458f0355d5819ea2972d671f565506e288dccb5e2c751ddce17d26fa6ec8619fef7664b7055264d85088345525f349bb798f217e48f9f5ee601959e34073de58341175d77e49d&pass_ticket=DtCyVz3oZIOzgnyKRA6L4ws2EF92qRvNy7DGu9ORFQ8gJgmjAGDApA%2FE1fcvClok&wxtoken=&appmsg_token=1057_eBMJYSfAeBImPuT8F2sRAj0DMiduc2JHYHTw0Q~~&x5=0&f=json"


req = requests.get(url)
ass = req.json()
dict1 = json.dumps(ass,indent=4,sort_keys=True,ensure_ascii=False)
dict2 = json.loads(dict1)
print(req.text)
print(dict1)
print(dict2['general_msg_list'])