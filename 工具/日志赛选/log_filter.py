#!/usr/bin/env python
# coding:utf-8

import re
import os
import sys
import logging

logging.basicConfig(level=logging.DEBUG,  # 定义输出到文件的log级别，大于此级别的都被输出
                    format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',  # 定义输出log的格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 时间
                    filename='check.log',  # log文件名
                    filemode='a+')

# logfile为你要赛选的日志路径
for dir,root,files in os.walk('/var/log/supervisor/'):
    for file in files:
        if re.search("^php.*log$", file):
            logfile = os.path.join(dir, file)

# 赛选关键字
keyword=sys.argv[1]
# 记录文件信息
statfile='/tmp/logfilestat.txt'


logging.info("======================================================Start======================================================")
logging.info('log_file: {0}, keyword: {1} '.format(logfile, keyword))

# 判断文件是否存在
try:
    f = open(statfile, 'r')
    offset = f.readlines()
    f.close()
except Exception,e:
    logging.info('{0} file not exits,create stat file!'.format(statfile))
    offset = []

alter = []

# 获取文件信息，记录文件inode和offset
with open(statfile, 'w+') as offwr:
    with open(logfile, 'r') as f:
        if len(offset) == 0:
            f.seek(0, 2)
        
        elif len(offset) == 2:
			# 判断文件是否为新文件，如果不是，则延续上次的offset读取新内容
            if int(offset[1]) == int(os.stat(logfile)[1]):
                logging.info("start_offset: {0}".format(offset[0].strip()))
                f.seek(int(offset[0].strip()))
            else:
                logging.info("start_offset: 0")
                f.seek(0)
			# 遍历文本内容
            for i in f.readlines():
                if re.search(str(keyword), i.strip()):
                    logging.error("Find {0} the key!!".format(keyword))
                    alter.append(i)
                else:
                    pass
            
        offwr.write(str(f.tell()))
        offwr.write("\n")
        offwr.write(str(os.stat(logfile)[1]))

f.close()
offwr.close()

logging.info("======================================================End======================================================")

if len(alter) != 0:
    print alter
