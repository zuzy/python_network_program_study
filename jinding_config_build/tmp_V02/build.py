#!/usr/bin/python3
# coding: utf-8

import json, os
from excel_module import Relation

class Build():
    STATE = {
        "互斥": "off",
        "关":"off",
        "共存":"stay",
        "-":"stay",
        "开":"on",
        "不可用":"ban",
        "":"stay"
    }
    menu = 'config/'

    def __init__(self, path = 'relation.xlsx'):
        
        rule = Relation()
        os.system('mkdir ' + self.menu)
        f = open("state.json", "w")

        for nact, act in enumerate(rule.acts):
            f = open(self.menu + act + '.json', 'w')
            d = {}
            states = rule.relation[nact]
            for nstate, state in enumerate(states):
                d[rule.states[nstate]] = self.STATE[state]

            f.write(json.dumps(d,ensure_ascii=False, indent=4))
            f.close()




b = Build()