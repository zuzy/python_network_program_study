#!/usr/bin/python3

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/warandpeace.html'
def test_simple():
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print(e)
    else:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        nameList = bsObj.findAll('span', {'class':'green'})
        for name in nameList:
            print(name.get_text(), end=',\t')
        
        princes = bsObj.findAll(text='The prince')
        print("\n'The prince' Num: ", len(princes))

if __name__ == '__main__':
    test_simple()
