# -*- coding:utf-8 -*-

import requests
import json

'''
基础环境：微信企业号
version：python 2.7
'''

class Send_Message():
    def __init__(self, text):
        self.text = text
    def Token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        # corpid,corpsecret 为微信端获取
        params = {'corpid':'wx02cd0899a03b0fec',
        'corpsecret': r'W8GSXBuU8bGSkqdI-MZkWv2fXHRHgcNqOrfNzuiw1Ezb1mTyCE2CT5dr4bPffDbX'
        }
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        r = requests.get(url=url, params=params)
        token=json.loads(r.text)['access_token']
        return token

    def send_message(self):
        data={"touser": "@all",
        "toparty": " PartyID1 | PartyID2 ",
        "totag": " TagID1 | TagID2 ",
        "msgtype": "text",
        "agentid": '2',
        "text": {
            "content": "%s" %(self.text)
        },
        "safe":0
        }
        # json.dumps在解析格式时，会使用ascii字符集，所以解析后的数据无法显示中文，ensure_ascii不解析为ascii字符集，使用原有字符集
        value = json.dumps(data, ensure_ascii=False)
        token = self.Token()
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' %(token)
        r = requests.post(url, data=value)
        return r.text

if __name__ == '__main__':
    s = Send_Message("你好，欢迎")
    s.send_message()