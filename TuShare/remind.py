# -*- coding:utf-8 -*-

import tushare as ts
import time
from pandas import DataFrame
from send import Send_Message

end = time.strftime('%Y-%m-%d',time.localtime(time.time()))
start = time.strftime('%Y-%m-%d',time.localtime(time.time()-31536000))

def data(code, end, start):
    res = ts.get_hist_data(code=code, start=start, end=end, ktype='D')
    # ts 取回来的数据格式为DataFrame数据格式
    df=DataFrame(res)
    # 获取索引为open的内容，获取后的格式为数组
    sdata=df['open'].values
    sum=0
    avg=len(sdata)
    for i in sdata:
        sum = sum + int(i)
    return sum/avg


if __name__ == '__main__':
    sh=data('sh', end, start)
    sz=data('sz', end, start)
    v='''上证平均行情(Year):%s \n
深指平均行情(Year):%s
    ''' %(str(sh), str(sz))
    s = Send_Message(str(v))
    s.send_message()

