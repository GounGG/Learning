# -*- coding:utf-8 -*-
'''
模块下载，帮助地址：https://github.com/liris/websocket-client#readme
模块：websocket-client
说明：websocket客户端
弊端：不能接受websocket服务端返回的数据
'''

import websocket
import thread
import time


#定义消息返回
def on_message(ws, message):
    print message

#定义错误返回
def on_error(ws, error):
    print error

#定义关闭返回
def on_close(ws):
    print "### closed ###"

def on_open(ws):
    #*args 默认没有k值
    def run(*args):
        time.sleep(2)
        #发送请求
        ws.send("cmd=hq.getIndexRankList&stockCode=A&marketCode=Industry_&page=1")
        #延迟两秒，等待消息返回
        time.sleep(2)
        #关闭连接
        ws.close()
        print "thread terminating..."
    #开启一个线程，执行run函数
    thread.start_new_thread(run, ())

i=0

if __name__ == "__main__":
    while True:
        try:
            websocket.enableTrace(True)
            ws = websocket.WebSocketApp("wss://hqservice.ghzq.com.cn/socket/echo",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
        #继续上面的on-open
            ws.on_open = on_open
        #执行上面的操作
            ws.run_forever()
            i = i + 1
            print "成功:%d" %i
        except Exception,e:
            print e
            exit(1)













