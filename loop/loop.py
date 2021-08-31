#!/usr/bin/env python3

import sys
import struct

def loop1(r):
    a = [j  for i in range(r) for j in range(i + 1)]
    print(a)

def loop2(l):
    a = ["({}, {})".format(i,j) for i in range(l) for j in range(l)]
    print(a)

def loopStruct(l):
    b = [i+j for i in range(l) for j in range(l)]
    print(b)
    c = struct.pack("I" * len(b), *b)
    print(c)
    

if __name__ == "__main__":
    loop1(int(sys.argv[1]))
    loop2(int(sys.argv[1]))
    loopStruct(int(sys.argv[1]))
    pass