#!/usr/bin/python3
#coding: utf-8
def myfun(a, b = 0, *c, d, **e) :
    print('a ', a)
    print('b ', b)
    print('c ', c)
    print('d ', d)
    print('e', e)
    return
kv = {'e1': 7, 'e2': 8}
myfun(1,2,3,4,d=10, **kv)
