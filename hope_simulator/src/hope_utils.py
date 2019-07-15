#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json, re, os

class R():
    def __init__(self):
        pass
    @staticmethod
    def exit():
        os.system("kill -9 " + str(os.getpid())) #杀掉进程

class Hp_info():
    def __init__(self):
        pass
    def get_sn(self):
        return '73001804123020'
        

class divide():
    tab = {
        'b':1,
        'w':2,
        'dw':4,
        dict:False,
    }
    def __init__(self, payload, step=['b','w','b','w', 10, b'\x7e']):
        self.payload = type(payload) == str and payload.encode() or payload
        self.step = step

    def __iter__(self):
        self.index = 0
        self.length = 0
        return self

    def __next__(self):
        if self.index > len(self.step):
            raise StopIteration
        if self.index == len(self.step):
            # print(self.payload)
            self.index += 1
            return self.payload
        t = self.step[self.index]
        ret = ''
        if t in self.tab:
            length = self.tab[t]
            try:
                for i in range(length):
                    ret += '%02x' % self.payload[i]
                self.payload = self.payload[length:]
                ret = int(ret, 16)
            except:
                raise StopIteration

        elif type(t) == int:
            try:
                for i in range(t):
                    ret += '%02x' % self.payload[i]
                self.payload = self.payload[t:]
            except:
                raise StopIteration
        elif type(t) == bytes:
            # print(t)
            try:
                s = self.payload.find(t)
                if s > 0:
                    ret = self.payload[:s]
                # print(s, ret)
                self.payload = self.payload[s+1:]
            except:
                StopIteration

        self.index += 1
        return ret


class hp_utils():
    def __init__(self):
        pass
    def itob(self, i, length=None):
        '''
        ####
        the old & stupid way to convert
        ####
        si = '%X' % i
        if length == None:
            length = len(si)
            length += length % 2

        elif length % 2 == 1:
            length += 1
        fmt = '%%0%dx' % length
        shex = fmt % i
        lhex = len(shex) - length
        if lhex > 0:
            shex = shex[lhex:]
        return bytes([int(shex[i]+shex[i+1], 16) for i in range(length) if i %2 == 0])
        '''

        si = '%x' % i
        li = len(si)
        if length == None:
            if li % 2 == 1:
                si = '0' + si
        else:
            length += (length % 2 == 1) and 1 or 0
            if length > li:
                si = '0' * (length - li) + si
            else:
                si = si[-length:]
        print(si)
        return bytes.fromhex(si)

            
    
    def tobyte(self, tar):
        if tar > 0xff or tar < 0:
            raise Exception('byte %d out of range!' % tar)
        return self.itob(tar)
    
    def toword(self, tar):
        if tar > 0xffff or tar < 0:
            raise Exception('word %d out of range!' % tar)
        return self.itob(tar, 4)
    
    def todword(self, tar):
        return self.itob(tar, 8)

    def encode(self, tar, pattern={0x7d:0x7d01, 0x7e:0x7d02}):
        if type(tar) == str:
            tar = bytes(tar, 'ascii')
        ret = b''
        for c in tar:
            if c in pattern:
                ret +=self.itob(pattern[c])
            else:
                ret += self.tobyte(c)
        return ret
    
    def unescape(self, bts, pattern={0x7d:{0x01:0x7d, 0x02:0x7e}}):
        en = False
        ret = b''
        for b in bts:
            if en == False:
                if b in pattern:
                    en = b
                else:
                    ret += self.tobyte(b)

            else:
                if b in pattern[en]:
                    ret += self.tobyte(pattern[en][b])
                else: 
                    print('error! %x %x' % (en, b))
                    return None
                en = False
        return ret
        

if __name__ == '__main__':
    u = hp_utils()
    a = u.itob(0x80380, length=1)
    b = u.itob(0x80380)
    print(a+b)
    # c = b'\x7e'
    # c += u.encode('\x12\x23\x01\x01\x01\x7e\x7d123456')
    # c += b'\x7e123'
    # print(c)
    # print(u.unescape(c))

    # z = '{abd:sdlfjsdfk!~}'
    # print(z)
    # y = u.encode(z)
    # print(y)
    # print(u.unescape(y))

    z = u.tobyte(0x77)
    z += u.toword(0x77)
    z += u.todword(0x37)
    print(z)

    # d = divide(u.unescape(c))
    # m = iter(d)
    # print([i for i in m])
    # print(d.payload, len(d.payload))

    # c = c[1:].decode()
    # m = re.match('.*\~', c, re.M)
    # print(m.group())

    # ddddd = b'~\x80\x01\x02\x01\x1a\xaau\x087&\x11\x97AD\x00{"ansId":0,"desc":"\xe6\xb6\x88\xe6\x81\xaf\xe6\xa0\xbc\xe5\xbc\x8f\xe6\x9c\x89\xe8\xaf\xaf\xef\xbc\x8c\xe8\xa7\xa3\xe7\xa0\x81\xe5\xa4\xb1\xe8\xb4\xa5\xef\xbc\x81\xe6\xb6\x88\xe6\x81\xaf\xe6\xa0\xa1\xe9\xaa\x8c\xe5\xa4\xb1\xe8\xb4\xa5\xef\xbc\x8c\xe8\xaf\xb7\xe6\xa3\x80\xe6\x9f\xa5\xe6\xb6\x88\xe6\x81\xaf\xe6\x8c\x87\xe4\xbb\xa4\xe4\xb8\xad\xe6\xa0\xa1\xe9\xaa\x8c\xe7\xa0\x81\xe7\x9a\x84\xe6\xad\xa3\xe7\xa1\xae\xe6\x80\xa7\xef\xbc\x81","result":50037}\x01T~'

    # ddddd = b'~\x80\x01\x02\x01\x14\xaau\x087&\x11\x97AD\x00{"ansId":0,"desc":"\xe6\xb6\x88\xe6\x81\xaf\xe6\xa0\xbc\xe5\xbc\x8f\xe6\x9c\x89\xe8\xaf\xaf\xef\xbc\x8c\xe8\xa7\xa3\xe7\xa0\x81\xe5\xa4\xb1\xe8\xb4\xa5\xef\xbc\x81\xe6\xb6\x88\xe6\x81\xaf\xe9\x95\xbf\xe5\xba\xa6\xe6\x9c\x89\xe8\xaf\xaf\xef\xbc\x8c\xe6\xb6\x88\xe6\x81\xaf\xe5\xae\x9e\xe9\x99\x85\xe9\x95\xbf\xe5\xba\xa6\xe4\xb8\x8e\xe6\x8c\x87\xe4\xbb\xa4\xe9\x95\xbf\xe5\xba\xa6\xe4\xb8\x8d\xe4\xb8\x80\xe8\x87\xb4\xef\xbc\x81","result":50037}\x01\xb0~'

    # ddddd = b'~\x80}\x01T~'
    # ddddd += ddddd


    # d = ddddd + ddddd
    # d += b'12331231231231sldfkjsdlakfjsakldfj'

    # print(d)
    # d = divide(ddddd)
    # m = iter(d)
    # print([i for i in m])

    # print('\n\n----\n',u.unescape(d))

    # d = u.unescape(d)
    # index = 1
    # while len(d) > 0:
        
    #     dd = divide(d)
    #     m = iter(dd)
    #     x = [i for i in m]
    #     print('-----%d-----\n' % index,x,'\n')
    #     index += 1
    #     if len(x) >= 7:
    #         d = x[6]
    #         if len(d) <= 0:
    #             break
    #     else:
    #         break
    
    # print('end')