#!/usr/bin/python3
# coding: utf-8
class Persion:
    name = None
    age = None
    def __init__(self, name = 'Noname', age = 0):
        self.name = name
        self.age = age
    def print_me(self):
        print('My name is %s age is %d' % (self.name, self.age))
zhao = Persion('zhao', 20)
zhao.print_me()

qiao = Persion('Qiao', 30)
qiao.print_me()