# -*- coding:utf-8 -*-

from tasks import add

result = add.delay(6, 7)
print result