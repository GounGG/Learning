#! -*- coding:utf-8 -*-

import json
from aliyunsdkcore import client
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest

'''
    获取所在区域的所有esc主机
'''
def get_sys_info():
    clt = client.AcsClient('LTAICYnd0O6o6Aey', 'weZ9tapicoQTbWJUliuzXJcG8p3lJj', 'cn-hangzhou')
    request = DescribeInstancesRequest.DescribeInstancesRequest()
    #request.set_PageNumber(1)   #设置页数
    request.set_PageSize(50)        #设置每页返回多少，默认为10条
    request.set_accept_format('json')
    result = json.loads(clt.do_action(request)).get('Instances').get('Instance')
    #result = clt.do_action(request)
    return result

print get_sys_info()

#for i in get_sys_info():
#    print i['Cpu']
#    print i['Memory']
#    print i['SecurityGroupIds']['SecurityGroupId']
#   exit(0)
    #print i['Status']  #运行状态
    #print i['PublicIpAddress']['IpAddress']      #获取服务器公网地址
    #print i['InnerIpAddress']['IpAddress']     #服务器所在地址和内网网IP
    #print i['InstanceName']     #服务器主机名
