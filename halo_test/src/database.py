#!/usr/bin/python3
# coding: utf-8
import json

class Database:
    _dev = 'getdevices'
    _sce = 'getscenes'
    _flr = 'getfloors'
    _rm = 'getrooms'
    path = {
        _dev:'device.db',
        _sce:'scene.db',
        _flr:'floor.db',
        _rm:'room.db',
    }
    def __init__(self, menu = 'dev_db/'):
        self.menu = menu
    def __dump(self, p):
        try:
            dev_path = self.menu + p
            f = open(dev_path)
            dev_str = f.read()
            s = json.dumps(json.loads(dev_str, encoding='utf-8'))
            return s
        except Exception as e:
            print('database read error',e)
            return None
    def dump_dev(self):
        return self.__dump(self.path[self._dev])
    def dump_sce(self):
        return self.__dump(self.path[self._sce])
    def dump_flr(self):
        return self.__dump(self.path[self._flr])
    def dump_rm(self):
        return self.__dump(self.path[self._rm])
    def dumps(self, cmd):
        if cmd in self.path:
            return self.__dump(self.path[cmd])
        else:
            return None


# d = Database()
# print(d.dump_dev())
# print(d.dump_sce())
# print(d.dump_flr())
# print(d.dump_rm())
