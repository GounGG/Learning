# coding:utf-8

import psutil
import re

pids = psutil.pids()
for i in pids:
    p=psutil.Process(i)
    if re.search('java', p.name()):
        print p.name(),p.num_threads()

