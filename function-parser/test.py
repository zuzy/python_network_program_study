#!/usr/bin/env python3

import sys
import json

t = '''name="database_proto",srcs=glob(["proto/database/*.proto"]))'''

_couples = {
    '(':')',
    '[':']',
    '-':'+',
}

m = min([t.index(i) if i in t else sys.maxsize for i in _couples.keys()])

print(m)
