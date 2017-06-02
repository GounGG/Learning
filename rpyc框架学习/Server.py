# -*- coding;utf-8 -*-

import time
from rpyc import Service
from rpyc.utils.server import ThreadedServer
import sys

class TimeService(Service):
    def exposed_get_time(self):
        return time.ctime()
    def exposed_get_name(self):
        name = 'Goun'
        return name
    def exposed_get_sys(self):
        return __file__

s = ThreadedServer(TimeService,port=12233,auto_register=False)
s.start()
