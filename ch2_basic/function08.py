#!/usr/bin/python3
# coding: utf-8
def myfun(x, y) :
    print(x, id(x))
    print(y, id(y))
    return
a = 10
b = [1,2]
print(a, id(a))
print(b, id(b))
print('---------------')
myfun(a,b)
'''
the demo ahead
share the memory
'''

def myfun2(x, y, z):
    x = x + 1
    y.append(3)
    z = [3, 4]
    print(x, id(x))
    print(y, id(y))
    print(z, id(z))
    return

aa = 10,
b = [1,2]
c = [1,2]
print('before')
print('\t', a, id(aa))
print('\t', b, id(b))
print('\t', c, id(c))

myfun2(10, b, c)

print('after')
print('\t', a, id(aa))
print('\t', b, id(b))
print('\t', c, id(c))
