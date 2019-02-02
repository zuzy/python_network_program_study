#!/usr/bin/python3
# coding: utf-8
path = 'test1.dat'
f = open(path, 'w')
for x in ['aa', 123, '文件', True, 'ddd']:
    if(type(x)) == str:
        f.write(x)
    # error when x is not a string
    # f.write(x)
# will not call close if error occurs
f.close()

f = open(path, 'r')
xx = f.read()
print('xx = ', xx)
f.close()