# -*- coding:utf-8 -*-

import requests
import json
import sys
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
        params = {'corpid':'xxxxx',
        'corpsecret': r'xxxx'
        }
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        # verify=True 访问https站点，会进行证书验证，False忽略证书验证，还可以通过cert指定证书，例：cert=('/path/server.crt', '/path/key')
        r = requests.get(url=url, params=params, verify=False)
        token=json.loads(r.text)['access_token']
        return token

    def send_message(self):
        # 当touser为@all后，toparty和totag可随意填写
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
        r = requests.post(url, data=value, verify=False)
        return r.text

if __name__ == '__main__':
    v = sys.argv[1]
    s = Send_Message(str(v))
    s.send_message()

