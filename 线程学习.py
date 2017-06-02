 # -*- coding: utf-8 -*-
# from multiprocessing import Pool 多进程
from multiprocessing.dummy import Pool as ThreadPool #多线程
import time
import urllib2

s

urls = [
    'http://www.baidu.com',
    'http://www.aliyun.com'
    ]

# 单线程
start = time.time()
results = map(urllib2.urlopen, urls)
print 'Normal:', time.time() - start

# 多线程
start2 = time.time()
# 开4个 worker，没有参数时默认是 cpu 的核心数
pool = ThreadPool(2)
# 在线程中执行 urllib2.urlopen(url) 并返回执行结果
time.sleep(10)
results2 = pool.map(urllib2.urlopen, urls)
pool.close()
pool.join()
print 'Thread Pool:', time.time() - start2
