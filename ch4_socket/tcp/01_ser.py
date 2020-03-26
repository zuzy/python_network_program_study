#!/usr/bin/python3
#coding:utf-8
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('127.0.0.1', 8088))

s.setblocking(1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind(('0.0.0.0', 0))

# s.bind((self._host, self._port))
s.bind(('0.0.0.0', 0))
print(s.getsockname())
print('listening on port:', s.getsockname()[1])


s.listen(1)
print('Waiting for connection')
(conn, addr) = s.accept()
print(conn, '\t', addr)

while True:
    str1 = conn.recv(1024)
    str2 = str(str1, encoding='utf-8')
    print('recv: ', str2)
    str3 = str2.upper()
    conn.send(str3.encode())
    if str2 == '.':
        break
conn.close()
s.close()