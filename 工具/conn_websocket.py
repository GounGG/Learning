# -*- coding:utf-8 -*-

'''
模块下载，帮助地址：https://github.com/liris/websocket-client#readme
模块：websocket-client
说明：websocket客户端
比较方便，可以根据自己的真实环境，进行改动
'''

from websocket import create_connection
import requests
import json

#建立一个websocket连接
ws = create_connection("ws://115.29.233.142:3397")
#对websocket客户端发送一个请求
ws.send("token")
#使用一个变量，接受返回的数据
result =  ws.recv()
url="http://www.xinyusoft.com:8085/uuFinancialPlanner/ESBServlet?command=xlog.AddLogAction&rst=%s" %result
data={'log':"xinyu"}
p = requests.post(url,data=data)
print p.text
#打印返回的数据
print result
#关闭websocketqingq
ws.close()




