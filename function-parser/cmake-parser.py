#!/usr/bin/env python3

import sys

class CmakeParser(object):
    def __init__(self, cmake_file):
        self._fin = open(cmake_file, 'r')

    def find_target(self, target):
        _find = False
        self._targets = []
        _tmp = ''
        for l in self._fin:
            if _find:
                _tmp += l
                if ')' in l:
                    self._targets.append(self.dispatch(_tmp))
                    _find = False
                    _tmp = ''
            elif target in l:
                _find = True
    
    def getvalues(self, key='NAME'):
        if key is None:
            return None
        key = key.upper()
        return [_t[key] for _t in self._targets if key in _t]
    
    def dump_key(self, key):
        values = self.getvalues(key)
        for _v in values:
            print(f"\t{_v}")

    def dump(self, key=None, ignore=False):
        if ignore and key is not None:
            key = key.upper()
        print('targets {}:'.format(key) if key is not None else 'targets:')
        
        for _t in self._targets:
            if key is not None:
                if key in _t:
                    print(f"\t{_t[key]}")
            else:
                print(f"\t{_t}")

    def dispatch(self, block):
        args = {}
        for l in block.splitlines():
            try:
                _as = l.split(None, 1)
                if len(_as) == 2:
                    args[_as[0].upper()] = _as[1].replace('(','').replace(')','').strip()
                else:
                    break
            except:
                break
        return args
    
    def get_names(self):
        return set(self.getvalues())
    
    def get_deps(self):
        _deps = set()
        link_deps = self.getvalues('link_deps')
        for _l in link_deps:
            _deps = _deps | set(_l.split())
        return _deps
    
    def deps(self, exclude=set()):
        _names = self.get_names()
        _deps = self.get_deps()
        return _names - _deps - exclude
      
    def combine(parser, libname):
        _names = parser.deps(set(libname,))
        if _names is None or len(_names) == 0:
            return None

        cmt_length = 45
        fmt_lib = ' STATIC LIBRARY lib{}.a '
        cmt_lib = fmt_lib.format(libname)
        if len(cmt_lib) > cmt_length:
            cmt_length = len(cmt_lib) + 2
        size = len(cmt_lib)
        ahead = (cmt_length - size) // 2
        left = cmt_length - size - ahead
        
        comment = '#' * cmt_length + '\n' + '#' * ahead + cmt_lib + '#' * left + '\n' + '#' * cmt_length + '\n'
        print(comment)

        fmt_head = 'add_library({} STATIC\n'
        fmt_body = '            $<TARGET_OBJECTS:{}>\n'
        fmt_end = ')\n'
        lib_str = fmt_head.format(libname)
        for _n in _names:
            lib_str += fmt_body.format(_n.strip())
        lib_str += fmt_end
        return lib_str

    
def combine(parser, libname):
    _names = parser.deps(set(libname,))
    if _names is None or len(_names) == 0:
        return None

    cmt_length = 45
    fmt_lib = ' STATIC LIBRARY lib{}.a '
    cmt_lib = fmt_lib.format(libname)
    if len(cmt_lib) > cmt_length:
        cmt_length = len(cmt_lib) + 2
    size = len(cmt_lib)
    ahead = (cmt_length - size) // 2
    left = cmt_length - size - ahead
    
    comment = '#' * cmt_length + '\n' + '#' * ahead + cmt_lib + '#' * left + '\n' + '#' * cmt_length + '\n'
    print(comment)

    fmt_head = 'add_library({} STATIC\n'
    fmt_body = '            $<TARGET_OBJECTS:{}>\n'
    fmt_end = ')\n'
    lib_str = fmt_head.format(libname)
    for _n in _names:
        lib_str += fmt_body.format(_n.strip())
    lib_str += fmt_end
    return lib_str


_usage = '''usage {0} {{CMAKELISTS.TXT}} {{LIBRARY_NAME}}
    List all dtu_cc_library functions & combine into a add_library({{LIBRARY_NAME}} ... )
    
    exp:
        $ {0} tops/sdk/lib/llir/CMakeLists.txt llir
        #############################################
        ######### STATIC LIBRARY libllir.a ##########
        #############################################

        add_library(llir STATIC
                    $<TARGET_OBJECTS:convert>
                    $<TARGET_OBJECTS:analysis>
                    $<TARGET_OBJECTS:builder>
                    $<TARGET_OBJECTS:ir>
                    ...
        )
    '''

_target = 'dtu_cc_library'

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(_usage.format(sys.argv[0]))
        exit(1)
    p = CmakeParser(sys.argv[1])
    p.find_target(_target)
    print(combine(p, sys.argv[2]))
            
