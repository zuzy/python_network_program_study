#!/usr/bin/python3
# coding: utf-8
import socket, time, uuid, asyncio, select, sys, json, threading, struct, os
from halo_cmd import parse_cmd
from database import Database

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
    def add_recv(self, handle):
        self.recv_dict[handle.get_fd()] = {'handle':handle, 'timestamp': time.time()}
        # self.recv_dict[handle.get_fd()]['timestamp'] = time.time()
        print("add ok")
    def run(self):
        while True:
            timestamp = time.time()
            in_list = []
            for fd in self.recv_dict:
                in_list.append(fd)
                tmp = self.recv_dict[fd]
                if tmp['handle'].to  and ((timestamp - tmp['timestamp']) > tmp['handle'].to):
                    tmp['handle'].timeout()
                    tmp['timestamp'] = time.time()
            infds, outfds, errfds = select.select(in_list,[],[],self.timeout)
            if len(infds) > 0:
                for i in infds:
                    self.recv_dict[i]['handle'].recv()
            else:
                # print('timeout ', time.time())
                pass
        
halo_handle = Halo_loop()


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

def get_mac():
    node = uuid.uuid1()
    hex = node.hex
    mac_addr = hex[-12:]
    return mac_addr

class Udp_handle:
    group_ip = '224.0.0.1'
    send_port = 19601
    recv_port = 19602
    send_group_addr = (group_ip, send_port)
    recv_group_addr = (group_ip, recv_port)
    sock = None
    to = None
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        # local_ip = socket.gethostbyname(socket.gethostname())
        # 监听端口，已测试过其实可以直接bind 0.0.0.0；但注意不要bind 127.0.0.1不然其他机器发的组播包就收不到了
        self.sock.bind(('0.0.0.0', self.recv_port))
        # 加入组播组
        mreq = struct.pack("=4sl", socket.inet_aton(self.group_ip), socket.INADDR_ANY)
        self.sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)
        self.sock.setblocking(0)
        self.active_sending()
    
    def get_fd(self):
        return self.sock

    def active_sending(self, times = 3):
        send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        send_sock.settimeout(0)
        d = {'cmd': 'hopediscover', 'params':{'deviceid': get_mac()}}
        # ident 参数 表示打印 tab长度
        # data = json.dumps(d, indent=4) + '\n'
        data = json.dumps(d) + '\n'
        for i in range(times):
            send_sock.sendto(data.encode(), self.send_group_addr)
        send_sock.close()

    def recv(self):
        try:
            data, client = self.sock.recvfrom(1024)
            device_queue.add(str(data, encoding='utf-8'))
            os.system('clear')
            device_queue.dumps()
            print('please select a device [0-%d]' % (device_queue.length() - 1))
        except:
            print('err while udp recv!')
            pass

    def send(self):
        pass
    def timeout(self):
        pass


class Tcp_handle:
    sock = None
    to = None
    def __init__(self, addr, timeout = 30):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(addr)
        self.sock.setblocking(0)
        self.to = int(timeout)
        try:
            heartbeat = json.dumps({'cmd':'info', 'params':{}}) + '\n'
            # self.sock.send(str(heartbeat, 'utf-8'))
        except:
            print('sending !!!!!!! error')

    def get_fd(self):
        return self.sock

    def active_sending(self, times = 3):
        pass

    def dispatch_recv(self, data):
        try:
            d = Database()
            for x in data.split('\n'):
                x = x.strip()
                if len(x) > 0:
                    cmd = json.loads(x)
                    # print(cmd['cmd'])
                    db_str = d.dumps(cmd['cmd'])
                    print('db_str', db_str)
                    if db_str:
                        self.send(db_str + '\n')
        except Exception as e:
            print('dispatch error ',e)

    def recv(self):
        try:
            data = self.sock.recv(1024)
            data = data.decode().strip()
            print('tcp recv ', data)
            
            self.dispatch_recv(data)
        except Exception as e:
            print('tcp recv error ', e)
    def send(self, data):
        try:
            self.sock.send(data.encode())
        except:
            print('tcp send error')
    def timeout(self):
        heartbeat = json.dumps({'cmd':'info', 'params':{}}) + '\n'
        print(heartbeat)
        self.send(heartbeat)

        
        pass


class Std_handle:
    to = None

    def __init__(self):
        self.fd = sys.stdin
    def get_fd(self):
        return self.fd
    def active_sending(self, times = 3):
        pass
    def recv(self):
        try: 
            cmd = self.fd.readline().strip('\n')
            print("keyboard cmd: ", cmd)
            try:
                index = int(cmd)
                if index >= 0 and index < device_queue.length():
                    addr = device_queue.sel(index)
                    print('start to connect ', addr)
                    self.tcp_handle = Tcp_handle(addr)
                    halo_handle.add_recv(self.tcp_handle)
                else:
                    print('the index is out of range')
            except:
                s = parse_cmd(cmd)
                print(s)
                if s:
                    self.tcp_handle.send(s)
        except:
            print('keyboard input error')
    def send(self):
        pass
    def timeout(self):
        pass


def main(argv):

    try:
        # halo_handle = Halo_loop()
        udp_handle = Udp_handle()
        print('')
        halo_handle.add_recv(udp_handle)
        print('')
        std_handle = Std_handle()
        print('')
        halo_handle.add_recv(std_handle)
        print('')

        halo_handle.start()
    except Exception as e:
        print('error! ', e)
        R.exit()
    
    while True:
        try:
            time.sleep(1000)
        except:
            R.exit()

if __name__ == "__main__":
    main(sys.argv)