#!/usr/bin/python3
# coding: utf-8
class Persion:
    name = None
    age = None
    def __init__(self, name = 'Noname', age = 0, color = 'No color'):
        self.name = name
        self.age = age
        self.color = color
    def print_me(self):
        print('My name is %s, age is %d' % (self.name, self.age))
    def print_color(self):
        print('My name is %s, my color is %s' % (self.name, self.color))

zhao = Persion('zhao', 20, 'red')
zhao.print_me()
zhao.print_color()

qian = Persion('qian', 30)
qian.print_me()
qian.color = 'green'
qian.print_color()
del qian.color

