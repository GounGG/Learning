# -*- coding:utf-8 -*-

import requests
import  json
import time
from send import  *

url = "http://IP/zabbix/api_jsonrpc.php"
header = {"Content-Type":"application/json"}

class Zabbix():
    def __init__(self, url, header):
        self.url = url
        self.header = header
    def get_session(self):
        data = json.dumps({"jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": "xxx",
                "password":r"xxx"
            },
            "id": 0})
        r = requests.post(url = self.url, data = data, headers = self.header)
        ID = json.loads(r.text)
        return  ID['result']

    def send(self):
        data = json.dumps({"jsonrpc": "2.0",
        "method": "alert.get",
            "params": {
                "output": "extend",
                "time_from": time.time() -180,
                "time_till": time.time(),
            },
            "auth":self.get_session(),
            "id": 1
            })
        r = requests.post(url = self.url, data = data, headers = self.header)
        v = json.loads(r.text)
        n = []
        for  i in v['result']:
            value='zabbix报警'
            ss = i['message']
            if ss in n:
                continue
            else:
                if ss:
                    s = Send_Message(ss.encode('utf-8'))
                    s.send_message()
                    n.append(ss)

if __name__ == '__main__':
    try:
        i = 0
        while True:
            r = Zabbix(url, header)
            r.send()
            i = i + 1
            print "第%s次检查" %(i)
            time.sleep(180)
    except Exception as e:
        print e
