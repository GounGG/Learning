# -*- coding:utf-8 -*-

from hashlib import md5

def getmd5(md5, filename):
    m = md5()
    p = open(filename, 'r+')
    m.update(p.read())
    p.close()
    md5 = m.hexdigest()
    return  md5


print(getmd5(md5, r'C:\Users\Administrator\Desktop\logstash.conf'))