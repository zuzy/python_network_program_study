#!/usr/bin/python3
# coding: utf-8

import json, os
from excel_module import *
from tkinter import *

_state_ = {
    'ban':'disable'
}
_color_ = {
    'off':'white',
    'on':'red',
}

def _trager_(status):
    if status == 'on' or status == True:
        return 'off'
    else:
        return 'on'

def _exclusive_(status):
    return 'off'

def _pass_(status):
    return status

def _parse_(status):
    if status == 'ban':
        return('disable', 'white')
    elif status == 'on':
        return('normal', 'red')
    else:
        return('normal', 'white')

class Relation():
    r_judge = {
        '-':'trager',
        '互斥':'exclusive',
        '共存':'pass',
    }
    d_judge = {
        '共存':True,
        '互斥':False,
    }
    c_judge = {
        '共存':False,
        '开':True,
        '关':False,
        '高':True,
        '低':False,
        '定时开':'timer_on',
        '定时关':'timer_off',
    }
    ban = '互斥'
    def __init__(self):
        pass

class Scene(Excel):
    ban = '互斥'
    judge = {
        '共存':False,
        '开':True,
        '关':False,
    }
    name = 'scene'
    staff = {}
    def __init__(self, path='relation.xlsx'):
        super().__init__(path, self.name)
        self.scenes = self.cols[0].copy()
        del(self.scenes[0])
        self.function = self.rows[0].copy()
        del(self.function[0])


class Chief(Excel, Relation):
    name = 'chief'
    def __init__(self, path='relation.xlsx'):
        Relation.__init__(self)
        Excel.__init__(self, path, self.name)
        self.chief = self.rows[0].copy()
        del(self.chief[0])
        self.relation = self.cols[0].copy()
        del(self.relation[0])

    def build(self):
        try:
            d = {}
            for nchf, chf in enumerate(self.chief):
                d[chf] = {}
                for nrel, rel in enumerate(self.relation):
                    d[chf][rel] = self.r_judge[self.rows[nchf+1][nrel+1]]
        except Exception as e:
            print('strong build failed, ', e)
        finally:
            return d


class Dependence(Excel, Relation):
    name = 'dependence'
    def __init__(self, path='relation.xlsx'):
        Excel.__init__(self, path, self.name)
        Relation.__init__(self)
        self.depends = self.rows[0].copy()
        del(self.depends[0])
        self.mj = self.cols[0].copy()
        del(self.mj[0])

    def build(self):
        try:
            ret = {}
            for n, major in enumerate(self.mj):
                ret[major] = []
                for d, dep in enumerate(self.depends):
                    if self.d_judge[self.rows[n+1][d+1]]:
                        ret[major].append(dep)
        except Exception as e:
            print('dep build', e)
        finally:
            print(ret)
            return ret
            
        pass


class Major():
    name = 'major'

    def __init__(self):
        self.chief = Chief()
        self.dep = Dependence()

    def build(self):
        c = self.chief.build()
        d = self.dep.build()
        

class Independence(Excel):
    judge = {
        '共存':True,
        '关闭':False,
        '立即关闭':False,
    }
    name = 'independence'
    staff = {}
    def __init__(self, path='relation.xlsx'):
        super().__init__(path, self.name)
        self.independece = self.rows[0].copy()

    def build(self, path):
        try:
            f = open(path, 'w')
            json.dump(self.independece, f, ensure_ascii=False, indent=4)
            f.close()
        except Exception as e:
            print(self.name, ' failed, ', e)
        pass
    
    def set_status(self, name, status):
        if name in self.independece:
            self.staff[name]['state'] = status
            if status == 'on':
                self.staff[name]['control']['bg'] = 'red'
            else:
                self.staff[name]['control']['bg'] = 'white'

    def callback(self, event):
        name =  event.widget['text']
        state_new = _trager_(self.staff[name]['state'])
        self.staff[name]['state'] = state_new
        event.widget['state'], event.widget['bg'] = _parse_(state_new)
        state = {}
        for indep in self.independece:
            state[indep] = self.staff[indep]['state']
        return state


    def paint(self, tk, pos, callback):
        for nindep, indep in enumerate(self.independece):
            self.staff[indep] = {
                'state':'off',
                'control':Button(tk, text=indep, bg='white')
            }
            self.staff[indep]['control'].bind('<Button-1>', callback)
            self.staff[indep]['control'].grid(row=pos[0], column=pos[1] + nindep)

        

class Reset(Excel):
    name = 'reset'
    def __init__(self, path = 'relation.xlsx'):
        try:
            super().__init__(path, self.name)
            self.reset = self.rows[0].copy()
        except Exception as e:
            print(self.name, ' init failed, ', e)
    
    def build(self, path):
        try:
            f = open(path, 'w')
            json.dump(self.reset, f, ensure_ascii=False, indent=4)
            f.close()
        except Exception as e:
            print(self.name, ' failed, ', e)
        pass

class Build():
    menu = 'module/'
    path = {
        'scene':'scene.json',
        'major':'major/',
        'independence':'independence.json',
        'reset':'reset.json'
    }
    state_path = '/tmp/state.json'
    def __init__(self, path = 'relation.xlsx'):
        os.system('mkdir ' + self.menu)
        self.chief = Chief()
        d = self.chief.build()
        print(d)

        self.dep = Dependence()
        self.dep.build()

        self.major = Major()
        self.major.build()
        

  




b = Build()
# b.run()