#!/usr/bin/python3
# coding: utf-8
sum = 0
for x in range(50, 101):
    sum += x
    if sum > 1000:
        break
print('sum is %d x is %d' % (sum, x))