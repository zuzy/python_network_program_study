#!/usr/bin/python3
# coding: utf-8
import json
zhao = {'name':     'zhao', 'age' : 20}
with open('test5.dat', 'w') as f:
    json.dump(zhao, f)
with open('test5.dat', 'r') as f:
    zhao1 = json.load(f)
print('zhao1 = ', zhao1)
print('type(zhao1) = ', type(zhao1))