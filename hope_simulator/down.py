#!/usr/bin/python3
#coding: utf-8

# from requests import *
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



def run():
    print("hello")
    url = 'http://192.168.2.9:8080/hopeApi/upgrade/mac'
    dat = {"deviceGuid":"00:00:6C:06:A6:29","deviceSN":"72123123325"}
    s = json.dumps(dat, separators=(',',':'))
    print(s)
    data = {
        'ver':'1.0',
        'cid':'881256532942016512',
        'sid':'750837261197414400',
        'key':'0CF9DE03AF1C46F9A970AB27120A91D2',
        'len':len(s),
        'dat':s
    }
    data['des'] = get_des(s)
    print(json.dumps(data))
    print(data['des'])
    resp = requests.post(url, data=data)
    print(resp.text)

def get_des(dat):
    data = {
        'ver':'1.0',
        # 'des':79,
        'cid':'881256532942016512',
        'sid':'750837261197414400',
        'key':'0CF9DE03AF1C46F9A970AB27120A91D2',
        'len':len(dat),
        'dat':dat,
    }

    print(dat, len(dat))
    password = "%d%s%s%s%s" % (data['len'], data['key'], data['cid'], data['sid'], data['ver'])
    m = hashlib.md5()
    m.update(password.encode())
    print(password)
    md = m.hexdigest().upper()
    print(md)
    ret = 0

    for c in md.encode():
        ret = ret ^ c
        # print(c , ret)

    print(ret)
    print('%x' % ret)
    return '%02x' % ret

if __name__ == "__main__":
    run()

    s = '{"deviceGuid":"00:00:6C:06:A6:29","deviceSN":"70368170428025"}'
    print(s, len(s))

    get_des(s)





