#  -*- coding:utf-8 -*-

from flask import Flask,render_template,request
from aliSDK import *

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/input')
def input():
    n = request.args.get('username')
    #return n
    return render_template('input.html',username = n)

@app.route('/ali')
def ali():

    return value

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)