#!/usr/bin/python3
# coding:utf-8
import xlrd

class Excel:
    def __init__(self, path, sheet):
        try:
            workbook = xlrd.open_workbook(path)
            sheet = workbook.sheet_by_name(sheet)
            nrows = sheet.nrows
            self.rows = []
            self.cols = []
            for i in range(0, nrows):
                self.rows.append(sheet.row_values(i))
            ncols = sheet.ncols
            for i in range(0, ncols):
                self.cols.append(sheet.col_values(i))
        except Exception as e:
            print(e)

class Depends(Excel):
    def __init__(self, path='relation.xlsx', sheet = 'depend'):
        dep = super().__init__(path, sheet)
        nodes = self.rows[0].copy()
        del(nodes[0])
        limits = self.cols[0].copy()
        del(limits[0])
        self.depends = {}
        for nnode, node in enumerate(nodes):
            rels = []
            for nlimit, limit in enumerate(limits):
                rel = self.cols[nnode + 1][nlimit + 1]
                if rel == '共存':
                    rels.append(limit)
            self.depends[node] = rels
        # print(self.depends)

class Index(Excel):
    def __init__(self, path = 'relation.xlsx', sheet = 'index'):
        try:
            super().__init__(path, sheet)
            self.button_names = self.cols
            # self._init_depend()

        except Exception as e:
            print(e)
    # def _init_depend(self, path='relation.xlsx', sheet = 'depend'):
    #     dep = Excel(path, sheet)
    #     nodes = dep.rows[0].copy()
    #     del(nodes[0])
    #     limits = dep.cols[0].copy()
    #     del(limits[0])
    #     self.depends = {}
    #     for nnode, node in enumerate(nodes):
    #         rels = []
    #         for nlimit, limit in enumerate(limits):
    #             rel = dep.cols[nnode + 1][nlimit + 1]
    #             if rel == '共存':
    #                 rels.append(limit)
    #         self.depends[node] = rels
    #     print(self.depends)

class Relation(Excel):
    def __init__(self, path='relation.xlsx', sheet = 'rule'):
        try:
            super().__init__(path, sheet)
            self.acts = self.cols[0].copy()
            del(self.acts[0])
            self.states = self.rows[0].copy()
            del(self.states[0])
            self.relation = []
            for i in self.rows:
                tmp = i.copy()
                del(tmp[0])
                self.relation.append(tmp)
            del(self.relation[0])

        except Exception as e:
            print("inition error, ", e)
            return None

        # print(self.depends)

                
            


class _Relation():
    def __init__(self, path='relation.xlsx', sheet = 'rule'):
        try:
            # self.path = path
            workbook = xlrd.open_workbook(path)
            self.sheet = workbook.sheet_by_name(sheet)
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

r = Relation()
# print(r.relation)