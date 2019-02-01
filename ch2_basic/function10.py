#!/usr/bin/python3
# coding: utf-8
def myfun(n, x, y, z):
    if n <= 1:
        print(x, '---->', z)
        return
    else:
        myfun(n - 1, x, z, y)
        print(x, '---->', z)
        myfun(n - 1, y, x, z)
    return
myfun(3, 'A', 'B', 'C')
