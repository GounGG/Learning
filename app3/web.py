# -*- coding:utf-8 -*_
from flask import Flask,request,render_template
import pymysql
app = Flask(__name__)

conn = pymysql.connect(host='192.168.1.202',user='root', passwd='20131220', db='log',  charset='utf8')
cur = conn.cursor()
def SQL(cur,sql):
    cur.execute(sql);
    return (cur);

@app.route('/')
def index():
    table = '<table border="1" width="100%" style="table-layout:fixed" >'
    #$table += '<style>table td{text-align:center;}</style>'
    table += '<tr align="center"><td>IP</td><td>URL</td><td>status</td><td>sum</td><td>DATE</td></tr>'
    a=SQL(cur,'select * from log order by sum desc limit 20;')
    for c in a:
        table += '<tr><td align="center">%s</td><td style="word-wrap:break-word">%s</td><td align="center">%s</td><td align="center">%s</td><td align="center">%s</td></tr>'%c
    table += '</table>'
    return table

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9092)