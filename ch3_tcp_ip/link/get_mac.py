#!/usr/bin/python3
# coding: utf-8
import uuid
'''
uuid.uuid1 （当前时间戳 - 随机数 - mac）组成
uuid.hex 转成16进制字符串
'''
node = uuid.uuid1()
print('type(node) = ', type(node))
print(node)
hex = node.hex
print(type(hex), hex)
mac_addr = hex[-12:]
print('mac addr: ', mac_addr)

node = uuid.uuid4()
print(node)