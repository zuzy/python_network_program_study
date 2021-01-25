#!/usr/bin/python3
from itertools import product

def combination(tar):
    alphaList = [ [c.upper(), c.lower()] for c in tar]
    return {''.join(a) for a in list(product(*alphaList))}
    
def _jpg():
    j = ['J', 'j']
    p = ['P', 'p']
    g = ['G', 'g']
    return  tuple(_j + _p + _g for _j in j for _p in p for _g in g)
ALLOWED_EXTENSIONS = _jpg()


if __name__ == '__main__':
    print(_jpg())
    print(combination('jpg'))
    print(combination('nbdla'))