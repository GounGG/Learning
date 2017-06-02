# -*- codinf:utf-8 -*-

import rpyc
c=rpyc.connect('localhost',12233)

print c.root.get_time()
c.close()