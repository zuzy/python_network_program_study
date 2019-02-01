#!/usr/bin/python3
# coding: utf-8
class Person(object):
    __name = None
    def __init__(self, name = 'noname'):
        self.__name = name
    def get_name(self):
        return self.__name
    def whoami(self):
        print("i'm a person, my name is ", self.get_name())

class Student(Person):
    __score = 0
    # def __init__(self, name = 'noname', score = 0):
    def __init__(self, name, score = 0):
        super().__init__(name)
        __score = score
    def whoami(self):
        print("i'm a student, my name's %s, score %d" % (super().get_name(), self.__score))
class Teacher(Person):
    __title = None
    def __init__(self, name='noname', title = 'none'):
        super().__init__(name=name)
        self.__title = title
    def whoami(self):
        print("i'm a theacher, my name's %s, title %s" % (super().get_name(), self.__title))

def whoareyou(x):
    x.whoami()
p1 = Person('zhao')
p2 = Student('qian', 90)
p3 = Teacher('sun', 'professor')
whoareyou(p1)
whoareyou(p2)
whoareyou(p3)
        