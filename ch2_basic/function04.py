#!/usr/bin/python3
# coding: utf-8
def myfun(*args) :
    print(args)
    s = 0
    for x in args:
        s += int(x)
    return s
print(myfun(1,2,3,'23'))