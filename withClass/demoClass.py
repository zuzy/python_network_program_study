#!/usr/bin/python3

import sys

class Context(object):
    def __enter__(self):
        try:
            raise Exception("Oops in __enter__")
        except:
            # Swallow exception if __exit__ returns a True value
            if self.__exit__(*sys.exc_info()):
                pass
            else:
                raise


    def __exit__(self, e_typ, e_val, trcbak):
        print( "Now it's running")


with Context():
    pass

