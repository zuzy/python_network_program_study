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

