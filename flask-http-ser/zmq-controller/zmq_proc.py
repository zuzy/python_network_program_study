#!/usr/bin/python3

from multiprocessing import Process, Queue

from zmq.sugar.version import zmq_version
import zhelpers
import zmq
from zmq_common import *
import json, time

class ZmqHandler:
    def __init__(self):
        self._context = zmq.Context()
        # Socket facing clients
        self._ctrlRouter = self._context.socket(zmq.ROUTER)
        self._ctrlRouter.bind(BIND_FMT.format(ROUTER_PORT))

        self._ctrlRequester = self._context.socket(zmq.REQ)
        # print(BIND_FMT.format(CTRL_SIN_PORT))
        self._ctrlRequester.bind(BIND_FMT.format(CTRL_SIN_PORT))
        self._clients = []
        self._id = 0

        # Socket facing services
        # self._ctrlReq  = self._context.socket(zmq.REQ)
        # self._ctrlRouter.bind(BIND_FMT.format(CTRL_SIN_PORT))

    def discover(self):
        cmd = {
            'CMD':'setId',
            'BODY':str(self._id),
            'ID':0
        }
        self._clients.clear()
        id = ''
        while True:
            payload = json.dumps(cmd)
            self._ctrlRequester.send(payload.encode('utf-8'))
            request = self._ctrlRequester.recv()
            req = json.loads(request)
            print(payload, request)
            if 'BODY' not in req:
                print("cmd {} has no body".format(req))
                break
            if len(id) == 0:
                id = req['BODY']
            elif id == req['BODY']:
                break
            self._clients.append(req['BODY'])
            self._id += 1
            cmd['BODY'] = str(self._id)
            # time.sleep(0.01)
        print("clients: ", self._clients)

    def sendCmd(self, cmd, body='', client='', time=1):
        cmd = {
            'CMD':cmd,
            'BODY':body,
            'ID':0
        }
        payload = json.dumps(cmd)
        if client == '' :
            for cli in self._clients:
                for _ in range(time):
                    self._ctrlRouter.send_multipart([cli.encode('utf-8'), payload.encode('utf-8')])
                    msgs = self._ctrlRouter.recv_multipart()
                    for msg in msgs:
                        if msg != b'0':
                            print("REPLY", _, msg)
        else:
            if client in self._clients:
                for _ in range(time):
                    self._ctrlRouter.send_multipart([client.encode('utf-8'), payload.encode('utf-8')])
                    msgs = self._ctrlRouter.recv_multipart()
                    for msg in msgs:
                        if msg != b'0':
                            print("REPLY", _, msg)

    def proc(self):
        pass

if __name__ == '__main__':
    zh = ZmqHandler()
    time.sleep(1)
    zh.discover()
    time.sleep(1)
    zh.sendCmd('get_welcome', client='0', time=10)
    