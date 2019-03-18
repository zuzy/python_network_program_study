#!/usr/bin/python3
# coding: utf-8

l = ['abc','der', 'sdfsdf']
del l[0]
for i in l:
    print(i)

it = iter(l)
for i in it:
    print(i)

it = iter(l)
while True:
    try:
        print(next(it))
    except StopIteration:
        break
    except Exception as e:
        print('error', e)
        break
'''
it = iter(l)
while True:
    print(next(it))
'''

class Mynum():
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

m = Mynum()
it = iter(m)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
while True:
    try:
        print(next(it))
    except StopIteration:
        break