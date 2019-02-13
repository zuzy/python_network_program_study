#!/usr/bin/python3
# coding: utf-8
import psutil
info = psutil.net_if_addrs()
# print(type(info), info)
net1 = info['enp5s0']
print(type(net1), net1)
pack = net1[2]
print(type(pack), pack)
print(pack.address)



