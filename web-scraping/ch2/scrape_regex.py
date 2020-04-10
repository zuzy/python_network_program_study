#!/usr/bin/python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
import re

import sys
sys.path.append('../../')
from zdump import dump

url = 'http://www.pythonscraping.com/pages/page3.html'

def test_re():
    html = urlopen(url)
    bsObj = BeautifulSoup(html, 'html.parser')
    # images = bsObj.findAll('img', {'src': re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
    images = bsObj.findAll('img', {'src': re.compile(".*\/gifts\/img.*\.jpg")})
    for image in images:
        # 获取标签属性
        # myTag.attrs 获取全部属性
        # attrs['src]  获取某一个属性
        print(image['src'])
    

def test_lambda():
    html = urlopen(url)
    bsObj = BeautifulSoup(html, 'html.parser')
    tags = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
    for tag in tags:
        print(tag.attrs)

if __name__ == '__main__':
    # test_re()
    test_lambda()