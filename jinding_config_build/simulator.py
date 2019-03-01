#!/usr/bin/python3
from excel_module import *
from tkinter import *
import json

class Simulator:
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
        self.button_names = Index().buttons
        self.init_state()
        # print(self.button_names)
        
        self.tk = Tk()
        d_state = self.get_state()
        self._init_buttons(d_state)


    def _init_buttons(self, d_state):
        init_colors = {
            'on': 'red',
            'off': 'white',
            'ban': 'gray',
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
        f = open(self.menu + '电源.json', 'r')
        d_init = json.loads(f.read())
        f.close()
        f = open(self.s_path, 'w')
        f.write(json.dumps(d_init['state_off_to_on'], ensure_ascii=False, indent=4))
        f.close()

    def get_state(self):
        f = open(self.s_path, "r")
        d_state = json.loads(f.read())
        f.close()
        return d_state
    
    def set_state(self, state):
        f = open(self.s_path, "w")
        f.write(json.dumps(state))
        f.close()
    
    def get_status(self, name, state):
        f = open(self.menu + name + '.json', 'r')
        d_status = json.loads(f.read())
        f.close()
        '''
        state_on_to_off
        state_off_to_on
        '''
        if state:
            status = d_status['state_on_to_off']
        else:
            status = d_status['state_off_to_on']
        return status
    
    def update_buttons(self, name, state):
        status = self.get_status(name, state)
        print(status)
        for name in self.names:
            print(name)
            print(status[name])
            if status[name] == 'ban':
                self.buttons[name]['state'] = 'disable'
            elif status[name] == 'stay':
                pass
            else:
                self.buttons[name]['bg'] = self.colors[status[name]]
        self.set_state(status)


    
    def button_callback(self, event):
        status = self.states[event.widget['bg']]
        name = event.widget['text']
        self.update_buttons(name, status)

        


s = Simulator()
s.run()