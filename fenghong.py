# -*- coding=utf-8 -*-
__author__ = 'linzirong'

import json
import requests
import datetime

#获取所有有股票分红的代码
def get_stock_list(exchange):
    stocklist_url = "http://client.gushitong.baidu.com/ui/gushitong?queryURL=stockcode&from=test&os_ver=2.0&vv=100&cuid=test&uid&format=json"
    response = requests.get(stocklist_url)
    content = response.content
    content_dict = json.loads(content)
    #检测content_dict中是否包含“data”这个key
    if not content_dict.has_key('data'):
        logger.error('not stocklist found')
        raise Exception
    if not content_dict['data'].has_key('newData'):
        logger.error('not stocklist found')
        raise Exception

    all_stock_list = content_dict['data']['newData']
    stock_list = []
    if exchange == 'hk':
        for stock in all_stock_list:
            f_exchange = stock['f_exchange']
            asset = stock['f_asset']
            stock_code = stock['f_code']
            if f_exchange == 'hk' and asset == '0':
                stock_list.append(stock_code)
    if exchange == 'hs':
        for stock in all_stock_list:
            f_exchange = stock['f_exchange']
            asset = stock['f_asset']
            stock_code = stock['f_code']
            if (f_exchange == 'sh' or f_exchange == 'sz') and asset == '0':
                stock_list.append(stock_code)
    return stock_list

def get_fenghong_from_zxg(code):
    url='http://ifzq.gtimg.cn/stock/corp/cwbb/search?symbol='+code+'&type=sum&jianjie=1&_appName=android&_dev=mx2&_devId=860806022057110&_appver=3.5.0&_ifChId=65&_screenW=800&_screenH=1280&_osVer=4.1.1&_uin=825474077'
    try:
        response=requests.get(url)
        content=response.content
        print content
        dict=json.loads(content)
        return dict['data']['gegu']['fenhong'][0]
    except Exception as e:
        print str(e)
        return {}

#测试
#fenhong_dict=get_fenghong_from_zxg('sz000029')
#print fenhong_dict['cqr']

stock_list=get_stock_list('hs')
today=datetime.date.today()
today_str=today.strftime("%Y-%m-%d")
#print today,today_str
i=0
for stock in stock_list:
#    print stock
    fenhong_dict=get_fenghong_from_zxg(stock)
    if len(fenhong_dict.keys())==0:
        continue
    cqr=fenhong_dict['cqr']
#    print i
#    i+=1
    #cqr=cqr.replace('-','')
    if cqr==today_str:
        print stock, fenhong_dict




