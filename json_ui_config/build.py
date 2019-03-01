#!/usr/bin/python3
# coding: utf-8

import json,os
from excel_module import Relation

class Build(Relation):
    STATE = {
        "互斥": "off",
        "共存":"stay",
        "开":"on",
        "不可用":"ban"
    }
    menu = 'config/'

    def __init__(self, path = 'relation.xlsx'):
        os.system("mkdir " + self.menu)
        super().__init__(path)
        # print(self.acts)
        # print(self.states)
        # print(self.relation)
        for nact, act in enumerate(self.acts):
            f = open(self.menu + act + '.json', 'w')
            states = self.relation[nact]
            # print(states)
            d = {}
            for nstate, state in enumerate(states):
                # print(self.states[nstate])
                # print(state)
                # print(self.STATE[state])
                d[self.states[nstate]] = self.STATE[state]
            print(d)
            f.write(json.dumps(d,ensure_ascii=False, indent=4))
            f.close()
            # break
            



b = Build()