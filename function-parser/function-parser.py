#!/usr/bin/env python3

import sys
import json
from log import *

class Parser:
    def __init__(self, path):
        self._path = path
        self._funcs = []
        self._getstr()
        self._log = Log()
        # self._log.enable()

    def purebody(self, body, left):
        return left not in body

    def getbody(self, body, left='(', right=')', offset=0):
        self._log.print(f'getbody : {left} {right}')
        if self.purebody(body, left):
            return body.split(right)[0], None
        _i = offset + 1
        deep = 0
        while True:
            self._log.print('-'*30, _i, self.purebody(body, left))
            self._log.print(body[_i:])
            _il = body.index(left, _i) if left in body[_i:] else sys.maxsize
            _ir = body.index(right, _i)
            if _il > _ir:
                if deep == 0:
                    return body[:_ir+1], body[_ir+1:]
                else:
                    deep -= 1
                    _i = _ir + 1
            else:
                _i = _il + 1
                deep += 1
            self._log.print("-----  deep", deep)

    
    def seperateBody(self, block):
        _couples = {
            '(':')',
            '[':']',
        }
        
        body = {}
        while True:
            if block is not None and '=' in block:
                if block.startswith(','):
                    block = block.split(',', 1)[1]
                    
                h, t = block.split('=', 1)
                self._log.print("seperate:", h, t)
                if t[0] == '"':
                    _i = t[1:].index('"') + 1
                    v, block = t[1:_i], t[_i + 1:]
                elif t[0] in _couples:
                    self._log.print("-----", t[0])
                    v, block = self.getbody(t, t[0], _couples[t[0]])
                else:
                    m = min([t.index(i) if i in t else sys.maxsize for i in _couples.keys()])
                    # m = min([i for i in _couples.keys() and i in t])
                    self._log.print('min', m)
                    v, block = self.getbody(t, t[m], _couples[t[m]], m)
                body[h.replace('"', '')] = v.replace('"', '')
            else:
                break
        return body

    def getfun(self, body):
        try:
            args = body.split('(', 1)
            if len(args) == 2:
                return args[0], args[1]
            else:
                return None, None
        except :
            return None, None
    
    def dump(self):
        print(json.dumps(self._funcs, ensure_ascii=True, indent=4))
    
    def _getstr(self):
        with open(self._path) as f:
            self._strs = f.read()

    def parse(self):
        left = self._strs.replace('\n', '').replace(' ','')
        while True:
            func, left = self.getfun(left)
            self._log.print('+' * 10, func)
            if func is None:
                return
            else:
                body, left = self.getbody(left)
                self._log.print(f'\t++body: {body}')
                self._log.print(f'\t\t++left: {left}')
                # self._funcs.append({'func':func, 'body':body})
                self._funcs.append({'func':func, 'body':self.seperateBody(body)})


_usage = 'usage {} \{path\}'
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(_usage.format(sys.argv[0]))
    p = Parser(sys.argv[1])
    p.parse()
    p.dump()

