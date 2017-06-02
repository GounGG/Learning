#! -*- coding:utf-8 -*-

from xlwt import *
import xlrd
import pymysql
import time


conn = pymysql.connect(host='120.26.228.169',user='root', passwd='p3temp_S', db='mom', charset='utf8')
cur = conn.cursor()

def SQL(sql):
    cur.execute(sql);
    return (cur);

w= Workbook(encoding='utf-8')
ws= w.add_sheet(u"MOM每日运营报表")

fnt = Font()
fnt.bold = True
fnt.height = 0x012C
alignment = Alignment()
alignment.horz = Alignment.HORZ_CENTER
alignment.vert = Alignment.VERT_CENTER

style = XFStyle()
style.font = fnt
style.alignment = alignment


alignment1 = Alignment()
alignment1.horz = Alignment.HORZ_CENTER
alignment1.vert = Alignment.VERT_CENTER

style1 = XFStyle()
style1.alignment = alignment1

ws.write_merge(0, 0, 0, 1, "MOM每日运营报表", style)
ws.write(0, 2, time.strftime('%Y-%m-%d',time.localtime(time.time())), style1)
ws.write_merge(1, 4, 0, 0,'出入金情况', style1)
ws.write_merge(6, 9, 0, 0, '资金池交易情况', style1)
ws.write_merge(11, 12, 0, 0, '开户', style1)
ws.write(14 ,0 , '交易人数', style1)
ws.write(1 ,1 , r'当日总充值金额（元）', style1)
ws.write(2 ,1 , r'当日总提现金额（元）', style1)
ws.write(3 ,1 , '充值人数', style1)
ws.write(4 ,1 , '提现人数', style1)
ws.write(6 ,1 , '资金方', style1)
ws.write(6 ,2 , '可用资金（元）', style1)
ws.write(6 ,3 , '买入成交额（元）', style1)
ws.write(6 ,4 , '卖出成交额（元）', style1)
ws.write(7 ,1 , '王纪仁账户', style1)
ws.write(8 ,1 , '牛总账户', style1)
ws.write(9 ,1 , '王小林账户', style1)
ws.write(11 ,1 , '总开户数', style1)
ws.write(12 ,1 , '新增开户数', style1)

a=SQL(r"SELECT SUM(b.f_money) FROM  (SELECT f_name,f_userid,f_account FROM mom.t_peizi_account WHERE f_money_userid !='43') a JOIN  (SELECT f_userid,f_money,f_type,f_createtime FROM mom.t_recharge_cashout WHERE f_type='C') b ON a.f_userid=b.f_userid WHERE DATE(b.f_createtime)=DATE(NOW());")
for i in a:
    ws.write(1 , 2 , i[0])

a=SQL(r"SELECT SUM(b.f_money) FROM (SELECT f_name,f_userid,f_account FROM mom.t_peizi_account WHERE f_money_userid !='43') a JOIN (SELECT f_userid,f_money,f_type,f_createtime FROM mom.t_recharge_cashout WHERE f_type='T') b ON a.f_userid=b.f_userid WHERE DATE(b.f_createtime)=DATE(NOW());")
for i in a:
    ws.write(2, 2, i[0])

a=SQL(r"SELECT COUNT(*) from (SELECT a.f_account FROM  (SELECT f_name,f_userid,f_account FROM mom.t_peizi_account WHERE f_money_userid !='43') a JOIN  (SELECT f_userid,f_money,f_type,f_createtime FROM mom.t_recharge_cashout WHERE f_type='C') b ON a.f_userid=b.f_userid WHERE DATE(b.f_createtime)=DATE(NOW()) GROUP BY a.f_account) a;")
for i in a:
    ws.write(3, 2, i[0])

a=SQL(r"SELECT COUNT(*) from (SELECT a.f_account FROM  (SELECT f_name,f_userid,f_account FROM mom.t_peizi_account WHERE f_money_userid !='43') a JOIN  (SELECT f_userid,f_money,f_type,f_createtime FROM mom.t_recharge_cashout WHERE f_type='T') b ON a.f_userid=b.f_userid WHERE DATE(b.f_createtime)=DATE(NOW()) GROUP BY a.f_account) a;")
for i in a:
    ws.write(4, 2, i[0])

a=SQL(r"SELECT COUNT(*) from (SELECT a.f_account FROM (SELECT f_account,f_name FROM mom.t_peizi_account WHERE f_money_userid !='43') a JOIN (SELECT f_account,f_cjsj,f_code,f_stockname,f_side,f_cjsl,f_cjjj,f_cjje,f_exchange,f_qs_day,f_createtime FROM unitrade_counter.t_his_security_cj WHERE DATE(f_createtime)=DATE(NOW())) b ON a.f_account=b.f_account GROUP BY a.f_account) c;")
for i in a:
    ws.write(14, 1, i[0])

a=SQL(r"SELECT COUNT(*) FROM mom.t_peizi_account WHERE f_money_userid !='43' AND f_name NOT IN ('hj!','N','哈哈','无卡号','何静','曾建峰','nan','nan1','测试','nan2','何静11','临摹1','nn','临摹','南','HJ','何','南');")
for i in a:
    ws.write(11, 2, i[0])

