#!/usr/bin/python3
# coding: utf-8
def myfun(x):
    try:
        h = 1 / x
    except Exception as e1:
        print('Exception: ', e1)
        print(x, 'is wrong')
        return 0
    # bad except order!
    except TypeError as e2:
        print('exception: ', e2)
        print(x, 'is not a number')
        return 0
    return h

xx = [1, 'a', 3, 0, 5, 4]
s = 0
for x in xx:
    s += myfun(x)
print("s is %6.2f" % s)