#!/usr/bin/python3
# coding: utf-8

import json, os
from excel_module import Relation

class Build():
    STATE = {
        "互斥": "off",
        "关":"off",
        "共存":"stay",
        "开":"on",
        "不可用":"ban",
        "":"stay"
    }
    menu = 'config/'

    def __init__(self, path = 'relation.xlsx'):
        # super().__init__(path)
        # print(self.acts)
        # print(self.states)
        # print(self.relation)
        r_on = Relation()
        r_off = Relation(sheet='rule_off')
        os.system('mkdir ' + self.menu)
        f = open("state.json", "w")
        tmp = {}

        self.states = r_on.states
        self.act = r_on.acts

        for state in r_on.states:
            tmp[state] = 'off'
        f.write(json.dumps(tmp, ensure_ascii=False,indent=4))
        f.close()
        for nact, act in enumerate(r_on.acts):
            f = open(self.menu + act + '.json', 'w')
            d = {}
            d_off = d['state_off_to_on'] = {}
            d_on = d['state_on_to_off'] = {}

            states = r_on.relation[nact]
            # print(r_on.relation)
            # print(r_on.states)
            for nstate, state in enumerate(states):
                # print(nstate, state)
                # print(self.STATE[state])
                # print(r_on.states[nstate])
                d_off[r_on.states[nstate]] = self.STATE[state]

            states = r_off.relation[nact]
            for nstate, state in enumerate(states):
                d_on[r_off.states[nstate]] = self.STATE[state]

            f.write(json.dumps(d,ensure_ascii=False, indent=4))
            f.close()
            # break
            
    def index(self):
        f.open("index.json", 'w')




b = Build()