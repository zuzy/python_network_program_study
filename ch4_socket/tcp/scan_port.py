#!/usr/bin/python3
#coding: utf-8
import socket
ip = '127.0.0.1'
for port in range(0, 9000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((ip, port))
    if result == 0:
        print('port %d is opened' % port)
    s.close()
