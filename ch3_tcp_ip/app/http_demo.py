#!/usr/bin/python3
#coding: utf-8
from urllib import request
# req = request.Request('http://www.baidu.com/item/马云')
# req = request.Request('https://baike.baidu.com/item/马云')
req = request.Request('https://www.baidu.com')
resp = request.urlopen(req)
print(resp.geturl())
print(resp.getcode())
print(resp.info())


import requests
headers = {
    "Host":"baike.baidu.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5383.400 QQBrowser/10.0.1313.400"
}
response = requests.get("https://baike.baidu.com/item/马云", headers=headers)
print(response.content)