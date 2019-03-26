#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json, sys, os, re, binascii
from hope_post  import Hp_post
from hope_netif import *
from hope_music import *
from hope_utils import *
import qrcode

class Regist(Net_info, Hp_post):
    apis = {
        'mac' : '/hopeApi/upgrade/mac',
        'info' : '/hopeApi/device/register',
        'attr' : '/hopeApi/device/status',
        'music' : '/hopeApi/music/initial',
    }
    # def __init__(self):
    def __init__(self, cid='881256532942016512', sid='750837261197414400', key='0CF9DE03AF1C46F9A970AB27120A91D2', ver='1.0', uri='http://192.168.2.9:8080'):
        Net_info.__init__(self)
        Hp_post.__init__(self, cid, sid, key, ver, uri)
        # print(self.mac)

    def regist_mac(self):
        tmp = {
            # 'deviceGuid':'10:D0:7A:74:8C:1D',
            'deviceGuid':self.mac,
            'deviceSN':self.get_sn(),
        }
        print(self.post(tmp, api=self.apis['mac']))
        # self.post(tmp, api=self.apis['mac'])
    
    
    def cover(self):
        nref = int(self.ref)
        rref = self.ref[::-1]
        if nref > 0:
            l = len(rref)
            for i in range(l, 20):
                rref += 'A'
        else:
            rref = rref[0:-1]
            l = len(rref)
            for i in range(l, 20):
                rref += 'F'
        r = rref[::-1]
        self.cover_ref = r
        self.ref_code = [int(r[i]+r[i+1], 16) for i in range(len(r)) if i % 2 == 0]
        # self.ref_code = [chr(int(r[i]+r[i+1], 16)) for i in range(len(r)) if i % 2 == 0]
        self.ref_bytes = bytes(self.ref_code)
        # print('%s' % ('abc' + str(self.ref_bytes)))

    def regist_info(self):
        tmp = {
            'comName':'HOPE',
            'deviceSN':self.get_sn(),
            'deviceName':'HOPE-Q3',
            'deviceCata':'Q3',
            'firmVersion':'ats3605-debug-0.1',
            'softVersion':'0.0.1',
            'macAddress':self.mac,
            'playerType':'_test',
            'playerVersion':'1.0',
            'bgType':'master',
            'bgVersion':'1.0.0',
            'upgradeChannel':'release-HOPE-Q3',
            'deviceDrive':'ats3605',
            'parentId':'753396045774098432',
        }
        code, body = self.post(tmp, api=self.apis['info'])
        if code == 200:
            ref = json.loads(body)
            if ref['code'] == 100000:
                self.auth = str(ref['object']['authCode'])
                self.ref = str(ref['object']['refrenceId'])
        print(self.auth, self.ref)
        self.cover()


    def regist_attr(self):
        tmp = {
            'deviceId':self.ref,
            'profile': {
                'status':1,
                'play':1,
                'control':1,
                'skip':1,
                'idvol':1,
                'mute':1,
                'setvol':1,
                'source':1,
                'effect':1,
                'model':1,
                'locale':1,
            }
        }
        print(self.post(tmp, api=self.apis['attr']))
        self.post(tmp, api=self.apis['attr'])
    
    def regist_music(self, playlist):
        tmp = {
            'authCode':self.auth,
            'deviceId':self.ref,
            'list':playlist
        }
        print(json.dumps(tmp, ensure_ascii=False, indent=4))
        print(self.post(tmp, api=self.apis['music']))

    def regist_all(self):
        self.regist_mac()
        self.regist_info()
        self.regist_attr()
        code = {
            'comName':'HOPE',
            'deviceCata':'Q3',
            'deviceName':'HOPE-Q3',
            'parentId':'753396045774098432',
            'playerType':'_test',
            'deviceSN':self.get_sn(),
            # 'uuid':'9FCDE6963E830630F13B285B5417DB18',
        }
        print('qrcode :\n', json.dumps(code, ensure_ascii=False, indent=4))
        img = qrcode.make(json.dumps(code, ensure_ascii=False))
        print(type(img), img)
        img.save('dev_addition.png')
        



if __name__ == '__main__':
    # hp = Hp_post()
    # nf = Net_info()
    # s = {"deviceGuid":"00:00:6C:06:A6:29","deviceSN":"70368170428025"}
    # s['deviceGuid'] = nf.mac
    # print(json.dumps(s, indent=4))
    # print(hp.post(s))

    reg = Regist()
    # reg.regist_mac()
    # reg.regist_info()
    # reg.regist_attr()
    reg.regist_all()
    mus = Music(sys.argv[1])
    reg.regist_music(mus.playlist)
    
    # mus = Music(sys.argv[1])