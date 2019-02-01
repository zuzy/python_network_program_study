#!/usr/bin/python3
# coding: utf-8
def myfun(x):
    if x > 1:
        return x * myfun(x - 1)
    else:
        return 1
print(myfun(4))
