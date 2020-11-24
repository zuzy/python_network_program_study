#!/usr/bin/python3

# import struct
# import serial
# import socket
# import threading
# import select
# from .crc16 import Crc16
# from .client import RequestError, NoHeaderError

# from .discovery import *
# from .discoveryServer import *
# from .utils_z import dump, testMemory, printCurUsage, countMemory

# from ctypes import *

# import time
# import binascii
# from .log import Log

# try:
#     from rpmsg.sysfs import RpmsgEndpoint
#     RpmsgEndpointReady = True
# except ImportError:
#     RpmsgEndpointReady = False


from threading import Thread, Lock, Timer
import time
import random, datetime

class Emqtt(Exception):
    pass

class Payloads(object):
    def __init__(self):
        self._cursor = 0
        self._len = 0
        self._contents = []
        print("init payloads")

    def push(self, content):
        self._len += len(content)
        self._contents.append(content)
    
    def get(self, length, force = False):
        if self._len <= length:
            if force :
                raise Emqtt("not enougth")
            else:
                length = self._len
        if length == 0:
            return None
        ba = bytearray(length)
        print("get from payloads", length)
        index = 0
        self._len -= length
        if self._cursor != 0:
            left = len(self._contents[0]) - self._cursor
            if left > length:
                ba[index:] = self._contents[0][self._cursor: self._cursor + length]
                self._cursor += length
                length = 0
            else:
                ba[index:] = self._contents[0][self._cursor:]
                self._cursor = 0
                index += left
                length -= left
                self._contents.pop(0)
    
        while len(self._contents) > 0 and len(self._contents[0]) <= length:
            ba[index:] = self._contents[0]
            length -= len(self._contents[0])
            index += len(self._contents[0])
            print(index, length, ba)
            self._contents.pop(0)
        else:
            if length > 0:
                ba[index:] = self._contents[0][0:length]
                self.m_cursor = length
        return ba
    
    def clear(self):
        self._contents.clear()
        self._len = 0
        self._cursor = 0


class PayloadLists(object):
    def __init__(self):
        self._lock = Lock()
        self._payloads = {}
    
    def push(self, topic, payloads):
        if payloads is None or len(payloads) == 0:
            return
        if type(payloads) is bytearray:
            p = bytes(payloads)
        elif type(payloads) is bytes:
            p = payloads
        else:
            raise Emqtt("wrong type payloads")
        
        with self._lock:
            if topic not in self._payloads:
                self._payloads[topic] = Payloads()
            self._payloads[topic].push(payloads)
    
    def pop(self, topic, length, force = False):
        with self._lock:
            if topic in self._payloads:
                return self._payloads[topic].get(length, force)
            else:
                raise Emqtt("{} is empty".format(topic))
    
    def clear(self, topic=None):
        with self._lock:
            if topic is None:
                self._payloads.clear()
            elif topic in self._payloads:
                self._payloads[topic].clear()
            else:
                raise Emqtt("No {} in payloadlist".format(topic))
                


class MqttStatus:
    single = 0
    met = 1
    dated = 2
    marriaged = 3

if __name__ == "__main__":
    def test_payloadlist():
        class Test(Thread):
            def __init__(self, topic, p, index, unit_len = 16):
                super().__init__(daemon=True)
                self.m_topic = topic
                self.m_unit = unit_len
                self.m_p = p
                self.m_index = index
                self.m_len = 0
            def run(self):
                print("start thread!")
                while True:
                    try:
                        content = self.m_p.pop(self.m_topic, self.m_unit)
                        if content:
                            self.m_len += len(content)
                            print("{} {}\tpop!!!!".format(self.m_index, self.m_len),content)
                    except Exception as e:
                        pass
                    time.sleep(1)
        p = PayloadLists()        
        topic = 'top1'
        cont = '1234567890'
        for i in range(4):
            t = Test(topic, p, i)
            t.start()
        for i in range(20):
            p.push(topic, cont.encode('utf-8'))
            time.sleep(0.2)

        time.sleep(5)
        while True:
            try:
                c = p.pop(topic, 1024)
                print("final pop", c)
                if not c:
                    break
            except Exception as e:
                print(e)
                break

    # test_payloadlist()

    def test_bytes():
        a = '123456\n'
        print(a)
        b = bytes('7890'.encode())
        s = bytearray(len(a) + len(b))
        print(b)
        s[0:] = a.encode()
        s[len(a):] = b
        print(s, len(s))
        i = s.index(0x0a)
        print(i)
        print(s[0:i].decode())
        print(s[i+1:])
    # test_bytes()

    class MqttConst:
        head = b'[HEAD]'
        discover = 'Discover'
        reply = 'Reply'
        confirm = 'Confirm'
        ping = 'Ping'
        pong = 'Pong'
        close = 'Close'
        timer_unit = 0.25
        timer_timeout = 1 / timer_unit
    def test_dict():
        seek = dict([(MqttConst.discover, "123456")])
        # seek = dict()
        # seek[MqttConst.discover] = '123455'
        print(seek)

    test_dict()
