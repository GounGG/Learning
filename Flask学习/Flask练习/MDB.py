#  -*- coding:utf-8 -*-

'''
    获取阿里云ecs主机的基本情况，并入库
    表结构：CREATE TABLE `f_ecs` (
  `f_id` int(11) NOT NULL,
  `f_name` varchar(50) DEFAULT NULL,
  `f_public_ip` varchar(50) DEFAULT NULL,
  `f_ip` varchar(50) DEFAULT NULL,
  `f_cpu` int(4) DEFAULT NULL,
  `f_memory` int(8) DEFAULT NULL,
  `f_time` datetime DEFAULT NULL,
  PRIMARY KEY (`f_id`),
  KEY `f_name` (`f_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

import time
import pymysql
import aliSDK
conn = pymysql.connect(host='192.168.1.202',user='root', passwd='20131220', db='ali', charset='utf8')
cur = conn.cursor()

#查询
def Query(cur,sql):
    cur.execute(sql);
    return cur.fetchall();

#插入
def Insert(cur,sql):
    cur.execute(sql);
    conn.commit()
    return (cur);

#update
def Update(cur,sql):
    cur.execute(sql);
    conn.commit()
    return (cur);

for i in  aliSDK.get_sys_info():
    name = i['InstanceName']    #获取主机名
    ip = i['PublicIpAddress']['IpAddress']  #获取公网ip
    ip2 = i['InnerIpAddress']['IpAddress']  #内网ip
    cpu = i['Cpu']  #cpu个数
    mem = i['Memory']   #内存大小
    hostname = Query(cur,r"SELECT f_name,f_public_ip,f_ip,f_cpu,f_memory from t_ecs where f_ip='%s';" %(ip2[0]))
    if hostname:
        if hostname[0][2] != ip2[0] or hostname[0][3] != cpu or hostname[0][4] != mem:
            if ip:          #因为公网ip可能没有，所以在有公网ip和无公网ip中，sql语句会略微不同
               Update(cur,r"UPDATE t_ecs SET `f_public_ip`='%s', `f_ip`='%s', `f_cpu`='%s', `f_memory`='%s', `f_time`=now() WHERE f_name='%s';" %(ip[0], ip2[0], cpu, mem, name))
            else:
               Update(cur,r"UPDATE t_ecs SET `f_ip`='%s', `f_cpu`='%s', `f_memory`='%s', `f_time`=now() WHERE f_name='%s';" %(ip2[0], cpu, mem, name))
    else:
        if ip:
            Insert(cur, r"INSERT INTO t_ecs (`f_name`, `f_public_ip`, `f_ip`, `f_cpu`, `f_memory`, `f_time`) VALUES ('%s', '%s', '%s', %s, %s, now());" %(name, ip[0], ip2[0], cpu, mem))
        else:
            Insert(cur, r"INSERT INTO t_ecs (`f_name`, `f_ip`,`f_cpu`, `f_memory`, `f_time`) VALUES ('%s', '%s', %s, %s, now());" %(name , ip2[0], cpu, mem))
cur.close()
conn.close()