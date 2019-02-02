#!/usr/bin/python3
# coding: utf-8
# read line
path = 'test1.dat'
xx = ['aa', 123, '文件', True, 'ddd']

f = open(path, 'w')
for x in xx:
    if type(x) == str:
        f.write(x + '\n')
f.close()

f = open(path, 'r')
x = f.readline()
x = x[0:-1]
my_list = []
while x != '':
    print('x = ', x)
    my_list.append(x)
    x = f.readline()
    x = x[0: -1]
f.close()
print('mylist ', my_list)