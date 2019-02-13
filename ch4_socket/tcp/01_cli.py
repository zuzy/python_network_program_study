#!/usr/bin/python3
#coding:utf-8
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8088))
print('I`m a client')
for xx in ['abc', 'f服务d','h5Tq', '.']:
    s.send(xx.encode())
    str1 = s.recv(1024)
    str2 = str(str1, encoding='utf-8')
    print('get ', str2)
s.close()
