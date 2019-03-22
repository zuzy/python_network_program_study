#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json, sys, os

class Halo_parse:
    CMD = 'cmd'
    PARAMS = 'params'
    CTL = 'control'
    INFO = 'info'
    CONTENT = 'content'
    
    def __init__(self, Mus):
        self.mus = Mus

    def ctrl_playstate(self, state):
        pmap = {
            'play': self.mus.play,
            'pause': self.mus.pause,
            'stop': self.mus.stop,
            'next': self.mus.next,
            'prev': self.mus.prev,
        }
        if state in pmap:
            print('!!!!', state)
            pmap[state]()
        else:
            print(state, 'is illegal')
        
    def ctrl_songid(self, index):
        try:
            index = int(index)
            self.mus.play(index=index)
        except Exception as e:
            print('ctrl songid, ', e)

    def ctrl_volume(self, vol):
        try:
            ivol = int(vol)
            self.mus.setvol(ivol)
        except :
            pmap = {
                'inc': self.mus.inc_vol,
                'dec': self.mus.dec_vol,
            }
            if vol in pmap:
                pmap[vol]()

    def ctrl_mode(self, mode):
        pmap = {
            'random': 'random',
            'single': 'repeat_one',
            'cycle': 'repeat_all',
            'list': 'sequence',
        }
        if mode in pmap:
            print('set mode', mode)
            self.mus.loop_mode(pmap[mode])

    def ctrl_source(self, source):
        print('unsupport source control!', source)

    def parse_control(self, params):
        pmap = {
            'playstate': self.ctrl_playstate,
            'songid': self.ctrl_songid,
            'volume': self.ctrl_volume,
            'mode':self.ctrl_mode,
            'source': self.ctrl_source,
        }
        for k, v in params.items():
            if k in pmap:
                print('cmd:', k, v)
                pmap[k](v)
    
    def parse_speak(self, params):
        print('unsupport voicespeak')

    def parse_oper(self, params):
        print('unsupport voiceoper')

    def parse_specifyplay(self, params):
        if 'songs' not in params:
            print('without songs inside')
            return
        song = params['songs'][0]
        index = int(song['id'])
        self.mus.play(index=index)
    
    def parse_opertunnel(self, params):
        print('unsupport tunnel operation')
    
    def parse_songinfo(self, params):
        if 'songid' in params:
            index = int(params['songid'])
            json.dump(self.mus.info(index=index), sys.stdout, ensure_ascii=False, indent=4)
        else:
            print('error of songid!!')

        pass

    def parse_songlist(self, params):
        self.mus.show_list()
        pass

    def parse_info(self, params):
        json.dump(self.mus.info(), sys.stdout, ensure_ascii=False, indent=4)
        pass

    def parse(self, body):
        if body == None or type(body) != str:
            return

        btab = json.loads(body)
        pmap = {
            'control':self.parse_control,
            'voicespeak': self.parse_speak,
            'voiceoper': self.parse_oper,
            'specifyplay': self.parse_specifyplay,
            'opertunnel': self.parse_opertunnel,
            'querysonginfo': self.parse_songinfo,
            'getsonglist': self.parse_songlist,
            'info': self.parse_info,
        }
        json.dump(btab, sys.stdout, ensure_ascii=False, indent=4)        
        try:
            cmd = btab[self.CMD]
            params = btab[self.PARAMS]
        except Exception as e:
            print('parse body error, ',e)
        pmap[cmd](params)

        

