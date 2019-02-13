#!/usr/bin/python3
#coding: utf-8
from urllib import request
req = request.Request('http://www.baidu.com')
resp = request.urlopen(req)
print(resp.geturl())
print(resp.getcode())
print(resp.info())