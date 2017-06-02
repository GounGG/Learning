# -*- coding:utf-8 -*-

import requests
import json
from flask import Flask

app = Flask(__name__)

def  get(url):
    r = requests.get(url)
    a = r.text
    b=json.loads(a)
    return b['datalist']
URL=r'http://test.xinyusoft.com:8080/uuFinancialPlanner/ESBServlet?command=sunfloweross.getDataAction&selectsqlname=selectproductstatus&productstatus=S&page.size=max'

@app.route('/')
def index():
    table = '<table border="1" width="100%" style="table-layout:fixed" >'
    table += '<tr align="center"><td>product</td><td>URL</td><td>status</td><td>sum</td><td>DATE</td></tr>'
    for c in get(URL):
        table += '<tr><td align="center">%s</td><td style="word-wrap:break-word">%s</td><td align="center">%s</td><td align="center">%s</td><td align="center">%s</td></tr>' %(c[u'产品名称'],c[u'开始时间'],c[u'理财师昵称'],c[u'发布时间'],c[u'结束时间'])
    table += '</table>'
    return table

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092)

