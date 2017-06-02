# -*- coding:utf-8 -*-

import time
import winsound

file='0608.wav'

def play():
    sound = winsound.PlaySound(file, winsound.SND_FILENAME) #立即返回，支持异步播放

if __name__ == '__main__':
    n = 1
    while True:
        t = int(time.strftime('%H%M',time.localtime(time.time())))
        print "第%s检测！         %i" %(n, t)
        if t == 1330 or t == 1600 or t == 1900 or t == 230 or t == 930 or t == 1130:
            play()
        time.sleep(40)
        n = n + 1
