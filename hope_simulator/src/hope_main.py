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
    info = None
    def __init__(self, mus, timeout=100):
        # threading.Thread.__init__(self)
        self.mus = mus
        self.timeout = timeout
        self.recv_dict = {}
        self.send_dict = {}
        self.timeout_dict = {}
    def add_recv(self, name, handle):
        self.recv_dict[handle.fd] = {
            'name':name,
            'handle':handle,
            'time':time.time() * 1000,
        }

    def _manager(self):
        info = self.mus.info()
        en = False
        enid = False
        if self.info == None:
            en = enid = True
            print('en enid is true')
        else:
            for k, v in info.items():
                # if type(v) == dict:
                if k == 'music':
                    if 'musicId' in v :
                        if 'musicId' in self.info[k]:
                            if v['musicId'] != self.info[k]['musicId']:
                                print('music changed !!!')
                                en = enid = True
                        else:
                            en = enid = True
                elif k == 'pos':
                    if v - self.info[k] > 1000 or self.info[k] > v:
                        print('skip !!!')
                        en = True
                else:
                    if v != self.info[k]:
                        print(k, 'changed !!!', v)
                        en = True
            
        if en:
            print('update!!!!!!!!', enid)
            self.info = info.copy()
            for tmp in self.recv_dict.values():
                print(tmp['handle'].update)
                # if 'attribute' in tmp['handle']:
                if tmp['handle'].update != None:
                    tmp['handle'].update(enid)
        
        self.info['pos'] = info['pos']

        pass
        
    def run(self):
        while True:
            timestamp = time.time() * 1000
            in_list = []
            for fd, tmp in self.recv_dict.items():
                in_list.append(fd)
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
                pass
            # print('timeout !', time.time())
            self._manager()


def main(argv):
    try:
        mus = Music(argv[1])
        mus.show_list()
        hope_handle = Hope_loop(mus)
        stdhandle = Std_handle(mus)
        hope_handle.add_recv('std', stdhandle)
        tcphandle = Client_handle(mus, serv=True)
        # tcphandle = Client_handle(mus, serv=False)
        hope_handle.add_recv('client', tcphandle)
    except Exception as e:
        print('main error', e)
        R.exit()
    mus.start()
    hope_handle.run()
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