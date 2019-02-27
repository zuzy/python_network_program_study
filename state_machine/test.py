#!/usr/bin/python3
# coding:utf-8
import socket, time, uuid, asyncio, select, sys, json, threading, struct, os
from build import Rule

# r = Rule()
# print(r.state_range())
# print(r.act_range())
# print(r.trager())
# print(r.exclusive())
# print(r.relation())

# state_bit_str = r.state_range().strip()
# print(state_bit_str)
# tmp = state_bit_str.encode()
# print(tmp)
# state_bit_num = tmp[-1] - tmp[0]
# print(state_bit_num)

class Build:
    def __init__(self, path = 'rule'):
        try:
            self.rul = Rule(path)
            self.act_range = self.get_range(self.rul.act_range()) + 1
            print(self.act_range)
            self.state_range = self.get_range(self.rul.state_range()) + 1
            
            # self.trager = self.rul.trager()
            self.trager = self._trans_alpa_to_num(self.rul.trager())
            
            print(self.trager)

            self.exclusive = []
            for x in self.rul.exclusive():
                self.exclusive.append(self._trans_alpa_to_num(x))
            print(self.exclusive)

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
    
    def _state_trager(self, state):
        return 1

    def build(self, path = 'target'):
        max_state = 1 << self.state_range
        print(max_state)
        final_list = []
        for state in range(max_state):
            if self._check_if_exclusive(state):
                s_list = []
                s_list.append(state)
                for j in range(self.act_range):
                    if j in self.trager:
                        act = 1 << j
                        tmp = (state & act) ^ act
                        # print(tmp)
                        s_list.append(tmp)
                    else:
                        s_list.append(state)
                final_list.append(s_list)
        return final_list


b = Build().build()
print(b)
