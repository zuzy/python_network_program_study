#!/usr/bin/python3
# coding: utf-8
'''
StringIO 提供了一种像操作文本磁盘文件一样对内存缓存区数据操作的方法
'''
arr = ['aa', 123, '文件', True, 'ddd']
from io import StringIO
f = StringIO()
for x in arr:
    if type(x) == str:
        f.write(x)
f.seek(0)
xx = f.read()
print('xx = ', xx)
yy = f.getvalue()
print('yy = ', yy)

'''
BytesIO 提供了一种像操作二进制文本磁盘文件一样对内存缓存区数据操作的方法
'''
import pickle
from io import BytesIO
f = BytesIO()
for x in arr:
    pickle.dump(x, f)
f.seek(0)
while True:
    try:
        xx = pickle.load(f)
        print('xx = ', xx)
    except EOFError:
        break