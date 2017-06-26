# -*- coding:utf-8 -*-

import web

render = web.template.render('templates/')

# 创建URL结构，第一部分，使我们的URL，支持正则表达式，第二部分是接收的请求类
urls = (
  '/(.*)', 'index'
)

# 创建一个index类，常见的有GET和POST方法
class index:
    def GET(self):
        i = web.input(name='Goun')
        #name = '方记普'
        #return name
        return render.index(i.name)

if __name__ == "__main__":
    # 创建基于我们提交的URL列表的application（应用）
    app = web.application(urls, globals())
    app.run()