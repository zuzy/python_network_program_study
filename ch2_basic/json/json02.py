#!/usr/bin/python3
# coding: utf-8
import json
class Person: 
    def __init__(self, name = 'Noname', age = 0):
        self.name = name
        self.age = age

def person2dict(p):
    return {'name':p.name, 'age':p.age}
def dict2person(d):
    return Person(d['name'], d['age'])

xx = Person('zhao', 20)

with open('test6.dat', 'w') as f:
    json.dump(xx, f, default=person2dict)
with open('test6.dat', 'r') as f:
    yy = json.load(f, object_hook=dict2person)
print(yy.name, yy.age)
print(yy, type(yy))

aa = {'age':23, 'name':'zhu'}
d = json.dumps(aa)
print(type(d), d)
l = json.loads(d)
print(type(l), l)