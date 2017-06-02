#! -*- coding:utf-8 -*-
#启动脚本一键执行

import os
import re

dir="d:\\tradeserveronlinefortrade"

for root,dirs,files in os.walk(dir):
    for file in files:
        c=os.path.join(root,file)
        if re.findall("startup", c):
            os.chdir(root)
            os.system('start %s' %file)