#!/usr/bin/python3
# -*- coding: utf-8 -*-

def check_num(tar_num, order):
    for i in range(tar_num):
        # print(i)
        if i**order >= tar_num:
            return (i, i**order == tar_num)

def check_input(num):
    num = abs(num)
    for i in range(2, 6):
        ret, status = check_num(num, i)
        if status:
            print("check ok", ret, "**", i)
            return ret, i
    else:
        print("check false")
        return False

check_input(int(input('input a num')))