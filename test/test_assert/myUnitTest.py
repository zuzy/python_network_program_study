#!/usr/bin/python
# -*- encode: utf-8 -*-

import sys

class bcolors:
    GREEN = '\033[36m'
    BLUE = '\033[38;5;097m'
    ORANGE= '\033[38;5;172m'
    RED = '\033[31m'
    ENDC = '\033[0m'

class TestBase(object):
    def __init__(self, header='Test_', init_header='Init_', deinit_header='Deinit_'):
        self._success = 0
        self._failure = 0
        self._header = header
        self._init_header = init_header
        self._deinit_header = deinit_header
    
    def _fun_from_header(self, header):
        return filter(lambda x: x.startswith(header) and callable(getattr(self,x)), dir(self))
    
    def _call_funs_from_header(self, header):
        iter = self._fun_from_header(header)
        for i in iter:
            try:
                getattr(self, i)()
            except Exception as e:
                print("call {} failed, with failure: {}".format(i, e))
                sys.exit(1)

    def testAll(self):
        print(bcolors.BLUE + '┌' + '─' * 40 + '┐')
        print(bcolors.BLUE + "│ Let's go {}:".format(self.__class__.__name__) + bcolors.ENDC)
        self._call_funs_from_header(self._init_header)
        iter = self._fun_from_header(self._header)
        for i in iter:
            print(bcolors.BLUE + '│' + bcolors.ORANGE + ('-' * 30))
            print(bcolors.BLUE + '│' + bcolors.ORANGE + "\ttesting {}".format(i) + bcolors.ENDC)
            test_result = getattr(self, i)()
            if test_result == False:
                print(bcolors.BLUE + '│' + bcolors.RED + "\tFailed!" + bcolors.ENDC)
                self._failure += 1
            else:
                print(bcolors.BLUE + '│' + bcolors.GREEN + "\tPassed!" + bcolors.ENDC)
                self._success += 1
        print(bcolors.BLUE + '│' + bcolors.ORANGE + '-' * 40)
        if self._failure > 0:
            print(bcolors.BLUE + '│' + bcolors.RED, end='')
        else:
            print(bcolors.BLUE + '│', end='')
        print("total test {}, success: {}, failed: {}".format(self._failure + self._success, self._success, self._failure))
        print(bcolors.BLUE + '└' + '─' * 40 + '┘' + bcolors.ENDC)
        self._call_funs_from_header(self._deinit_header)


if __name__ == "__main__":
    class TestCase(TestBase):
        def Init_Case(self):
            print(self.__class__.__name__, sys._getframe().f_code.co_name)
            return

        def Deinit_Case(self):
            print(self.__class__.__name__, sys._getframe().f_code.co_name)
            raise Exception("deinit failue")
            

        def Test_true(self):
            # print(self.__class__.__name__, sys._getframe().f_code.co_name)
            return True
        def Test_failure(self):
            return False
            # return True
        def Test_success(self):
            text = 'hello'
            text_list = ['hello' for i in range(3)]
            print(text_list)
            return True
    TestCase().testAll()
