#!/usr/bin/python3
#coding: utf-8
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_addr = ('127.0.0.1', 8090)
s.sendto(b'CPU INFO', s_addr)
(data_b, addr) = s.recvfrom(1024)
if addr == s_addr:
    data_b = data_b.decode('utf-8')
    data_list = data_b.split('\n')
    print('cpu usage is ', data_list[0])
    print('%-20s%-5s%-10s' % ('name', 'pid', 'cpu usage'))
    data_list = data_list[1: -1]
    for x in data_list:
        yy = x.split(',')
        print('%-20s%-5s%-10s' % (yy[0], yy[1], yy[2]))
s.close()
        
