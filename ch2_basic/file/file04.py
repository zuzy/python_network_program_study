#!/usr/bin/python3
# coding: utf-8
# pickle 提供了将其他类型数据转成byte的手段。
# dump 负责将数据序列化之后写入二进制文件中
# load 负责将序列化的的数据从二进制文件读出后转化为原有的类型
import pickle
with open('test2.dat', 'wb') as f:
    for x in ['aa', 123, '文件', 'c', (3+4j)]:
        pickle.dump(x, f)
# f = open('test2.dat', 'wb')
# for x in ['aa', 12345]:
#     pickle.dump(x, f)

with open('test2.dat', 'rb') as f:
    '''
    seek(offset, 0/1/2) :   0-> start + offset
                            1-> present location + offset
                            2-> end + offset; if file, offset must be 0
    '''
    f.seek(0, 2)
    endp = f.tell()
    f.seek(0)
    xx = pickle.load(f)
    while xx is not None:
        print('xx = ', xx)
        if f.tell() >= endp:
            break
        xx = pickle.load(f)