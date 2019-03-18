#!/usr/bin/python3
#coding: utf-8

import requests, json, hashlib, sys, re

'''
ver	1.0
des	79
cid	750064224428658688
sid	750837261197414400
key	A716A953593940D2BD78E1A02CD3C070
len	62
dat	{"deviceGuid":"00:00:6C:06:A6:29","deviceSN":"70368170428025"}
'''

class hp_post():
    def __init__(self, cid='881256532942016512', sid='750837261197414400', key='0CF9DE03AF1C46F9A970AB27120A91D2', ver='1.0'):
        self.data = {}
        self.data['cid'] = cid
        self.data['sid'] = sid
        self.data['key'] = key
        self.data['ver'] = ver

    def dump(self, dat_tab):
        return json.dumps(dat_tab, separators=(',',':'))

    def get_des(self, dat_str):
        l = len(dat_str)
        passwd = '%d%s%s%s%s' % (l, self.data['key'], self.data['cid'], self.data['sid'], self.data['ver'])
        m = hashlib.md5()
        m.update(passwd.encode())
        md = m.hexdigest().upper()
        ret = 0
        for c in md.encode():
            ret ^= c
        return l, '%02x' % ret
    
    def post(self, target, api='/hopeApi/upgrade/mac', uri='http://192.168.2.9:8080'):
        data = self.data.copy()
        if type(target) != str:
            target = self.dump(target)
        data['len'], data['des'] = self.get_des(target)
        data['dat'] = target
        resp = requests.post(uri+api, data=data)
        return resp.text

if __name__ == "__main__":
    s = '{"deviceGuid":"00:00:6C:06:A6:29","deviceSN":"70368170428025"}'
    print(s, len(s))
    hp = hp_post()
    print(hp.post(s))





