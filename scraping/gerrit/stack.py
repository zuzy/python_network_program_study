#!/usr/bin/env python3
import json
import requests
from urllib.request import urlopen
# import request

# url = 'https://www.pse.com/api/sitecore/OutageMap/AnonymoussMapListView'

url = 'http://gerrit.enflame.cn/q/111547e125ceddb42b1ba86545f240f2a7bf1e98'
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(page)
print(html)

d = requests.get(url)
print(d)
# data = requests.get(url).json()
# start_index = html.find("<title>") + len("<title>")
# end_index = html.find("</title>")
# title = html[start_index:end_index]
# print(title)


# url = 'https://www.google.co.il/search?q=eminem+twitter'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'

# header variable
headers = { 'User-Agent' : user_agent }

# creating request
req = requests.get(url, headers)
print(req)
# getting html


# uncomment this to print all data:
#print(json.dumps(data, indent=4))

for d in data['PseMap']:
    print(d)
    # print('{} - {}'.format(d['DataProvider']['PointOfInterest']['Title'], d['DataProvider']['PointOfInterest']['MapType']))
    # for info in d['DataProvider']['Attributes']:
    #     print(info['Name'], info['Value'])
    print('-' * 80)