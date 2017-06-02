#!/bin/usr/env python
# -*- coding:utf-8 -*-

class pp():
    def __init__(self, name):
        self.name=name
    def __del__(self):
        print self.name
        print 234
    def run(self):
        print 'Hello,my name is',self.name

class qq(pp):
    def __init__(self,age):
        self.age=age
    def q(self):
        print 12345
    def run(self):
        self.q()
        print 'Hello,my age is',self.age





q = qq('18')
q.run()
