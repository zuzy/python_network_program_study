#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json, sys, os, re
from hope_post  import Hp_post
from hope_netif import *
from hope_music import *

class Regist(Net_info, Hp_post):
    apis = {
        'mac' : '/hopeApi/upgrade/mac',
        'info' : '/hopeApi/device/register',
        'attr' : '/hopeApi/device/status',
        'music' : '/hopeApi/music/initial',
    }
    def __init__(self):
        Net_info.__init__(self)
        Hp_post.__init__(self)
        # print(self.mac)

    def regist_mac(self):
        tmp = {
            'deviceGuid':self.mac,
            'deviceSN':'70368170428025',
        }
        print(self.post(tmp, api=self.apis['mac']))
        # self.post(tmp, api=self.apis['mac'])
    
    def regist_info(self):
        tmp = {
            'comName':'HOPE',
            'deviceSN':'73001804123020',
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
        # self.post(tmp, api=self.apis['attr'])
    
    def regist_music(self, playlist):
        tmp = {
            'authCode':self.auth,
            'deviceId':self.ref,
            'list':playlist
        }
        print(json.dumps(tmp, ensure_ascii=False, indent=4))
        print(self.post(tmp, api=self.apis['music']))



if __name__ == '__main__':
    # hp = Hp_post()
    # nf = Net_info()
    # s = {"deviceGuid":"00:00:6C:06:A6:29","deviceSN":"70368170428025"}
    # s['deviceGuid'] = nf.mac
    # print(json.dumps(s, indent=4))
    # print(hp.post(s))

    reg = Regist()
    reg.regist_mac()
    reg.regist_info()
    reg.regist_attr()
    mus = Music(sys.argv[1])
    reg.regist_music(mus.playlist)
    
    # mus = Music(sys.argv[1])