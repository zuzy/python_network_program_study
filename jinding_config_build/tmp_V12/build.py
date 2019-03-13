#!/usr/bin/python3
# coding: utf-8

import json, os
from excel_module import *
from tkinter import *
import lupa
from time import perf_counter as counter

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
    disable = 'disable'
    def __init__(self):
        pass
    def parse_state(self, state):
        if state == self.disable:
            return 'disable', 'white'
        elif state:
            return 'normal', 'red'
        else:
            return 'normal', 'white'

    def trager(self, state):
        if not state:
            return True
        else:
            return False

class Scene(Excel, Relation):
    name = 'scene'

    def __init__(self, path='relation.xlsx'):
        Excel.__init__(self, path, self.name)
        Relation.__init__(self)
        self.scenes = self.cols[0].copy()
        del(self.scenes[0])
        self.function = self.rows[0].copy()
        del(self.function[0])
    def build(self):
        self.rule = {}
        for nsce, sce in enumerate(self.scenes):
            self.rule[sce] = {}
            for nfun, fun in enumerate(self.function):
                cont = self.rows[nsce + 1][nfun + 1]
                if cont != self.ban :
                    self.rule[sce][fun] = self.c_judge[cont]
                    # self.rule[sce][fun] = False
        return self.rule


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
            return ret
            
        pass


class Major():
    name = 'major'

    def __init__(self):
        self.chief = Chief()
        self.dep = Dependence()

    def build(self):
        chiefs = self.chief.build()
        deps = self.dep.build()
        self.rule = chiefs
        self.rule['dependence'] = self.dep.depends
        for nd, d in deps.items():
            self.rule[nd]['deps'] = d
        return self.rule
        

class Independence(Excel, Relation):
    judge = {
        '共存':True,
        '关闭':False,
        '立即关闭':False,
    }
    name = 'independence'
    staff = {}
    def __init__(self, path='relation.xlsx'):
        Excel.__init__(self, path, self.name)
        Relation.__init__(self)
        self.independece = self.rows[0].copy()

    def build(self):
        return self.independece

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
    
    def build(self):
        return self.reset

