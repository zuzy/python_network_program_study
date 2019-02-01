#!/usr/bin/python3
# coding: utf-8
def myfun(name, **kwargs) :
    print(kwargs)
    print('name ', name)
    for key in kwargs:
        print(key, ':', kwargs[key])
    return
myfun('zizy', age = 28, height = 1.88, city = 'ningbo')