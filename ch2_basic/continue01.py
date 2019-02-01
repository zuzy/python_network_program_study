#!/usr/bin/python3
# coding: utf-8
sum = 0
x = 49
while x < 101:
    x += 1
    if x % 2 == 1:
        continue
    sum += x
print('sum is', sum)