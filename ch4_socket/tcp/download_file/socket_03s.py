#!/usr/bin/python3
#coding:utf-8
import socket
import os
def sendfile(conn):
    str1 = conn.recv(1024)
    filename = str(str1, encoding='utf-8')
    print('client requests my file ', filename)
    if os.path.exists(filename):
        print("i have %s, begin to down load" % filename)
        conn.send(b'yes')
        conn.recv(1024)
        size = 1024
        with open(filename, 'rb') as f:
            while True:
                data = f.read(size)
                conn.send(data)
                if len(data) < size:
                    break
        print('%s is downloaded successfully!' % filename)
    else:
        print('I have no ', filename)
        conn.send(b'no')
    conn.close()

s = socket.socket()
s.bind(('127.0.0.1', 8888))
s.listen(1)
print("waiting for connection")
while True:
    (conn, addr) = s.accept()
    sendfile(conn)