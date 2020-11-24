#!/usr/bin/python3

import json
from dict import *

def test():
    print(d)
    d['hello'] = 'hello'
    s = 'd = ' + json.dumps(d)
    print(s)
    with open('dict.py', 'w') as f:
        f.write(s)

if __name__ == '__main__':
    test()
