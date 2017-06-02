# -*- coding:utf-8


from celery import Celery
import time

#test_redis  为名字   
app = Celery('test_redis', backend='redis', broker='redis://192.168.1.201:6379')

@app.task
def sendmail(mail):
    print('sending mail to %s...' % mail['to'])
    time.sleep(2)
    print('mail sent.')