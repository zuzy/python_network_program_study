#!/usr/bin/python3
# coding:utf-8

import socket, time, uuid, asyncio, select, sys, json, threading, struct, os


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



class Build:
    def __init__(self, path = 'rule'):
        try:
            self.rul = Rule(path)
            self.act_range = self.get_range(self.rul.act_range()) + 1
            # print(self.act_range)
            self.state_range = self.get_range(self.rul.state_range()) + 1
            
            # self.trager = self.rul.trager()
            self.trager = self._trans_alpa_to_num(self.rul.trager())
            
            # print(self.trager)

            self.exclusive = []
            for x in self.rul.exclusive():
                self.exclusive.append(self._trans_alpa_to_num(x))
            # print(self.exclusive)

            if self.act_range > self.state_range:
                raise Exception('error! act is more than state')
        except Exception as e:
            print(e)
            return None

    def get_range(self, i):
        try:
            s = i.strip().encode()
            return s[-1] - s[0]
        except Exception as e:
            print(e)
            return -1
    
    def _trans_alpa_to_num(self, alpa):
        alpa_list = alpa.split(',')
        ret = []
        for x in alpa_list:
            ret.append(x.encode()[0] - 'A'.encode()[0])
        return(ret)

    def __exclusive(self, state, ex_list):
        num = 0;
        for x in ex_list:
            if (1 << x) & state:
                num += 1
        return num < 2
    def _check_if_exclusive(self, state):
        for x in self.exclusive:
            if self.__exclusive(state, x) == False:
                return False
        return True

    def _trager_self(self, state, act_loc):
        state ^= 1 << act_loc
        return state

    def _get_max_exclusive(self, act_loc):
        e_list = []
        for l in self.exclusive:
            if act_loc in l:
                for ll in l:
                    if ll in e_list:
                        continue
                    else:
                        e_list.append(ll)
        return e_list

    def _trager_exclusive(self, state, act_loc):
        e_list = self._get_max_exclusive(act_loc)
        if len(e_list) > 1:
            tmp = self._trager_self(state, act_loc) & (1 << act_loc)
            if tmp == 0:
                return self._trager_self(state, act_loc)
            else:
                nstate = ~state
                # print(nstate)
                for z in e_list:
                    nstate |= 1 << z
                state = ~nstate
                state |= tmp
                return state
        elif act_loc in self.trager:
            return self._trager_self(state, act_loc)
        else:
            return state

    def build(self, path = 'target'):
        max_state = 1 << self.state_range
        # print(max_state)
        final_list = []
        for state in range(max_state):
            if self._check_if_exclusive(state):
                s_list = []
                s_list.append(state)
                for j in range(self.act_range):
                    s_list.append(self._trager_exclusive(state, j))
                final_list.append(s_list)
        return final_list
