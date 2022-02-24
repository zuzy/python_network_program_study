#!/usr/bin/python3
# coding: utf-8

import socket
import time

ms = 1000
us = ms * 1000
# unit = us
unit = ms

class Log(object):
    spend = 0
    able = False
    obj = None
    def __init__(self):
        Log.able = False
        self._fd = None
        Log.obj = self
    
    @classmethod
    def print(cls, *args, end="\n"):
        if cls.obj and cls.able:
            s = "{}".format(''.join((map(str, args)))) + end
            cls.obj._base_print(s)
            cls.obj.flush()
    
    def _base_print(self, msg):
        print(msg, end="", flush=True)
    
    def flush(self):
        pass

    def close(self):
        if self._fd:
            self._fd.close()
        self._fd = None
        self._enable = False
        Log.able = False

    @classmethod
    def enable(cls):
        cls.able = True
        cls.spend = 0
    
    @classmethod
    def disable(cls):
        cls.able = False
        cls.spend = 0
    
    @classmethod
    def timeCounter(cls, func):
        def f(*args, **kwargs):
            if True:
                _s = int(round(time.time() * unit))
                result = func(*args, **kwargs)
                _e = int(round(time.time() * unit))
                cls.spend = int(_e - _s)
                cls.spend = cls.spend if cls.spend > 0 else 1
            else:
                result = func(*args, **kwargs)
            return result
        return f


class TCP_log(Log):
    def __init__(self, ip, port):
        super().__init__()
        try:
            self._fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._fd.connect((ip, port))
            Log.obj = self
        except:
            self._fd = None
    
    def _base_print(self, msg):
        if self._fd:
            self._fd.send(msg.encode('utf-8'))
        else:
            super()._base_print(msg)


class UDP_log(Log):
    def __init__(self, ip, port):
        super().__init__()
        self._addr = (ip, port)
        try:
            self._fd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            Log.obj = self
        except:
            self._fd = None
    
    def _base_print(self, msg):
        try:    
            if self._fd == None:
                raise AssertionError
            self._fd.sendto(msg.encode('utf-8'), self._addr)
        except:
            super()._base_print(msg)


class File_log(Log):
    def __init__(self, path, opt = "w"):
        super().__init__()
        try:
            self._fd = open(path, opt)
            Log.obj = self
        except:
            self._fd = None
    
    def _base_print(self, msg):
        if self._fd:
            self._fd.write(msg)
        else:
            super()._base_print(msg)
    
    def flush(self):
        if self._fd:
            self._fd.flush()
    
class Test(object):
    def __init__(self, log):
        self._log = log

    @Log.timeCounter
    def test(self):
        self._log.enable()
        print(self._log.able)
        for i in range(10):
            self._log.print("log {}".format(i))
        Log.disable()
        print(self._log.able)
        for i in range(10):
            self._log.print("log \\t {}".format(i), end="\t")
        self._log.print()
        self._log.close()

def test():
    t = Test(Log())
    Log.enable()
    # t.test()
    # t.test()
    for i in range (10) :
        Log.print("hello ", i)
    # t = Test(Log())
    # t.test()
    t = Test(File_log("demo.log", "a"))
    t.test()

def test_file():
    t = Test(File_log("demo.log"))
    Log.enable()
    # t.test()
    # t.test()
    for i in range (10) :
        Log.print("hello ", i)
    # t = Test(Log())
    # t.test()
    t = Test(File_log("demo.log", "a"))
    t.test()

def test_tcp():
    t = Test(TCP_log("127.0.0.1", 12345))
    Log.enable()
    for i in range (10) :
        Log.print("hello ", i)
        
    print(Log.spend)
    print(TCP_log.spend)

def test_udp():
    # t = Test(UDP_log("127.0.0.1", 12345))
    t = Test(UDP_log("localhost", 12345))
    t.test()
    print(UDP_log.spend)
    

if __name__ == "__main__":
    # test_udp()
    # test_file()
    test()
    # test_tcp()
    # test_udp()
    pass