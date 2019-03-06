#!/usr/bin/python3
# coding: utf-8

import json, os
from excel_module import Relation, Depends

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

        for nact, act in enumerate(rule.acts):
            f = open(self.menu + act + '.json', 'w')
            d = {}
            states = rule.relation[nact]
            for nstate, state in enumerate(states):
                d[rule.states[nstate]] = self.STATE[state]

            f.write(json.dumps(d,ensure_ascii=False, indent=4))
            f.close()
        f = open("depend.json", "w")
        self._depend_init_()
        json.dump(self.depends, f, ensure_ascii=False, indent=4)
        f.close()
        self.init_state()

    
    def _depend_init_(self):
        dep = Depends()
        self.depends = dep.depends
        print(dep.depends)
    def init_state(self):
        d = {
            "离开": "off",
            "凉风扇外": "off",
            "照明": "off",
            "风速": "ban",
            "凉风内": "off",
            "洗浴场景": "off",
            "负离子": "off",
            "热干": "off",
            "音乐": "off",
            "换气扇内": "off",
            "电源": "off",
            "取暖": "off",
            "摆风": "ban",
            "洗漱场景": "off",
            "换气扇外": "off",
            "取暖模式": "off",
            "凉干": "off",
            "如厕场景": "off",
            "空气检测": "off"
        }
        f = open('state.json', 'w')
        json.dump(d, f, ensure_ascii=False, indent=4)
        f.close()




b = Build()