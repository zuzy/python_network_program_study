#!/usr/bin/python3
# -*- utf-8 -*-

import os, re, json, time, select, threading
from hope_regist import Regist
from hope_utils import *
from halo_cmd import *
from hope_protocol import *
from hope_music import *

# class Hope_loop(threading.Thread):
class Hope_loop():
    def __init__(self, timeout=100):
        # threading.Thread.__init__(self)

        self.timeout = timeout
        self.recv_dict = {}
        self.send_dict = {}
    def add_recv(self, name, handle):
        self.recv_dict[handle.fd] = {
            'name':name,
            'handle':handle,
            'time':time.time() * 1000,
        }
    def run(self):
        while True:
            timestamp = time.time()
            in_list = []
            for fd in self.recv_dict.keys():
                in_list.append(fd)
                tmp = self.recv_dict[fd]
                if tmp['handle'].to and tmp['handle'].to > 0 and ((timestamp - tmp['time'])) > tmp['handle'].to:
                    tmp['handle'].timeout()
                    tmp['time'] = time.time() * 1000
            
            try:
                infds, outfds, errfds = select.select(in_list, [], [], self.timeout / 1000)
            except Exception as e:
                print(e)
                R.exit()
            if len(infds) > 0:
                for i in infds:
                    self.recv_dict[i]['handle'].recv()
            else: 
                # print('timeout !', time.time())
                pass

def main(argv):
    try:
        hope_handle = Hope_loop()
        mus = Music(argv[1])
        mus.show_list()
        stdhandle = Std_handle(mus)
        hope_handle.add_recv('std', stdhandle)
        tcphandle = Client_handle(mus)
        hope_handle.add_recv('client', tcphandle)
    except Exception as e:
        print('main error', e)
        R.exit()
    hope_handle.run()
    mus.start()
    # while True:
    #     try:
    #         time.sleep(100)
    #     except:
    #         R.exit()


if __name__ == '__main__':
    # cli = Client_handle()
    # # re = cli.package(0x8034, "12345\x7e\x7d")
    # while True:
    #     # time.sleep(1)
    #     cli.recv()
    main(sys.argv)