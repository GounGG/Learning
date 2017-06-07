# -*- coding:utf-8 -*-

import requests
import json
import time
from multiprocessing.dummy import Pool as ThreadPool
import  re

# request API
class ES_API:
    def __init__(self, url, data, headers):
        self.url=url
        self.data=data
        self.headers=headers

    def get(self):
        r = requests.post(url=self.url, data=json.dumps(self.data), headers=self.headers)
        v=json.loads(r.text)
        return v

    def process(self):
        v = self.get()
        if v.get('status'):
            pass
        else:
            return (v['hits']['hits'])


def get_data(index):
    date = time.strftime('%Y.%m.%d', time.localtime(time.time()))
    url="http://192.168.30.135:9200/%s-%s/_search" %(index, date)
    headers={'Content-Type':'application/json'}
    data={
         "query": {
         "match": {
        "message": {
            "query": "ERROR"
            }
        }
        }
    }
    C=ES_API(url, data, headers)
    return C.process()

def data():
    indexs=['app', 'tomcatweb', 'system']
    pool = ThreadPool(len(indexs))
    results = pool.map(get_data, indexs)
    pool.close()
    pool.join()
    return  results

def returnData():
    value = {}
    for i in data():
        ff = 0
        for x in i:
            t = x['_source']['@timestamp']
            tt = re.search(r'^([0-9]{4}-[0-9]{2}-[0-9]{2})[a-zA-Z]+([0-9]{2}:[0-9]{2}:[0-9]{2}).*$', t)
            realtime = str(tt.group(1)) + str(tt.group(2))
            timeArray = time.strptime(realtime, "%Y-%m-%d%H:%M:%S")
            timeDiff = time.time() - time.mktime(timeArray)
            if int(timeDiff) > 300:
                v = {}
                v['time'] = str(tt.group(1)) + ' ' + str(tt.group(2))
                v['message'] = x['_source']['message']
                value[ff] = v
                ff = ff + 1
    return value

def if_null():
    if returnData():
        print(returnData())
    else:
        pass
    time.sleep(300)

if __name__ == '__main__':
    while True:
        if_null()




