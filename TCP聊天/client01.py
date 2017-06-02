# -*- coding:utf-8 -*-
'''
自动发送
'''
import socket
import os

host = socket.gethostname()
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect((host, port))
# 接收欢迎消息:
print s.recv(1024)

while True:
    #date=raw_input('#:')
    date=raw_input("#")
    if date == 'exit':
        s.close()
        break
    s.send(date)
    print  s.recv(1024)
