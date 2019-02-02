#!/usr/bin/python3
# coding: utf-8
def print_score(score):
    try:
        if not type(score) in [int, float]:
            raise TypeError('score must be the int or float type!')
        elif not 100 >= score >= 0:
            raise ValueError('score must be between 0 to 100')
            # raise Exception('sldkfjk')
        print('score is %6.2f' % score)
    except Exception as e:
        print('exception: ', e)

print_score(88.123)
print_score(123)
print_score('a')