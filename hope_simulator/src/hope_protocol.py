#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket, time, select, sys, json, threading, os
from hope_regist import Regist
from hope_utils import *
from halo_cmd import *
from halo_parse import *
from hope_parse import *

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
    def update(self, enid):
        info = self.mus.info()
        json.dump(info, sys.stdout, ensure_ascii=False, indent=4)

class Client_handle(Regist, hp_utils):
    # type of device!
    tag = 0x01
    cmd = {
        'common':   0x01,
        'heart':    0x02,
        'exit':     0x03,
        'identify': 0x04,
        'ctrl':     0x10,
        'list_new': 0x20,
        'list_create':  0x30,
        'list_rm':  0x40,
        'list_add': 0x50,
        'list_rmsong':  0x80,
        'list_change':  0x125,

        'area_scan':    0x60,
        'area_ctrl':    0x70,
        'area_vol': 0x195,

        'scene_new':    0x90,
        'scene_rule':   0x100,
        'scene_rm': 0x185,

        'unbind':   0x215,
        'event':    0x230,
        'tts':  0x250,
        'ttschk':   0x260,
    }

    def __init__(self, music, timeout=30000, serv=False):
        self.mus = music
        self.parse = Hope_parse(self.mus)
        self.to = timeout
        if serv:
            Regist.__init__(self, uri='http://open.nbhope.cn')
            self.host, self.port = 'open.nbhope.cn', 6666
        else:
            Regist.__init__(self)
            self.host, self.port = '192.168.2.9', 8888
        hp_utils.__init__(self)
        self.regist_all()
        # self.regist_music(self.mus.playlist)
        self.update_playlist()
        self.conn()
        print('connok')

    def update_playlist(self):
        playlist = []
        for v in self.mus.playlist:
            tt = v.copy()
            del tt['freq']
            del tt['musicSize']
            del tt['path']
            playlist.append(tt)
        json.dump(playlist, sys.stdout, ensure_ascii=False, indent=4)
        self.regist_music(playlist)

    def conn(self):
        self.fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.fd.connect((self.host, self.port))
        self.fd.setblocking(0)
        self.identify()
        self.heartbeat()

    def identify(self):
        tmp = {
            'code':self.auth
        }
        self.fd.send(self.package(self.cmd['identify'], json.dumps(tmp)))

    def heartbeat(self):
        self.fd.send(self.package(self.cmd['heart'], ''))

    def update_status(self):
        self.fd.send(self.package(self.cmd['ctrl'], 'status'))
        pass

    def package(self, cmd, body):
        ret = self.toword(cmd)
        ret += self.tobyte(self.tag)
        if type(body) == str:
            body = body.encode(encoding='ascii')
        # length is hex length not the char length! .....fuck b-e
        print('length is %d', len(body) * 2)
        ret += self.toword(len(body) * 2)
        ret += self.ref_bytes
        ret += body
        chk = 0
        for r in ret:
            chk ^= r
        ret += self.tobyte(chk)
        ret = self.encode(ret)
        ret += b'\x7e'
        ret = b'\x7e' + ret
        return ret
    
    def dispatch(self, data):
        div = divide(data)
        m = iter(div)
        cmd = [x for x in m]
        return cmd[1], cmd[5], cmd[6]

    def recv(self):
        try:
            data = self.fd.recv(1024)
            # print('recv data', data)
            if len(data) == 0:
                print('connection error!')
                R.exit()
            d = self.unescape(data)
            while len(d) > 0:
                cmd, body, d = self.dispatch(d)
                if body and len(body) > 0:
                    body = body[:-1].decode()
                    print('%x' % cmd, body)
                    self.parse.parse(cmd, body)
            print('parse end!!!')
        except Exception as e:
            print(e)
            sys.exit()
    
    def timeout(self):
        # print('hope tcp timeout !!!')
        self.heartbeat()
        
    def update(self, id=False):
        state = self.mus.info()
        tmp = {
            'status':True,
            'error':5000,
            'profile':{
                'status':state['state'],
                'skip':state['pos'],
                'setvol':int(state['vol']*100),
                'model':state['loop'],
                'source':1,
                'locale':0,
            }
        }
        if id:
            if 'musicId' in state['music']:
                tmp['profile']['play'] = tmp['musId'] = state['music']['musicId']
            if 'musicName' in state['music']:
                tmp['music'] = state['music']['musicName']
        pkg = self.package(self.cmd['ctrl'], json.dumps(tmp))
        print("tcp update body", pkg)
        self.fd.send(pkg)
        # self.fd.send(self.package(self.cmd['ctrl'], json.dumps(tmp)))


            