class Build(Relation):
    menu = 'module/'
    path = {
        'major':'major/',
        'scene':'scene.conf',
        'independence':'independence.conf',
        'reset':'reset.json'
    }
    state_path = '/tmp/state.json'
    staff = {}
    def __init__(self, path = 'relation.xlsx'):
        Relation.__init__(self)
        os.system('mkdir ' + self.menu)

        self.Sce = Scene()
        self.sce = self.Sce.scenes

        s_conf = self.Sce.build()
        # print(s_conf)
        f = open(self.menu + 'scene.conf', 'w')
        json.dump(s_conf, f, ensure_ascii=False)
        f.close()

        self.Major = Major()
        self.chief = self.Major.chief.chief
        self.depends = self.Major.dep.depends
        # print('dep', self.depends)
        rule = self.Major.build()
        # print(rule)
        f = open(self.menu + 'major.rule', 'w')
        json.dump(rule,f, ensure_ascii=False)
        f.close()

        f = open(self.menu + 'depends.conf', 'w')
        json.dump(self.depends, f, ensure_ascii=False)
        f.close()

        for rk, rv in rule.items():
            if 'deps' in rv:
                f = open(self.menu + rk + '.conf', 'w')
                d = {}
                for dep in rv['deps']:
                    d[dep] = False
                json.dump(d, f, ensure_ascii=False)
                f.close()

        self.Indep = Independence()
        self.indep = self.Indep.independece
        indep = self.Indep.build()
        # print(indep)
        f = open(self.menu + 'indep.conf', 'w')
        json.dump(indep, f, ensure_ascii=False)
        f.close()
        # self.stand_alone = self.indep.copy()
        # self.stand_alone.extend(self.depends)
        # print('stand-alone', self.stand_alone)
        self.Reset = Reset()
        self.reset = self.Reset.build()
        print(self.reset)
        f = open(self.menu + 'reset.conf', 'w')
        json.dump(self.reset, f, ensure_ascii=False)
        f.close()


        state = self.init_state()
        # print('state', state)
        self.init_staff(state)



    def init_state(self):
        state = {}
        for sce in self.sce:
            state[sce] = False
        for chief in self.chief:
            state[chief] = False
        for dep in self.depends:
            state[dep] = self.disable
        for indep in self.indep:
            state[indep] = False
        for reset in self.reset:
            state[reset] = False
        # print(state)
        f = open(self.menu + 'state.json', 'w')
        json.dump(state, f, ensure_ascii=False)
        f.close()
        return state
    
    def init_buttons(self, tk, row, offset, names, callback, state):
        for i, n in enumerate(names):
            st, bg = self.parse_state(state[n])
            self.staff[n] = {
                'state':state[n],
                'widget':Button(tk, text=n, bg=bg, state=st)
            }
            self.staff[n]['widget'].bind('<Button-1>', callback)
            self.staff[n]['widget'].grid(row=row, column=(i+offset))

    def scene_check(self, state):
        f = open(self.menu + 'scene.conf', 'r')
        sce = json.load(f)
        f.close()
        for ks, vs, in sce.items():
            if state[ks]:
                for fun, st in vs.items():
                    if st and not state[fun]:
                        # print(ks, state[ks], fun, state[fun], st)
                        state[ks] = False
                        break
        return state

    def scene_control(self, name, state, on):
        f = open(self.menu + 'scene.conf', 'r')
        sce = json.load(f)
        f.close()
        state[name] = on
        for k, v in sce[name].items():
            # if v:
            state = v and self.fun(state, k, on) or state
        return state

    def callback(self, event):
        name = event.widget['text'].split(':')[0]
        print('passed', name)
        f = open(self.menu + 'state.json', 'r')
        state = json.load(f)
        f.close()
        if state[name] == self.disable:
            print(name, ' disable ')
            return
        print('state old', state)

        '''
            main logic part
        '''
        _start = counter()
        f = os.popen('pwd', 'r')
        pwd = f.read().strip()
        f.close()
        if False:
            script = pwd + '/state_machine'
            f = os.popen(script + (" '%s'" % name), 'r')
            print("system call c spend %d ms!!!" % ((counter() - _start) * 1000 ))
        else:
            script = pwd + '/state_machine.lua'
            f = os.popen("lua "+ script + (" '%s'" % name), 'r')
            print("system call lua spend %d ms!!!" % ((counter() - _start) * 1000 ))
        # print('popen',f.read())
        state = json.load(f)
        f.close()
        # self.scene_check(state)
        
        # if name not in self.sce:
        #     # state = self.fun(state, name)
        #     f = os.popen("lua ~/project/python_network_program_study/jinding_config_build/tmp_V06/state_machine.lua '%s'" % name, 'r')
        #     # print('popen',f.read())
        #     state = json.load(f)
        #     f.close()
        #     self.scene_check(state)
        # else:

        #     if not state[name]:
        #         '''
        #         disable all other enabled scene!
        #         '''
        #         for s in self.sce:
        #             if state[s]:
        #                 state.update(self.scene_control(s, state, False))
        #         # [state.update(self.scene_control(s, state, False)) for s in self.sce]
        #         state[name] = True
        #     else:
        #         state[name] = False
        #     self.scene_control(name, state, state[name])
        '''
        main logic end
        '''
                    
        print('state new', state)
        self.button_update(state)  
        f = open(self.menu + 'state.json', 'w')
        json.dump(state, f)
        f.close()

    def init_staff(self, state):
        self.tk = Tk()
        self.init_buttons(self.tk, 0, 0, self.reset, self.callback, state)
        self.init_buttons(self.tk, 1, 0, self.sce, self.callback, state)
        self.init_buttons(self.tk, 2, 0, self.indep, self.callback, state)
        self.init_buttons(self.tk, 3, 0, self.chief, self.callback, state)
        self.init_buttons(self.tk, 4, 0, self.depends, self.callback, state)
        
    def run(self):
        mainloop()



    def get_active_depends(self, state, action):
        tmp = {}
        for dep in self.depends:
            tmp[dep] = self.disable
        for chf in self.chief:
            if state[chf] and chf != action:
                f = open(self.menu + chf + '.conf' , 'r')
                tmp.update(json.load(f))
                f.close()
        if state[action]:
            f = open(self.menu + action + '.conf' , 'r')
            tmp.update(json.load(f))
            f.close()
        return tmp


    def fun(self, state, action, result='unknow'):
        # print('stand alone', self.stand_alone)
        # print('state old', state)
        if state[action] == self.disable:
            return state
        if self.depends.count(action) > 0:
            # print('depeneds passed')
            state[action] = False
            # state[action] = self.trager(state[action])
        elif self.indep.count(action) > 0:
            if result == 'unknow':
                state[action] = self.trager(state[action])
            else:
                state[action] = result
        else:
            '''
            equal to `elif action in self.chief:`
            action is in major function, some rule exclusive in need
            '''
            f = open(self.menu + 'major.rule', 'r')
            major_rule = json.load(f)
            f.close()
            rule = major_rule[action]
            if result == 'unknow':
                state[action] = self.trager(state[action])
            else:
                state[action] = result

            for chf, rela in rule.items():
                if (chf in state) and (rela == 'exclusive'):
                    state[chf] = False
            deps = self.get_active_depends(state, action)
            state.update(deps)
            # print('state new',state)
            f = open(self.menu + 'state.json', 'w')
            json.dump(state, f)
            f.close()
        return state

    def button_update(self, state):
        for ks, vs in state.items():
            self.staff[ks]['state'] = vs
            self.staff[ks]['widget']['state'], self.staff[ks]['widget']['bg'] = self.parse_state(vs)




        
b = Build()
b.run()
# lua = lupa.LuaRuntime()
# # lua['package']['path'] = '/tmp/lua/?.lua'
# sm = lua.require('state_machine')