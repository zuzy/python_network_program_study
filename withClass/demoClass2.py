#!/usr/bin/python3

import sys

class Context(object):
    def __init__(self, path):
        self.enter_ok = True
        self._path = path

    def __enter__(self):
        try:
            # raise Exception("Oops in __enter__")
            fp = open(self._path)
        except:
            if self.__exit__(*sys.exc_info()):
                self.enter_ok = False
            else:
                raise
        return self

    def __exit__(self, e_typ, e_val, trcbak):
        print ("Now this runs twice")
        return True


with Context(sys.argv[1]) as c:
    if c.enter_ok:
        print ("Only runs if enter succeeded")

print ("Execution continues")

with open("xxx") as f:
    pass