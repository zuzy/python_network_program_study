#!/usr/bin/python3
# -*- coding: utf-8 -*-

a = 0x8035

class Itochr():
    def __init__(self, tar, len=4):
        format = '%%0%dx' % len
        self.tar = format % tar
        print(self.tar)
    def __iter__(self):
        self.list = bytes([int(self.tar[i]+self.tar[i+1]) for i in range(len(self.tar)) if i % 2 == 0])
        print(self.list, type(self.list))
        self.index = 0
        return self
    def __next__(self):
        if self.index >= len(self.list):
            raise StopIteration
        else:
            x = chr(self.list[self.index])
            self.index += 1
            return x

m = Itochr(a)
m = iter(m)
b = ''
while True:
    try:
        b += next(m)
        print(type(b), b)
    except StopIteration:
        break
m = iter(m)
for i in m:
    print('1111',i)
c = b.encode(encoding='ascii')
print(c, type(c))
print('exit')

