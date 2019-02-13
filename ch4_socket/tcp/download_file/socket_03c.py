#!/usr/bin/python3
#coding: utf-8
import socket
s = socket.socket()
s.connect(('127.0.0.1', 8888))
filename = '/bin/ls'
print('i wanna get ', filename)
s.send(filename.encode())
str1 = s.recv(1024).decode('utf-8')
if str1 == 'no':
    print('%s is not exist!' % filename)
else:
    s.send(b'I am ready')
    temp = filename.split('/')
    myname = 'my_' + temp[len(temp) - 1]
    size = 1024
    with open(myname, 'wb') as f:
        while True:
            data = s.recv(size)
            f.write(data)
            if len(data) < size:
                break
    print('The downloaded file is ', myname)
s.close()