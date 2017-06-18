# -*- coding:utf-8 -*-

import tushare as ts
import time
from pandas import DataFrame
from send import Send_Message

end = time.strftime('%Y-%m-%d',time.localtime(time.time()))
start = time.strftime('%Y-%m-%d',time.localtime(time.time()-31536000))

class analysis_data():
    def __init__(self, end, start):
        self.end = end
        self.start = start

    def his_data(self,code, start, end):
        res = ts.get_hist_data(code=code, start=start, end=end, ktype='D')
        # ts 取回来的数据格式为DataFrame数据格式
        df=DataFrame(res)
        # 获取索引为open的内容，获取后的格式为数组
        sdata=df['open'].values
        return  sdata

    def his_avg_data(self, code, start, end):
        res = self.his_data(code, start, end)
        sum=0
        avg=len(res)
        for i in res:
            sum = sum + int(i)
        return sum/avg

    def vo_market(self,code):
        res = self.his_data(code, self.start, self.end)
        return res

    def data(self):
        d = {}
        res = ts.get_index()
        df = DataFrame(res)
        # 设置查找的索引
        code = ['000001', '399001']
        # 使用loc查找多列，多元数组，loc['游标，1,3<打印1-3行>'， '[list]<需要查找的列>']
        to_data = df.loc[:, ['code', 'change', 'preclose', 'high', 'low']]
        # to_data['code'].isin(code) 搜索code列中是否包含list code的内容，返回结果为index bool，
        # to_data['code'].isin(code) 获取匹配结果为True的行
        for code,change,pre,high,low in to_data[to_data['code'].isin(code)].values:
            x = {}
            x['curr'] = int((1 + float(change/100))*pre)
            x['high'] = int(high)
            x['low'] = int(low)
            d[code] = x
        return d

    def run(self):
        sh=self.his_avg_data('sh', self.start, self.end)
        sz=self.his_avg_data('sz', self.start, self.end)
        curr=self.data()
        v='''上证平均行情(Year):%s \n
max:%s\t\t\tmin:%s
------------------
深指平均行情(Year):%s \n
max:%s\t\t\tmin:%s
------------------
SH：
当前:%s\t\t\t最高:%s\t\t\t最低:%s
SZ:
当前:%s\t\t\t最高:%s\t\t\t最低:%s
''' %(str(sh), max(self.vo_market('sh')), min(self.vo_market('sh')), str(sz), max(self.vo_market('sz')), min(self.vo_market('sz')), curr['000001']['curr'],curr['000001']['high'],curr['000001']['low'] , curr['399001']['curr'],curr['399001']['high'], curr['399001']['low'])
        s = Send_Message(str(v))
        s.send_message()


f=analysis_data(end, start)
f.run()