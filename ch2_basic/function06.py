#!/usr/bin/python3
# coding: utf-8
def myfun(name, *, age, city):
    print('name: ', name)
    print('age: ', age)
    print('city: ', city)
    return
    
myfun('zizy', age = 29, city = 'ninbo')

