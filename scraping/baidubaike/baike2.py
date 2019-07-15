#-*-coding:utf-8-*-
import re
import requests
import bs4
from bs4 import BeautifulSoup
import json
import codecs
import sys
import os

path = sys.path[0] + os.sep
headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,zh-HK;q=0.7,en-US;q=0.6",
    "Connection":"keep-alive",
    "Cookie":"BAIDUID=12D740BD92DEA90B607F5B827987F30E:FG=1; BIDUPSID=12D740BD92DEA90B607F5B827987F30E; PSTM=1534166632; BKWPF=3; BDUSS=lleW52cG9MalVYcUhKeWJSYllpMlgzQXpnN2lORml-UXh3b1BqRGpqSnBtcVJiQVFBQUFBJCQAAAAAAAAAAAEAAAARJts6wu3D98flt-cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGkNfVtpDX1bT1; PSINO=1; H_PS_PSSID=1447_21105_20882_26350_26924_20927; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; pgv_pvi=419963904; pgv_si=s2644193280; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1534920932,1535362634,1535362645,1535362662; Hm_lpvt_55b574651fcae74b0a9f1cf9c8d7c93a=1535362662",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36", 
    "Host": 'baike.baidu.com',
    "Upgrade-Insecure-Requests":"1"
}

def craw(url, item):
    html = requests.get(url, headers=headers).content
    data = dict()
    data['url'] = url
    data['name'] = item
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find('h2').get_text()
    data['abstract'] = soup.find('div', class_='lemma-summary').get_text().strip().replace('\n', '').replace('\t', '')
    basic_info = soup.find('div', class_='basic-info')
    dts = basic_info.find_all('dt', class_='name')
    dds = basic_info.find_all('dd', class_='value')
    data['basic_info'] = dict()
    for i in range(len(dts)):
        name = dts[i].get_text().strip().replace('\n', '').replace('\t', '')
        value = dds[i].get_text().strip().replace('\n', '').replace('\t', '')
        data['basic_info'][name] = value
    paras = soup.find_all('div', class_=['para-title', 'para'])
    content = dict()
    # move cursor to div: para-title level-2
    for i in range(len(paras)):
        if 'level-2' in paras[i]['class']:
            paras = paras[i:]
            break
    level3_flag = False
    # traversal content, caution: there is level-3 para, so the code will be more complicate 
    for para in paras:
        if 'level-2' in para['class']:
            prefix = para.span.get_text().strip().replace('\n', '')
            name = para.h2.get_text().strip().replace('\n', '').replace(prefix, '')
            print 'name', name
            content[name] = ''
            level3_flag = False
        elif 'level-3' in para['class']:
            if not level3_flag:
                content[name] = dict()
            prefix = para.span.get_text().strip().replace('\n', '')
            children = para.h3.get_text().strip().replace('\n', '').replace(prefix, '')
            print 'children', children
            content[name][children] = ''
            level3_flag = True
        else:
            text = para.get_text().strip().replace('\n', '').replace('\t', '')
            if level3_flag:
                content[name][children] += text
            else:
                content[name] += text
    data['content'] = content
    f = codecs.open(path + 'baike.json', 'w', 'utf-8')
    json.dump(data, f, ensure_ascii=False)
    f.write('\n')
    f.close()

if __name__ == '__main__':
    baseurl = 'http://baike.baidu.com/item/'
    # items = ['Python', u'北京市', u'朝阳区']
    items = [u'北京市']
    for item in items:
        url = baseurl + item
        print url
        craw(url, item)
