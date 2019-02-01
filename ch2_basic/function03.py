#!/usr/bin/python3
# coding: utf-8
def myfun(xx, a = 3, b = 4):
    s = a * 3 + b * 4 + xx
    return s
print(myfun(1,2,3))
print(myfun(1, b = 3, a = 2))