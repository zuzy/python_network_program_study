#!/usr/bin/python3
# coding:utf-8
import json

class Rule:
    def __init__(self, path = 'rule'):
        self.path = path
        self.__dump()
    def __dump(self):
        try:
            f = open(self.path)
            rule_str = f.read()
            # print(rule_str)
            self.rule_tab = json.loads(rule_str)
            return json.dumps(self.rule_tab)
        except Exception as e:
            print('database read error',e)
            return None
    def state_range(self):
        try:
            # print(self.__dump())
            return self.rule_tab['state_range']
        except Exception as e:
            print("dump state range error ", e);
            return None
    def act_range(self):
        try:
            return self.rule_tab['act_range']
        except Exception as e:
            print("act range error, ", e)
            return None
    def trager(self):
        return self.rule_tab['rules']['trager']
    def exclusive(self):
        return self.rule_tab['rules']['exclusive']
    def relation(self):
        return self.rule_tab['rules']['relation']
