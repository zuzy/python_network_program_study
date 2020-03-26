#!/usr/bin/python3

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import sys
sys.path.append('../../')
from zdump import dump

url = 'http://www.pythonscraping.com/pages/page3.html'

def get_bsObj(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    try:
        # bsObj = BeautifulSoup(html.read(), 'html.parser')
        bsObj = BeautifulSoup(html, 'html.parser')
    except Exception as e:
        return None
    else:
        return bsObj

# @dump
def dump_children(bsObj):
    for child in bsObj.find('table', {'id':'giftList'}).children:
        print(child)

# 打印所有 tr 标签的兄弟标签（除了第一个）。next_siblings 返回一个标签的所有兄弟标签，一个标签不可能是它本身的兄弟标签。
# next_siblings 可以选择除了标题行以外的所有行
# sibling 兄弟、同胞
# @dump
def dump_brothers(bsObj):
    for sibling in bsObj.find('table', {'id': 'giftList'}).tr.next_siblings:
        print(sibling)

# @dump
def dump_parents(bsObj):
    price = bsObj.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()
    print(price)
    return price


if __name__ == '__main__':
    bsObj = get_bsObj(url)
    # dump_children(bsObj)
    # dump_brothers(bsObj)
    dump_parents(bsObj)
    