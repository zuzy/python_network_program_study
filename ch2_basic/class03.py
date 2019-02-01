#!/usr/bin/python3
# coding: utf-8
class Person:
    __slots__ = ('name', 'age', 'myprint')
def my_print(self):
    print('my name is %s, age is %d' % (self.name, self.age))
    
zhao = Person()
zhao.name = 'zhao'
zhao.age = 20
Person.myprint = my_print
zhao.myprint()