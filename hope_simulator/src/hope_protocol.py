#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket, time, select, sys, json, threading, os
from hope_regist import Regist
from hope_utils import *
from halo_cmd import *
from halo_parse import *

class Std_handle(hp_utils):
    to = None
    def __init__(self, music):
        hp_utils.__init__(self)
        self.fd = sys.stdin
        self.mus = music
        self.parse = Halo_parse(self.mus)
    def recv(self):
        try:
            cmd = self.fd.readline().strip('\n')
            print('cmd: ', cmd)
        except Exception as e:
            print('catch cmd error: ', e)
            pass
        s = parse_cmd(cmd)
        print(s)
        self.parse.parse(s)

class Client_handle(Regist, hp_utils):
    # type of device!
    tag = 0x01
    def __init__(self, music, timeout=30000, serv=False):
        self.mus = music
        self.to = timeout
        print('111')
        hp_utils.__init__(self)
        Regist.__init__(self)
        self.regist_all()
        print('111')
        if serv:
            self.host, self.port = 'open.nbhope.cn', 6666
        else:
            self.host, self.port = '192.168.2.9', 8888
        self.conn()

    def conn(self):
        self.fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.fd.connect((self.host, self.port))
        self.fd.setblocking(0)
        self.identify()

    def identify(self):
        tmp = {
            'code':self.auth
        }
        self.fd.send((self.package(0x04, json.dumps(tmp))))

    def package(self, cmd, body):
        ret = self.toword(cmd)
        ret += self.tobyte(self.tag)
        if type(body) == str:
            body = body.encode(encoding='ascii')
        # length is hex length not the char length! .....fuck b-e
        ret += self.toword(len(body) * 2)
        ret += self.ref_bytes
        ret += body
        chk = 0
        for r in ret:
            chk ^= r
        print('chk final %x' %chk)
        ret += self.tobyte(chk)
        print(ret)
        ret = self.escape(ret)
        print('es', ret)
        ret += b'\x7e'
        ret = b'\x7e' + ret
        print('pkg', ret)
        return ret
    
    def dispatch(self, data):
        div = divide(data)
        m = iter(div)
        cmd = [x for x in m]
        return cmd[1], cmd[5]

    def recv(self):
        try:
            data = self.fd.recv(1024)
            print('recv data', data)
            d = self.unescape(data)
            cmd, body = self.dispatch(d)
            print(body[:-1].decode())

        except Exception as e:
            print(e)
            sys.exit()


            