# -*- coding:utf-8 -*-

import redis
import json

def key(name):
    r=redis.Redis(host='120.26.228.169',port=6379,db=0)
    a=r.hvals(name)[1]
    b=json.loads(a)
    print b['drsyl']*100

key('product:baseinfo:463')



