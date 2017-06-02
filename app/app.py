#  -*- coding:utf-8 -*-

from flask import Flask,render_template,request
import recommend

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/')
def search():
    n=request.args.get('user')
    dic = recommend.recomment(n)
    return render_template('search.html',Data=dic)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)