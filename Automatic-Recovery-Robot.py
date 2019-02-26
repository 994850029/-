from wxpy import *
import requests
import json
bot = Bot(cache_path=True)

company_group = bot.groups().search('谁来拿外卖')[0]
#调用机器人
def auto_reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "b1c0534942d0485e85f004c6c048386c"
    padload = {
        "key": api_key,
        'info': text
    }
    r = requests.post(url, data=json.dumps(padload))
    result = json.loads(r.content)
    return result["text"]

@bot.register(chats=company_group)
def recv_send_msg(recv_msg):
    print('收到的信息：', recv_msg.text)
    re = auto_reply(recv_msg.text)
    return re
embed()