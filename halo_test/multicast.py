#!/usr/bin/python
#coding: utf-8

# cannot work in python3 ?!

import threading, sys, os, socket, time, struct, select
import uuid, json

class R():
    def __init__(self):
        pass
    @staticmethod
    def exit():
        os.system("kill -9 " + str(os.getpid())) #杀掉进程

def get_mac():
    node = uuid.uuid1()
    hex = node.hex
    mac_addr = hex[-12:]
    return mac_addr

class MulticastClient(threading.Thread):
    def __init__(self, port = 19602, destaddr = ('224.0.0.1', 19601)):
        threading.Thread.__init__(self)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # local_ip = socket.gethostbyname(socket.gethostname())
        sock.bind(('0.0.0.0', port))

        mreq = struct.pack("=4sl", socket.inet_aton('224.0.0.1'), socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)

        
        sock.setblocking(0)
        self.sock = sock
        self.destaddr = destaddr
        self.r = 1
        print('init ok')
    def run(self):
        sock = self.sock
        packSize = 1024
        devices = Dev_queue()
        # while(self.r):
        for i in range(0, 3):
            try:
                d = {'cmd':'hopediscover'}
                d['params'] = {'deviceid':get_mac()}
                s = json.dumps(d) + '\n'
                # print('send to, ', s)
                sock.sendto(s.encode(), self.destaddr)
                # print('send ok')
                while True:
                    infds, outfds, errfds = select.select([sock,],[],[],1)
                    if len(infds) > 0:
                        data, client = sock.recvfrom(packSize)
                        # print ("MulticastClient recv data: ", data, "client: ", client)
                        devices.add(data)

                    else:
                        # print('timeout !')
                        break
            except:
                break
        devices.dumps()
        # print(devices.dumps())

class Dev_queue:
    def __init__(self) :
        self.devs = []
    def add(self, s):
        # print('add ', s)
        cmd = json.loads(s)
        # print(cmd)
        for x in self.devs:
            if x['hopeid'] == cmd['params']['hopeid']:
                return
        self.devs.append(cmd['params'])
    def dumps(self):
        for i, x in enumerate(self.devs):
            print (i, '\t', x)

def main(argv):
    try:
        mserver = MulticastClient()
        mserver.start()
    except Exception as e:
        print("error: ", e)
        R.exit()
    while 1:
        try:
            time.sleep(1000)
        except :
            R.exit()

if __name__ == "__main__":
    main(sys.argv)
