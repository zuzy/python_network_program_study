#!/usr/bin/python3
# -*- coding: utf-8 -*-
def sum_from_string(s):
    whole = 0
    for i in s.split(','):
        whole += float(i)
    return whole

print(sum_from_string(input("input a list of numbers \\")))