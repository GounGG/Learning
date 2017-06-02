#！ -*- coding:utf-8 -*-

from xlwt import *
import xlrd
import pymysql
import time

conn = pymysql.connect(host='121.43.110.205',user='root', passwd='20131220', db='cts_report', charset='utf8')
cur = conn.cursor()
def SQL(cur,sql):
    cur.execute(sql);
    return (cur);

a=SQL(cur,r"SELECT f_xz_lcss AS 新增理财师数量,f_lcs_ljs as 理财师总数量,f_lcs_xz_zjl as 理财师新增资金量,f_lcs_lj_zjl AS 理财师总资金量,f_zc_drxz AS 新增跟投数量,f_zc_lj as 跟投总数量,f_xz_gt_je as 新增跟投资金量,f_zc_xz_zc as 跟投新增账户资金量,f_zzc as 跟投总资金量 from cts_report.t_mrbb_report where date(f_day)=date(20170207);")

w= Workbook(encoding='utf-8')
ws= w.add_sheet(u"跟投宝每日报表")
f = ['新增数量', '总数量', '新增资金量', '总资金量','新增数量', '总数量', '新增跟投资金量', '新增账户资金量', '总资金量']
ff = ['当日买入笔数', '当日买入交易量', '当日卖出笔数', '当日卖出交易量','累计交易量', '当日买入笔数', '当日买入交易量', '当日卖出笔数', '当日卖出交易量', '累计交易量']

fnt = Font()
#fnt.name = 'Times New Roman'   #指定字体类型
fnt.bold = True         #加粗
fnt.height = 0x012C     #字体大小
#fnt.underline = True    #下划线
#fnt.italic = True       #斜体
fnt1 = Font()
fnt1.height = 0x00FA

alignment = Alignment() # Create Alignment
alignment.horz = Alignment.HORZ_CENTER # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
alignment.vert = Alignment.VERT_CENTER # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED

style = XFStyle()
style.font = fnt1
style.alignment = alignment

style1 = XFStyle()
style1.font = fnt
style1.alignment = alignment

ws.write_merge(0, 0, 0, 1, "跟投宝每日运营报表", style1)
ws.write(0, 2, time.strftime('%Y-%m-%d',time.localtime(time.time())), style)
ws.write_merge(1, 4, 0, 0, "专户理财师", style)
ws.write_merge(5, 9, 0, 0, "跟投宝客户", style)
for x in range(len(f)):
    ws.write( x+1 , 1, f[x])

for i in a:
    for b in range(len(i)):
        ws.write( b+1 , 2, i[b])

ws.write(12, 0, "交易情况：")
ws.write_merge(13, 13, 0, 1, "跟投宝交易情况", style1)
ws.write(13, 2, time.strftime('%Y-%m-%d',time.localtime(time.time())), style)
ws.write_merge(14, 18, 0, 0, "专户理财师", style)
ws.write_merge(19, 23, 0, 0, "跟投宝客户", style)
for x in range(len(ff)):
    ws.write( x+14 , 1, ff[x])

a=SQL(cur, 'select f_lcs_cj_b,f_lcs_cj_b_je,f_lcs_cj_s,f_lcs_cj_s_je,f_lcs_lj_jyl,f_gt_cj_b,f_gt_cj_b_je,f_gt_cj_s,f_gt_cj_s_je,f_gt_lj_jyl FROM cts_report.t_mrbb_report where f_day=date(20170207)')
for i in a:
    for b in range(len(i)):
       ws.write( b+14 , 2, i[b])

ws.col(0).width = 6666
ws.col(1).width = 4444
ws.col(2).width = 3333

w.save(u"跟投宝运营报表.xls")