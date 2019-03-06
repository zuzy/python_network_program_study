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
    

class Scene(Excel):
    ban = '互斥'
    judge = {
        '共存':False,
        '开':True,
        '关':False,
    }
    name = 'scene'
    def __init__(self, path='relation.xlsx'):
        super().__init__(path, self.name)
        self.scenes = self.cols[0].copy()
        del(self.scenes[0])
        self.function = self.rows[0].copy()
        del(self.function[0])

    def build(self, path):
        try:
            f = open(path, 'w')
            d = {}
            for nsce, sce in enumerate(self.scenes):
                d[sce] = {}
                for nfun, fun in enumerate(self.function):
                    rel = self.rows[nsce+1][nfun+1]
                    if rel != self.ban:
                        d[sce][fun] = self.judge[rel]
            json.dump(d, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(e)
    
    def paint(self, tk):
        pass


class Strong(Excel):
    judge = {
        '-':'trager',
        '互斥':'exclusive',
        '共存':'pass',
    }
    name = 'strong'
    def __init__(self, path='relation.xlsx'):
        super().__init__(path, self.name)
        self.strong = self.rows[0].copy()
        del(self.strong[0])
        self.relation = self.cols[0].copy()
        del(self.relation[0])

    def build(self, path):
        try:
            f = open(path, 'w')
            self.path = path
            d = {}
            for nstg, stg in enumerate(self.strong):
                d[stg] = {}
                for nrel, rel in enumerate(self.relation):
                    d[stg][rel] = self.judge[self.rows[nstg+1][nrel+1]]
            json.dump(d, f, ensure_ascii=False, indent=4)
            f.close()
        except Exception as e:
            print('strong build failed, ', e)
    
    def get_relation(self):
        f = open(self.path, 'r')
        rel = json.load(f)
        f.close()
        return rel

class Dependence(Excel):
    ban = '互斥'
    judge = {
        '共存':False,
        '开':True,
        '关':False,
        '高':True,
        '低':False,
        '定时开':'timer_on',
        '定时关':'timer_off',
    }
    name = 'dependence'
    def __init__(self, path='relation.xlsx'):
        super().__init__(path, self.name)
        self.depends = self.rows[0].copy()
        del(self.depends[0])

    def build(self, menu):
        try:
            os.system('mkdir ' + menu)
            self.path = menu
            self.strongs = self.cols[0].copy()
            del(self.strongs[0])
            for nstg, stg in enumerate(self.strongs):
                f = open(menu  + stg, 'w')
                d = {}
                for ndp, dp in enumerate(self.depends):
                    tmp = self.rows[nstg + 1][ndp + 1]
                    if tmp == self.ban:
                        continue
                    if type(tmp) == float:
                        d[dp] = int(tmp)
                    else:
                        l = tmp.split(':')
                        if len(l) == 1:
                            d[dp] = self.judge[l[0]]
                        else:
                            d[dp] = {
                                'state':self.judge[l[0]],
                                'val':l[1]
                            }
                json.dump(d, f, ensure_ascii=False, indent=4)
                f.close()
        except Exception as e:
            print('depends build failed, ', e)
    
    def get_relation(self):
        self.rela = {}
        for stg in self.strongs:
            f = open(self.path + stg, 'r')
            self.rela[stg] = json.load(f)
            f.close()
        return self.rela


class Major():
    name = 'major'
    path = {
        'strong':'strong.json',
        'dependence':'dependence/'
    }
    staff = {}
    def __init__(self):
        self.strong = Strong()
        self.dependence = Dependence()

    def build(self, menu):
        os.system('mkdir ' + menu)
        self.strong_relation_path = menu + self.path['strong']
        self.strong.build(self.strong_relation_path)
        self.stg_rela = self.strong.get_relation()
        

        self.dependence.build(menu + self.path['dependence'])
        self.dep_rela = self.dependence.get_relation()

    def update_status(self, name):
        rela = self.stg_rela[name]
        for s, r in rela.items():
            if r == 'trager':
                self.staff[s]['state'] = _trager_(self.staff[s]['state'])
            elif r == 'exclusive':
                self.staff[s]['state'] = 'off'
            else:
                pass
            self.staff[s]['control']['bg'] = _color_[self.staff[s]['state']]
    
    def update_dep_status(self, name):
        rela = {}
        for n, r in self.dep_rela.items():
            print('%s %s' % (n, r))
            if self.staff[n]['state'] == 'on':
                for k_r, v_r in r.items():
                    rela[k_r] = v_r
        if self.staff[name]['state'] == 'on':
            for k_r, v_r in self.dependence.rela[name].items():
                rela[k_r] = v_r
        
        print('rela: ', rela)
        for dep in self.dependence.depends:
            if dep in rela:
                self.staff[dep]['control']['state'] = 'normal'
                print(dep, ',',type(rela[dep]))
                if rela[dep] == False:
                    self.staff[dep]['state'] = 'off'
                    self.staff[dep]['control']['bg'] = 'white'
                    self.staff[dep]['control']['text'] = dep
                elif rela[dep] == True:
                    self.staff[dep]['state'] = 'on'
                    self.staff[dep]['control']['bg'] = 'red'
                    self.staff[dep]['control']['text'] = dep
                elif type(rela[dep]) == int:
                    print(rela[dep])
                    self.staff[dep]['state'] = 'on'
                    self.staff[dep]['control']['bg'] = 'red'
                    self.staff[dep]['control']['text'] = dep + ':' + str(rela[dep])
                else:
                    self.staff[dep]['state'] = 'on'
                    print(type(rela[dep]))
                    if rela[dep]['state'] == 'timer_off':
                        self.staff[dep]['control']['bg'] = 'green'
                    else:
                        self.staff[dep]['control']['bg'] = 'blue'
                    self.staff[dep]['control']['text'] = dep + ':' + rela[dep]['val']
            else:
                self.staff[dep]['state'] = 'ban'
                self.staff[dep]['control']['bg'] = 'white'
                self.staff[dep]['control']['state'] = 'disable'
                self.staff[dep]['control']['text'] = dep
        pass


        
    def s_callback(self, event):
        name =  event.widget['text']
        self.update_status(name)
        self.update_dep_status(name)
        

    def d_callback(self, event):
        if event.widget['state'] == 'disabled':
            return
        name_all =  event.widget['text'].split(':')
        name = name_all[0]
        

        print(self.staff[name]['state'])
        state_new = _trager_(self.staff[name]['state'])
        print(state_new)
        self.staff[name]['state'] = state_new
        event.widget['state'], event.widget['bg'] = _parse_(state_new)

    def paint(self, tk, pos):
        for nstg, stg in enumerate(self.strong.strong):
            self.staff[stg] = {
                'state':'off',
                'control':Button(tk, text=stg, bg='white')
            }
            self.staff[stg]['control'].bind('<Button-1>', self.s_callback)
            self.staff[stg]['control'].grid(row=pos[0], column=pos[1] + nstg)
        offset = len(self.strong.strong) + pos[1]
        for ndep, dep in enumerate(self.dependence.depends):
            self.staff[dep] = {
                'state':'ban',
                'control':Button(tk, text=dep, bg='white', state='disable')
            }
            self.staff[dep]['control'].bind('<Button-1>', self.d_callback)
            self.staff[dep]['control'].grid(row=pos[0], column=offset+ndep)

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
    
    def callback(self, event):
        name =  event.widget['text']
        state_new = _trager_(self.staff[name]['state'])
        self.staff[name]['state'] = state_new
        event.widget['state'], event.widget['bg'] = _parse_(state_new)


    def paint(self, tk, pos):
        for nindep, indep in enumerate(self.independece):
            self.staff[indep] = {
                'state':'off',
                'control':Button(tk, text=indep, bg='white')
            }
            self.staff[indep]['control'].bind('<Button-1>', self.callback)
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
        # 'strong':'strong.json',
        # 'dependence':'dependence/',
        'independence':'independence.json',
        'reset':'reset.json'
    }
    state_path = '/tmp/state.json'
    def __init__(self, path = 'relation.xlsx'):
        os.system('mkdir ' + self.menu)

        self.reset = Reset()
        self.reset.build(self.menu + self.path[self.reset.name])

        self.scene = Scene()
        self.scene.build(self.menu + self.path[self.scene.name])

        self.independence = Independence()
        self.independence.build(self.menu + self.path[self.independence.name])

        self.major = Major()
        self.major.build(self.menu + self.path[self.major.name])
        

        # self.strong = Strong()
        # self.strong.build(self.menu + self.path[self.strong.name])

        # self.dependance = Dependance()
        # self.dependance.build(self.menu + self.path[self.dependance.name])

        self.init_status()
        self.init_tk()
    
    def init_status(self):
        print(self.reset.reset)
        
        print(self.scene.scenes)
        print(self.independence.independece)
        print(self.major.strong.strong)
        print(self.major.dependence.depends)
        pass

    def init_tk(self):
        self.tk = Tk()
        self.independence.paint(self.tk, (0,0))
        self.major.paint(self.tk, (1, 0))
    
    def run(self):
        mainloop()




b = Build()
b.run()