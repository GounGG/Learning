# -*- coding:utf-8 -*-

import pymysql
import re
import sys

try:
    conn = pymysql.connect(host='121.43.110.205',user='root', passwd='20131220', db='', charset='utf8')
    cur = conn.cursor()
except Exception,e:
    print e

def Querys(sql):
    cur.execute(sql);
    return cur.fetchall();

a = Querys('show full processlist;')

def connections():
    return len(a)

sleep = []
def Sleep():
    for i in a:
        if re.findall('Sleep', str(i)):
            sleep.append(i[5])
    return len(sleep)

query = []
def Query():
    for i in a:
        if re.findall('Query', str(i)):
            query.append(i[5])
    return len(query)

def avg_time():
    number = 0
    for i in a:
        number = number + int(i[5])
    t1 = number / len(a)
    return t1

if __name__ == '__main__':
    try:
        if sys.argv[1] == 'connections':
            print connections()
        elif sys.argv[1] == 'Sleep':
            print Sleep()
        elif sys.argv[1] == 'Query':
            print Sleep()
        elif sys.argv[1] == 'avg_time':
            print avg_time()
        else:
            pass
    except Exception,e:
        print e






