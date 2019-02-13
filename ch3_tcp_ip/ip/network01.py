#!/usr/bin/python3
# coding: utf-8
import psutil
info = psutil.net_if_addrs()
net1 = info['enp5s0']
net2 = info['lo']

print(net1[0])
print(net1[1])

print(net1[0].address)
print(net1[1].address)


import netifaces
info = netifaces.gateways()
print(type(info), info)
print(info['default'][2][0])