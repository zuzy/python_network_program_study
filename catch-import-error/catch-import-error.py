#!/usr/bin/env python3

import re

try:
    import aaa
    import bbb
except ImportError as e:
    print(e)
    matchObj = re.match( r'No module named \'(.*)\'', str(e))
    if matchObj:
        print ("may you type to install: python3|python -m pip install {}".format(matchObj.group(1)))
