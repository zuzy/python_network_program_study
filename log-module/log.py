#!/usr/bin/python3
# coding: utf-8

import socket
import time

class Log(object):
    _fd = None

    def __init__(self):
        self.close()
    
    @classmethod
    def print(self, *args, end="\n"):
        s = "{}".format(''.join((map(str, args)))) + end
        self._base_print(s)
    
    @classmethod    
    def _base_print(self, msg):
        print(msg, end="")
    
    @classmethod
    def close(self):
        if self._fd:
            self._fd.close()
            self._fd = None
    

class TCP_log(Log):
    def __init__(self, ip, port):
        super().__init__()
        self._ip = ip
        self._port = port
        self.open()
    
    def open(self):
        try:
            self._fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._fd.connect((self._ip, self._port))
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
        self.open()
    
    def open(self):
        try:
            self._fd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except:
            self._fd = None
    
    def _base_print(self, msg):
        try:    
            if self.fd == None:
                raise AssertionError
            self._fd.sendto(msg.encode('utf-8'), self._addr)
        except:
            super()._base_print(msg)
    
    
class File_log(Log):
    def __init__(self, path, opt = "w"):
        super().__init__()
        self._path = path
        self._opt = opt
        self.open()
    
    def open(self):
        try:
            self._fd = open(self._path, self._opt)
        except:
            self._fd = None
    
    def _base_print(self, msg):
        if self._fd:
            self._fd.write(msg)
        else:
            super()._base_print(msg)
    
class Test(object):
    def __init__(self, log):
        self._log = log

    def test(self):
        for i in range(10):
            self._log.print("log {}".format(i))
        for i in range(10):
            self._log.print("log \\t {}".format(i), end="\t")
        self._log.print()
        self._log.close()

def count(func):
    def wrapped(*args, **kwargs):
        _start_time = int(round(time.time() * 1000))
        output = func(*args, **kwargs)
        _end_time = int(round(time.time() * 1000))
        print('-' * 80)
        print("{} spend {}ms".format(func.__name__, _end_time - _start_time))
        print('-' * 80)
        return output
    return wrapped

@count
def test_file():
    t = Test(File_log("demo.log"))
    t.test()
    # t = Test(Log())
    # t.test()
    t = Test(File_log("demo.log", "a"))
    t.test()

@count
def test_tcp():
    t = Test(TCP_log("127.0.0.1", 12345))
    t.test()

@count
def test_udp():
    # t = Test(UDP_log("127.0.0.1", 12345))
    t = Test(UDP_log("localhost", 12345))
    t.test()



if __name__ == "__main__":
    # test_udp()
    # test_file()
    test_tcp()
    pass
