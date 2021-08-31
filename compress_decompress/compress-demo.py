#!/usr/bin/env python3
import zlib

# a = "hello world"
a = "Hello, world!00000001111111111111100000"
b = zlib.compress(a.encode())
print(type(b), len(b))
for bt in b:
    print("{:02X}".format(bt), end=' ')
print()
b=zlib.decompress(b, bufsize=len(a))
print(b)
# print zlib.decompress(b) #outputs original contents of a
