#!/usr/bin/python3
# encoding:utf-8
import json, os

# os.system("kill -9 " + str(os.getpid())) #杀掉进程

state_on = {
    "switch":[],
    "ban":[],
    "turn_on":[],
    "turn_off":["self"],
}

state_off = {
    "switch":[],
    "ban":[],
    "turn_on":["self"],
    "turn_off":[],
}

menu = 'config/'
f = open("index.json", 'r')
s = f.read()
f.close()
index_list = json.loads(s)
os.system("mkdir " + menu)
state_dict = {}
state_dict['ban'] = []
state_dict['state'] = {}
for name in index_list:
    f = open(menu + name + '.json', 'w')
    d = {}
    d['name'] = name
    d['state_on'] = state_on
    d['state_off'] = state_off
    # print(json.dumps(d, indent=4, ensure_ascii=False))
    f.write(json.dumps(d, indent=4, ensure_ascii=False))
    f.close()
    state_dict['state'][name] = 'off'
f = open("state.json", 'w')
f.write(json.dumps(state_dict, indent=4, ensure_ascii=False))


