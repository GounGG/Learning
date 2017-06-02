#!/usr/bin/env python
# -*-coding:utf-8-*-

import smtplib
from email.mime.text import MIMEText

mailto_list=["fangjipu@xinyusoft.com"] 
mail_host="smtp.exmail.qq.com"
mail_user="fangjipu@xinyusoft.com"
mail_pass="password"
mail_postfix="xinyusoft.com"
  
def send_mail(to_list,sub,content): 
    me="方记普"+"<"+mail_user+"@"+mail_postfix+">"  
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host)  
        server.login(mail_user,mail_pass)  
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False  
if __name__ == '__main__':  
    if send_mail(mailto_list,"售后回复","真的好好"):  
        print "发送成功"  
    else:  
        print "发送失败"
