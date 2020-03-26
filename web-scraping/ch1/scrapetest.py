#!/usr/bin/python3
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import sys

sys.path.append('../../')

from bs4 import BeautifulSoup
from zdump import dump

url = 'http://www.pythonscraping.com/pages/page1.html'
html = urlopen(url)
def test():
    # html = urlopen('http://www.baidu.com')
    print(html.read().decode('utf-8'))

@dump
def test_bs():
    # html = urlopen('http://www.baidu.com')
    bsObj = BeautifulSoup(html.read(), 'html.parser')
    print(bsObj.h1)


def test_reliability():
    title = getTitle(url)
    if title == None:
        print("Titel could not be found")
    else:
        print(title)
    
@dump
def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print('Tag was not found', e)
        return None

    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

if __name__ == '__main__':
    test()
    # test_bs()
    # test_reliability()
    
'''
<html>
<head>
<title>A Useful Page</title>
</head>
<body>
<h1>An Interesting Title</h1>
<div>
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
</div>
</body>
</html>
'''