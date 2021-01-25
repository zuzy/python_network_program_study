#!/usr/bin/python3

from subprocess import Popen, PIPE
from collections import namedtuple

class ArpScan:
    def __init__(self) -> None:
        pass


SCAN_SHELL = 'sudo arp-scan -ql'

Pair = namedtuple('Pair', ['ip', 'mac'])

exIp = ['10.88.38.127']

exMac = ['48:e0:79:64:89:3e', '66:34:b0:6c:cd:e9', '66:34:b0:6c:cd:e1']


def rules(p):
    # print(p)
    if p.ip in exIp or p.mac in exMac:
        return False
    if p.mac.startswith('66:34'):
    # if p.mac.startswith('48'):
        return True
    return False


def arpscan(func=None):
    imTable = []
    with Popen(SCAN_SHELL, shell=True, stdout=PIPE) as proc:
        # print( proc.stdout.read().decode().split(' ') )
        for i in  proc.stdout.read().decode().split('\n'):
            try:
                ip, mac = i.split('\t')
                p = Pair(ip, mac)
                if func is not None and func(p) != True:
                    continue
                imTable.append(p)
            except:
                pass
    return sorted(imTable, key=lambda pair: pair.mac)
        # ip, mac = proc.stdout.read().decode().split(' ')
        

if __name__ == '__main__':
    # test()
    imlist = arpscan(rules)
    print(len(imlist))
    for im in imlist:
        print(im)
