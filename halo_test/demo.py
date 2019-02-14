#!/usr/bin/python3
# coding: utf-8
import time
import socket

# 组播组IP和端口
mcast_group_ip = '224.0.0.1'
mcast_group_port = 19601

def sender():
    # 建立发送socket，和正常UDP数据包没区别
    send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    # 每十秒发送一遍消息
    while True:
        message = "this message send via mcast !"
        # 发送写法和正常UDP数据包的还是完全没区别
        # 猜测只可能是网卡自己在识别到目的ip是组播地址后，自动将目的mac地址设为多播mac地址
        send_sock.sendto(message.encode(), (mcast_group_ip, mcast_group_port))
        print('send ok')
        time.sleep(10)


import struct
import time
import socket

# 组播组IP和端口
mcast_group_ip = '234.2.2.2'
mcast_group_port = 23456

def receiver():
    # 建立接收socket，和正常UDP数据包没区别
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    # 获取本地IP地址
    local_ip = socket.gethostbyname(socket.gethostname())
    # 监听端口，已测试过其实可以直接bind 0.0.0.0；但注意不要bind 127.0.0.1不然其他机器发的组播包就收不到了
    sock.bind((local_ip, mcast_group_port))
    # 加入组播组
    mreq = struct.pack("=4sl", socket.inet_aton(mcast_group_ip), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)

    # 允许端口复用，看到很多教程都有没想清楚意义是什么，我这里直接注释掉
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 设置非阻塞，看到很多教程都有也没想清楚有什么用，我这里直接注释掉
    # sock.setblocking(0)
    while True:
        try:
            message, addr = sock.recvfrom(1024)
            print(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}: Receive data from {addr}: {message.decode()}')
        except :
            print("while receive message error occur")


if __name__ == "__main__":
    receiver()

    
if __name__ == "__main__":
    sender()