# -*- coding:utf-8 -*-

import urllib2
import json
key = 'q5mTrTGzCSVq5QmGpI9y18Bo'
ipurl = 'http://api.map.baidu.com/location/ip?ak='+key+'&coor=bd09ll&ip='
sqlarr = []
def getGeo(ip):
    try:
        u = urllib2.urlopen(ipurl+ip)
        page = json.load(u)
        if 'content' in page:
            #获取ip地址的经纬度
            point = page['content'].get('point')
            #获取ip具体地址地址
            add = page['content'].get('address')
            print r'address: %s' % add
            print 'ip %s has geoX %s and geoY %s' % (ip,point['x'],point['y'])
    except:
        print 'error'
getGeo('202.198.16.3')