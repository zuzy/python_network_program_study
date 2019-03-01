#!/usr/bin/python3
# coding:utf-8
import xlrd

class Relation(object):
    def __init__(self, path='relation.xlsx'):
        try:
            # self.path = path
            workbook = xlrd.open_workbook(path)
            self.sheet = workbook.sheet_by_name(u'rule')
            self.nrows = self.sheet.nrows
            self.relation = []
            for i in range(0, self.nrows):
                tmp = self.sheet.row_values(i)
                del(tmp[0])
                self.relation.append(tmp)
            del(self.relation[0])
            self.states = self.sheet.row_values(0)
            del(self.states[0])
            # print(self.states)
            self.acts = self.sheet.col_values(0)
            del(self.acts[0])
            # print(self.acts)
        except Exception as e:
            print("inition error, ", e)
            return None

# r = Relation()
# print(r.relation)