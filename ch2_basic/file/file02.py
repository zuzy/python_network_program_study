#!/usr/bin/python3
# coding: utf-8
path = 'test1.dat'
xx = ['aa', 123, '文件', True, 'ddd']

# two different ways to make sure f can be closed.

f = open(path, 'w')
try:
    for x in xx:
        if type(x) == str:
            f.write(x)
except Exception as e:
    print('Exception: ', e)
finally:
    f.close()

# open a file with 'with', need not to close manually
with open(path, 'w') as f:
    for x in xx:
        if type(x) == str:
            f.write(x)
