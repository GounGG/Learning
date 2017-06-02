#! -*- coding:utf-8 -*-

import requests
import json
import time
import random
import re

DATA3={'type':'housenum',
       'userhousenum':'5019'
}
url="http://kaipan.juzhen.pw/hbpoly/2016/buyhouse20161221bymatrix/webserver/parkingserver.aspx"
headers = {'Accept': 'application/json, text/javascript, */*; q=0.01'}
cookies={'ASP.NET_SessionId':'afl4jk2q2zj2uwb4qcvyc2mt',
         'userprimary':'7c193f8f-07d8-4227-bb26-dfa3e0694c91',
         'parkuserid':'9CA2B40C579EE65F',
         'aliyungf_tc':'AQAAAKvP9wCVdAcAmi/3OuRc+edOXThg'
         }

r3 = requests.post(url, cookies = cookies, data=DATA3, headers=headers)
a=r3.headers['Set-Cookie']
b=re.split('=|;', a)
print b

cookies['userhousenum']=b[1]
a='3-1'
num='2303'
DATA4={'type':'getallinfo', 'area':a}
print cookies
print DATA4
r4 = requests.post(url, cookies = cookies, data=DATA4, headers=headers)
aa=json.loads(r4.text)

for i in aa['rows']:
   if i['num'] == num:
         b = i['keypwd']

DATA5={'type':'sendbykeypwd',
      'area':a,
      'num':num,
      'keypwd':b}
DATA6={'type':'getinfobyidandkeypwd',
       'area':a,
       'num':num,
       'keypwd':b}
r6 = requests.post(url, cookies = cookies, data=DATA6, headers=headers)
print r6.text
r5 = requests.post(url, cookies = cookies, data=DATA5, headers=headers)
print r5.text

