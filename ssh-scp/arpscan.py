#!/usr/bin/python3

from subprocess import Popen, PIPE
from collections import namedtuple
import socket
import struct


def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]

def int2ip(addr):
    return socket.inet_ntoa(struct.pack("!I", addr))

def mac2int(mac):
    return int.from_bytes(bytes.fromhex(mac.replace(":", "")), byteorder='big')

# Pair = namedtuple('Pair', ['ip', 'mac'])

class ArpScan:
    SCAN_SHELL = 'sudo arp-scan -ql'

    def __init__(self, sortMac=True, *, rules=None, exIp = [], exMac = []) -> None:
        self._exIp = exIp
        self._exMac = exMac
        self._rules = rules
        self._sorter = 'mac' if sortMac else 'ip'
        pass

    @property
    def rules(self):
        return self._rules

    @rules.setter
    def rules(self, rules):
        self._rules = rules
    
    @property
    def excludeIp(self):
        return self._exIp
    
    @excludeIp.setter
    def excludeIp(self, exIps):
        self._exIp = exIps

    @property
    def excludeMac(self):
        return self._exMac
    
    @excludeMac.setter
    def excludeMac(self, exMacs):
        self._exMac = exMacs

    def scan(self, func=None):
        imTable = []
        with Popen(self.SCAN_SHELL, shell=True, stdout=PIPE) as proc:
            for i in  proc.stdout.read().decode().split('\n'):
                try:
                    ip, mac = i.split('\t')
                    if self._exclude(ip, mac):
                        continue
                    if self._rules is not None and self._rules(ip, mac) != True:
                        continue
                    imTable.append({'ip':ip, 'mac':mac})
                except:
                    pass
        return sorted(imTable, key=lambda p: p[self._sorter])

    def _exclude(self, ip, mac):
        return ip in self._exIp or mac in self._exMac
            
def rules(ip, mac):
    # print(p)
    # if mac.startswith('66:34'):
    if mac.startswith('48'):
        return True
    return False

if __name__ == '__main__':
    # scanner = ArpScan(rules, False)
    # scanner = ArpScan(rules)
    # scanner = ArpScan(None, False)
    scanner = ArpScan(rules=rules)
    scanner.excludeIp = ['10.88.38.127']
    scanner.excludeMac = ['48:e0:79:64:89:3e', '66:34:b0:6c:cd:e9', '66:34:b0:6c:cd:e1']


    imlist = scanner.scan()
    print(len(imlist))
    for im in imlist:
        print(im)
