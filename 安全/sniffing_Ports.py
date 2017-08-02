#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import nmap
import argparse

scan_data=[]
input_scan = raw_input('Please input hosts:')
ports = raw_input('Please input port:')
scan_data = input_scan.split(" ")
if len(scan_data) == 0:
  print "Input errores.example \"192.168.1.0/24|192.168.0.1-100/192.168.0.1 192.168.0.2"
  sys.exit(0)


# scan_data=['121.41.51.189', '115.29.233.142']
for hosts in scan_data:
  try:
    nm = nmap.PortScanner()
  except nmap.nmap.PortScannerError:
# sys.exc_info()[0]  获取当前正在处理的异常类
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(0)
  except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(0)

  try:
    nm.scan(hosts=hosts, arguments=' -v -sS -p'+str(ports))
  except Exception,e:
    print "Scan error:" + str(e)

  for host in nm.all_hosts():
    print('-----------------------------------------------------------------------------')
    print('Host: %s(%s)' %(host,nm[host].hostname()))
    print('State :%s' %nm[host].state())
    for proto in nm[host].all_protocols():
      print('-----------')
      print('Protocol : %s' % proto)
      lport = nm[host][proto].keys()
      lport.sort()
      for port in lport:
        print('port : %s\tstate : %s' % (port,nm[host][proto][port]['state']))