a=SQL(r"SELECT COUNT(b.f_new) FROM (SELECT f_name,f_account,f_password,f_jyfy,f_gyf,f_createtime FROM mom.t_peizi_account WHERE f_money_userid !='43' AND f_name NOT IN ('hj!','N','哈哈','无卡号','何静','曾建峰','nan','nan1','测试','nan2','何静11','临摹1','nn','临摹','南','HJ')) a LEFT JOIN (SELECT f_account,COUNT(f_account)AS f_new FROM mom.t_peizi_account WHERE DATE_FORMAT(f_createtime,'%Y-%m-%d')=DATE_SUB(DATE_FORMAT(NOW(),'%Y-%m-%d'),INTERVAL 0 DAY) GROUP BY f_account) b ON a.f_account=b.f_account;")
for i in a:
    ws.write(12, 2, i[0])

a=SQL(r"SELECT SUM(b.f_cjje/10000) FROM (SELECT f_account,f_name FROM mom.t_peizi_account WHERE f_money_userid ='45') a JOIN (SELECT f_account,f_stockcode,f_stockname,f_side,f_cjsl,f_cjje,f_cjsj FROM mom.t_trade WHERE f_side!='S') b ON a.f_account=b.f_account WHERE DATE(b.f_cjsj)=DATE(NOW())")
for i in a:
    ws.write(7, 3, i[0])

a=SQL(r"SELECT SUM(b.f_cjje/10000) FROM  (SELECT f_account,f_name FROM mom.t_peizi_account WHERE f_money_userid ='45') a JOIN (SELECT f_account,f_stockcode,f_stockname,f_side,f_cjsl,f_cjje,f_cjsj FROM mom.t_trade WHERE f_side!='B') b ON a.f_account=b.f_account WHERE DATE(b.f_cjsj)=DATE(NOW());")
for i in a:
    ws.write(7, 4, i[0])

a=SQL(r"SELECT SUM(b.f_cjje/10000) FROM (SELECT f_account,f_name FROM mom.t_peizi_account WHERE f_money_userid ='44') a JOIN (SELECT f_account,f_stockcode,f_stockname,f_side,f_cjsl,f_cjje,f_cjsj FROM mom.t_trade WHERE f_side!='S') b ON a.f_account=b.f_account WHERE DATE(b.f_cjsj)=DATE(NOW())")
for i in a:
    ws.write(8, 3, i[0])

a=SQL(r"SELECT SUM(b.f_cjje/10000) FROM  (SELECT f_account,f_name FROM mom.t_peizi_account WHERE f_money_userid ='44') a JOIN (SELECT f_account,f_stockcode,f_stockname,f_side,f_cjsl,f_cjje,f_cjsj FROM mom.t_trade WHERE f_side!='B') b ON a.f_account=b.f_account WHERE DATE(b.f_cjsj)=DATE(NOW());")
for i in a:
    ws.write(8, 4, i[0])

a=SQL(r"SELECT SUM(b.f_cjje/10000) FROM (SELECT f_account,f_name FROM mom.t_peizi_account WHERE f_money_userid ='47') a JOIN (SELECT f_account,f_stockcode,f_stockname,f_side,f_cjsl,f_cjje,f_cjsj FROM mom.t_trade WHERE f_side!='S') b ON a.f_account=b.f_account WHERE DATE(b.f_cjsj)=DATE(NOW())")
for i in a:
    ws.write(9, 3, i[0])

a=SQL(r"SELECT SUM(b.f_cjje/10000) FROM  (SELECT f_account,f_name FROM mom.t_peizi_account WHERE f_money_userid ='47') a JOIN (SELECT f_account,f_stockcode,f_stockname,f_side,f_cjsl,f_cjje,f_cjsj FROM mom.t_trade WHERE f_side!='B') b ON a.f_account=b.f_account WHERE DATE(b.f_cjsj)=DATE(NOW());")
for i in a:
    ws.write(9, 4, i[0])

a=SQL(r"SELECT f_kyzj/10000 FROM unitrade_counter.t_his_security_money WHERE f_account='88050031' AND DATE(f_qs_day)=DATE(NOW())")
for i in a:
    ws.write(7, 2, i[0])

a=SQL(r"SELECT f_kyzj/10000 FROM unitrade_counter.t_his_security_money WHERE f_account='92707713' AND DATE(f_qs_day)=DATE(NOW())")
for i in a:
    ws.write(8, 2, i[0])

a=SQL(r"SELECT f_kyzj/10000 FROM unitrade_counter.t_his_security_money WHERE f_account='36800477' AND DATE(f_qs_day)=DATE(NOW())")
for i in a:
    ws.write(9, 2, i[0])

ws.col(0).width = 6666
ws.col(1).width = 5555
ws.col(2).width = 5555
ws.col(3).width = 5555
ws.col(4).width = 5555

w.save(u"MOM运营报表.xls")