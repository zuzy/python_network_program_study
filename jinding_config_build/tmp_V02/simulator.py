#!/usr/bin/python3
from excel_module import *
from tkinter import *
import json

class Simulator(Index):
    s_path = '/tmp/state.json'
    menu = 'config/'
    button_names = None
    buttons = {}
    colors = {
        'on': 'red',
        'off': 'white',
    }
    states = {
        'red':True,
        'white':False
    }
    names = []
    
    def __init__(self):
        super().__init__()
        # self.button_names = self.buttons
        self.init_state()        
        self.tk = Tk()
        d_state = self.get_state()
        self._init_buttons(d_state)


    def _init_buttons(self, d_state):
        init_colors = {
            'on': 'red',
            'off': 'white',
            'ban': 'white',
            'stay':'white'
        }
        for i, name_list in enumerate(self.button_names):
            for j, name in enumerate(name_list):
                if len(name) > 0:
                    self.names.append(name)
                    (row, col) = (int(i * 2 + j / 4), int(j % 4))
                    status = ((d_state[name] == 'ban') and 'disable') or 'active'

                    self.buttons[name] = Button(self.tk, state=status, text=name, bg=init_colors[d_state[name]])
                    self.buttons[name].bind('<Button-1>', self.button_callback)
                    self.buttons[name].grid(row=row, column=col)
    def run(self):
        mainloop()

    def init_state(self):
        d = {
            "离开": "off",
            "凉风扇外": "off",
            "照明": "off",
            "风速": "ban",
            "凉风内": "off",
            "洗浴场景": "off",
            "负离子": "off",
            "热干": "off",
            "音乐": "off",
            "换气扇内": "off",
            "电源": "off",
            "取暖": "off",
            "摆风": "ban",
            "洗漱场景": "off",
            "换气扇外": "off",
            "取暖模式": "off",
            "凉干": "off",
            "如厕场景": "off",
            "空气检测": "off"
        }
        f = open(self.s_path, 'w')
        f.write(json.dumps(d, ensure_ascii=False, indent=4))
        f.close()

    def get_state(self):
        f = open(self.s_path, "r")
        d_state = json.loads(f.read())
        f.close()
        return d_state
    
    def set_state(self, state):
        f = open(self.s_path, "w")
        f.write(json.dumps(state, ensure_ascii=False, indent=4))
        f.close()
    
    def get_status(self, name, state):
        f = open(self.menu + name + '.json', 'r')
        d_status = json.loads(f.read())
        f.close()
        return d_status
    
    def get_button_status_onoff(self, name):
        btn = self.buttons[name]
        if btn['bg'] == 'red':
            return 'on'
        else:
            return 'off'

    def get_button_status(self, name):
        btn = self.buttons[name]
        if btn['state'] == 'disabled':
            return 'ban'
        if btn['bg'] == 'red':
            return 'on'
        else:
            return 'off'

    def draw_buttons(self, state):
        for n, s in state.items():
            if s == 'ban':
                self.buttons[n]['state'] = 'disable'
                self.buttons[n]['bg'] = 'white'
            else:
                self.buttons[n]['state'] = 'normal'
                if s == 'on':
                    self.buttons[n]['bg'] = 'red'
                else:
                    self.buttons[n]['bg'] = 'white'
            

    def update_buttons(self, name_in, state):
        status = self.get_status(name_in, state)
        print(status)
        for name in self.names:
            if status[name] == 'stay':
                if name == name_in:
                    if state:
                        status[name] = 'off'
                    else:
                        status[name] = 'on'
                else:
                    status[name] = self.get_button_status(name)

        print(self.depends)
        for dep_name, dep in self.depends.items():
            for d in dep:
                if status[d] == 'on':
                    print("on %s !!!" % d)
                    if status[dep_name] == 'ban':
                        status[dep_name] = self.get_button_status_onoff(dep_name)
                    print(status[dep_name])
                    break
            else:
                status[dep_name] = 'ban'
        self.draw_buttons(status)
        self.set_state(status)


    
    def button_callback(self, event):
        status = self.states[event.widget['bg']]
        name = event.widget['text']
        if event.widget['state'] == 'disabled':
            print("disabled")
            return
        self.update_buttons(name, status)

        


s = Simulator()
s.run()