#!/usr/bin/python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'https://movie.douban.com'

def test():
    html = urlopen(url)
    bsObj = BeautifulSoup(html, 'html.parser')
    links = bsObj.findAll('a', {'class': 'item'})
    for link in links:
        if 'alt' in link:
            print(link['alt'])
    
if __name__ == '__main__':
    test()