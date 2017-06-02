# -*- coding:utf-8 -*-

import pymysql

f = open('nginx.log')
res = {}
for l in f:
    arr = l.split(' ')
    # 获取ip url 和status
    ip = arr[0]
    url = arr[6]
    status = arr[8]
    # ip url 和status当key，每次统计+1
    res[(ip,url,status)] = res.get((ip,url,status),0)+1
# 生成一个临时的list
res_list = [(k[0],k[1],k[2],v) for k,v in res.items()]

conn = pymysql.connect(host='192.168.30.130',user='root', passwd='p3temp_S', db='log')
cur = conn.cursor()
def SQL(cur,sql):
    cur.execute(sql);
    return (cur);

#conn.commit()
# 按照统计数量排序，打印前10
try:
    for s in sorted(res_list,key=lambda x:x[3],reverse=True)[:10]:
        SQL(cur, r"insert log values ('%s','%s',%s,%s,now());" % s )
        if SQL:
            conn.commit()
except Exception,e:
    print e
