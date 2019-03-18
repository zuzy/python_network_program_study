#!/usr/bin/python3
# coding: utf-8

def fab(num):
    a, b, counter = 0, 1, 0
    while True:
        if counter <= num:
            b, a = a+b, b
            counter += 1
            yield a
        else:
            return

f = fab(10)
while True:
    try:
        print(next(f))
    except StopIteration:
        break
