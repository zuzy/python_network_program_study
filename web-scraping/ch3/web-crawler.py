#!/usr/bin/python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'http://en.wikipedia.org/wiki/Kevin_Bacon'

def test1():
    html = urlopen(url)
    bsObj = BeautifulSoup(html, 'html.parser')
    for link in bsObj.findAll('a'):
        if 'href' in link.attrs:
            print(link.attrs['href'])

def test2():
    html = urlopen(url)
    bsObj = BeautifulSoup(html, 'html.parser')
    for link in bsObj.find("div", {"id":"bodyContent"}).findAll('a', href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            print(link.attrs['href'])

import datetime
import random

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org' + articleUrl)
    bsObj = BeautifulSoup(html, 'html.parser')
    return bsObj.find('div', {'id': 'bodyContent'}).findAll('a', 
        href = re.compile("^(/wiki/)((?!:).)*$"))

def test3():
    links = getLinks('/wiki/Kevin_Bacon')
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)

if __name__ == '__main__':
    # test1()
    # test2()
    test3()