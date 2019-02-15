#!/usr/bin/python3
# coding: utf-8
import socket, time, uuid, asyncio, select, sys, json, threading, struct, os

class R():
    def __init__(self):
        pass
    @staticmethod
    def exit():
        os.system("kill -9 " + str(os.getpid())) #杀掉进程


class Halo_loop(threading.Thread):
    recv_dict = {}
    send_dict = {}
    timeout = 0
    def __init__(self, timeout = 1):
        threading.Thread.__init__(self)
        self.timeout = timeout
    def add_recv(self, fd, cb):
        self.recv_dict[fd] = cb
        print("add ok")
    def run(self):
        while True:
            in_list = []
            for fd in self.recv_dict:
                in_list.append(fd)
            infds, outfds, errfds = select.select(in_list,[],[],self.timeout)
            if len(infds) > 0:
                for i in infds:
                    for fd in self.recv_dict:
                        if fd is i:
                            self.recv_dict[fd](fd)
                            pass
                            break
            else:
                # timeout
                # print('timeout')
                pass
    
        
halo_handle = Halo_loop()

def get_mac():
    node = uuid.uuid1()
    hex = node.hex
    mac_addr = hex[-12:]
    return mac_addr

# 组播组IP和端口
group_ip = '224.0.0.1'
send_port = 19601
recv_port = 19602

send_group_addr = (group_ip, send_port)
recv_group_addr = (group_ip, recv_port)

def sender():
    send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    send_sock.settimeout(0)
    d = {'cmd': 'hopediscover', 'params':{'deviceid': get_mac()}}
    # ident 参数 表示打印 tab长度
    # data = json.dumps(d, indent=4) + '\n'
    data = json.dumps(d) + '\n'
    # print(data)
    send_sock.sendto(data.encode(), send_group_addr)
    # print('send ok')
    send_sock.close()

class Dev_queue:
    def __init__(self) :
        self.devs = []
    def add(self, s):
        print('json load')
        cmd = json.loads(s)
        print('json load ok')
        for x in self.devs:
            if x['hopeid'] == cmd['params']['hopeid']:
                return
        self.devs.append(cmd['params'])
    def dumps(self):
        print('%-4s%-25s%-25s%-10s%-10s' % ('id', 'MAC', "IP", "PORT", 'MODEL'))
        for i, x in enumerate(self.devs):
            print('%-4s%-25s%-25s%-10s%-10s' % (i, x['hopeid'], x['hopeip'], x['hopeport'],x['model']))
    def length(self):
        return len(self.devs)
    def sel(self, n):
        return (self.devs[n]['hopeip'], int(self.devs[n]['hopeport']))


device_queue = Dev_queue()

def receiver():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    # local_ip = socket.gethostbyname(socket.gethostname())
    # 监听端口，已测试过其实可以直接bind 0.0.0.0；但注意不要bind 127.0.0.1不然其他机器发的组播包就收不到了
    sock.bind(('0.0.0.0', recv_port))
    # 加入组播组
    mreq = struct.pack("=4sl", socket.inet_aton(group_ip), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)
    sock.setblocking(0)
    return sock

def udp_recv(fd):
    try:
        data, addr = fd.recvfrom(1024)
        print(data)
        device_queue.add(str(data, encoding='utf-8'))
        os.system('clear')
        device_queue.dumps()
        print('please select a device [0-%d]' % (device_queue.length() - 1))
    except:
        print('err while recv!')
        pass

def tcp_receiver(addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(addr)
    sock.setblocking(0)
    print(sock)
    return sock

def tcp_recv(fd):
    try:
        data = fd.recv(1024)
        data = str(data, 'utf-8')
        print("tcp recv ", data)
    except:
        print('tcp recv error !')

def keyboard_receiver():
    return sys.stdin

def keyboard_recv(fd):
    try:
        cmd = fd.readline().strip()
        print('keyboard input ',cmd)
        index = int(cmd)
        if index >= 0 and index < device_queue.length():
            addr = device_queue.sel(index)
            print('start to connect ', addr)
            halo_handle.add_recv(tcp_receiver(addr), tcp_recv)
        else: 
            print('out of range!')
    except:
        print('error while keyboard')


if __name__ == "__main__":
    try:
        # halo_handle = Halo_loop()
        halo_handle.add_recv(receiver(), udp_recv)
        halo_handle.add_recv(sys.stdin, keyboard_recv)
        halo_handle.start()
    except Exception as e:
        print('error! ', e)
        R.exit()
    for i in range(0, 3):
        sender()
        print('send ok')

    while True:
        try:
            time.sleep(1000)
        except:
            R.exit()