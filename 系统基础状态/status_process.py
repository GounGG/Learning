# -*- coding:utf-8 -*-

import re
import psutil
import sys

pid_status={}
def process(x):
    n = 0
    p = psutil.pids()
    for i in p:
        pid = psutil.Process(i)
        name = str(pid.name())
        if re.match(x, name):
            pid_status[n] = {'pid':i, 'name':name, 'status':pid.status()}
            n = n + 1
    return  pid_status

name = sys.argv[0]
process(name)
for i in pid_status.keys():
    if pid_status[i]['status'] == 'running':
        print 0
    else:
        print 1

