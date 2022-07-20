#!/usr/bin/env python3
import requests

# 111547e125ceddb42b1ba86545f240f2a7bf1e98
url = 'http://gerrit.enflame.cn/q/111547e125ceddb42b1ba86545f240f2a7bf1e98'

url = 'http://gerrit.enflame.cn/changes/7054d6dc6440453039848b1303b78c3c29962bb0'

# url = 'http://www.ichangtou.com/#company:data_000008.html'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'}

for i in range(4):
    response = requests.get(url, headers=headers)
    print(response.content)
    print(response.url)
    url = response.url