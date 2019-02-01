#!/usr/bin/python3
# coding: utf-8
score = int(input("enter your score:"))
if score >= 90:
    print("grade is A")
    print('Excellent')
elif score >= 80:
    print('grade is B')
    print('Good')
elif score >= 70:
    print('grade is C')
elif score >= 60:
    print('grade is D')
else:
    print('not passed')