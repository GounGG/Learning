# -*- coding:utf-8 -*-

from flask import Flask

#实例化Flask，__name__对应的是实际导入的名称，也就是本文件名
app = Flask(__name__)

@app.route('/')
def index():
    return "主页"
@app.route('/hello')

def hello():
    return "hello world"

#变量规则      使用<>来标记，如：<username>  不限制接收的字符类型   <int:userid>    前面的int限定了变量接收字符类型
#int    整数型
#float  同int一样，但是接收浮点数
#path   和默认的相识，但也接收斜线
@app.route('/user/<username>')
def user_name(username):
    #显示用户的名字
    return 'User %s' % username

@app.route('/user/<int:userid>')
def user_id(userid):
    #显示用户id,只显示用户提交的整数型ID
    return r'user:方记普 id:%i' % userid

@app.route('/fjp/')
def fjp():
    return 'The is fjp/'

@app.route('/about')
def about():
    return 'The is about'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)