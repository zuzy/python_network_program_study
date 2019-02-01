#!/usr/bin/python3
# coding: UTF-8

s1 = 'aaa'
s2 = s1
s = '123\n' + '456'
print(len(s))
s = '1234567890'
print(s[0], s[1])
print(s[2:4])
print(s[2:-4])

print(s[::2])
print(s[::4])
print(s[2:-4:2])
print(s[::-1])

print(int(s))
print(int(s, 16))

s = 'ab'
print(s.join('123'))
print(s.join(['1', '2']))

s = 'ab,cd,e'
print(s.split(','))
print(s.split(',', 1))

s = '1234567890'
print(s.find('34'))
print(s.find('346'))
print(s.find("34", 1, 4))
# print(s.index('34'))

s = '123123123'
print(s.rfind('12'))

print(s.count('2'))
print(s.replace('12', 'ab'))
print(s.replace('12', 'ab', 2))

s = '12\t12'
print(s)
print(s.expandtabs(4))
print(s.expandtabs())

s = 'aA12Bb'
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.capitalize())
print(s.islower())
print(s.isalpha())

print(s.istitle())
print('-------')
print(s.capitalize().istitle())


print(ord('a'))
print(ord('中'))

print(chr(20013))
print('中'.encode('utf-8'))
print(bytes('abc中',encoding='utf-8'))
print(str(b'abc\xe4\xb8\xad', encoding='utf-8'))

print('there is %d apples' % 10)