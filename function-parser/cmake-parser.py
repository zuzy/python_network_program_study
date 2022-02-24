#!/usr/bin/env python3

# 汇总cmake的所有dtu_cc_library，并生成一个静态库


import sys
import json
from log import *

class CmakeParser(object):
    def __init__(self, cmake_file):
        
        pass
    


_usage = 'usage {} \{CMAKELISTS.TXT\}'
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(_usage.format(sys.argv[0]))
    p = Parser(sys.argv[1])
    p.parse()
    p.dump()
