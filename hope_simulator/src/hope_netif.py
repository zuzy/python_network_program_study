#!/usr/bin/python3
# coding: utf-8
import uuid
'''
uuid.uuid1 （当前时间戳 - 随机数 - mac）组成
uuid.hex 转成16进制字符串
'''
import psutil


class Net_info():
    def __init__(self, adapter='eth0'):
        self.adapter = adapter
        info = psutil.net_if_addrs()
        net = info[self.adapter]
        self.ip = net[0].address
        self.mac = net[2].address
    def get_sn(self):
        return '73001804123020'
        # return '74001806140063'

    def get_uuid(self):
        return '9FCDE6963E830630F13B285B5417DB18'

    
nf = Net_info()
print(nf.ip, '===', nf.mac)