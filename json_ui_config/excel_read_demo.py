#!/usr/bin/python3
#-*- coding: utf8 -*-
import xlrd

# 读取文件
data = xlrd.open_workbook('relation.xlsx')
# 通过索引顺序获取
table = data.sheets()[0]
# 通过索引顺序获取
table = data.sheet_by_index(0)
# 通过名称获取
table = data.sheet_by_name(u'Sheet1')
# 获取整行的值（数组）
# table.row_values(行号)
# # 获取整列的值（数组）
# table.col_values(列号)
# 获取行数　　
nrows = table.nrows
# 获取列数
ncols = table.ncols

# 循环行列表数据
for i in range(0,nrows): #从第一行开始至结尾，修改数字可以改变起始行
    print(i, ",", table.row_values(i))

# 根据指定的行与列获取单元格的值
cell_A1 = table.cell(0, 0).value
cell_C4 = table.cell(2, 3).value 
# 左为行号，右为列号，从0开始计算，即0为第一行（列）

# 根据行列索引获取单元格的值
cell_A1 = table.row(0)[0].value
cell_A2 = table.col(1)[0].value
