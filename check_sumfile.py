# -*- coding:utf-8 -*-

import os
import time
import re

t = time.strftime('%Y%m%d',time.localtime(time.time()))
dir = "D:\historysshqdata"

check_files = []

try:
    for root,dir,files in os.walk(dir):
        for f in files:
            if re.match(t, f):
                check_files.append(f)
    if len(check_files) == 4:
        print 0
    else:
        print 1
except Exception,e:
    print 1