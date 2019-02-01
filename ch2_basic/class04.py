#!/usr/bin/python3
# coding: utf-8
class Person:
    __name = None
    __age = None
    def __init__(self, name = 'Noname', age = 0):
        self.__name = name
        self.__age = age
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age

zhao = Person('zhao', 20)
print(zhao.get_name(), zhao.get_age())
zhao.set_age(30)
print(zhao.get_name(), zhao.get_age())


class Person2:
    def __init__(self, name = 'noname', age = 0):
        self._name = name
        self._age = age
    @property #return the attr
    def name(self):
        return self._name
    @name.setter #set the attr
    def name(self, name):
        self._name = name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age
qian = Person2()
qian.name = 'qian'
qian.age = 28
print(qian.name, qian.age)
        