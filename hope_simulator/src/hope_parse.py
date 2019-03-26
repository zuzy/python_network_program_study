#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

'''
command

#define HOPE_CLI_MAP(XX)    \
    XX(0x01,        common,     _common_cb)         \
    XX(0x02,        heart,      _heart_cb)          \
    XX(0x05,        ctrl,       _ctrl_cb)           \
    XX(0x110,       event,      _event_cb)          \
    XX(0x135,       p_list,     _plist_cb)          \
    XX(0x140,       p_song,     _psongs_cb)         \
    XX(0x205,       info,       _info_cb)           \
    XX(0x235,       sel_list,   _selist_cb)         \
    XX(0x245,       tts_cmd,    _tts_cmd_cb)        \
    XX(0x255,       tts_check,  _tts_check_cb)      \
    XX(0,           nil,        NULL)
'''


'''
enum{
    C_DEV_COMMON = 0X01,
    C_DEV_HEART,
    C_DEV_EXIT,
    C_DEV_IDENTIFY,
    C_DEV_CTRL = 0X10,
    C_DEV_SONGLIST_NEW = 0X20,
    C_DEV_SONGLIST_CREATE = 0X30,
    C_DEV_SONGLIST_RM = 0X40,
    C_DEV_SONGLIST_ADD = 0X50,
    C_DEV_AREA_SCAN = 0X60,
    C_DEV_AREA_CTRL = 0X70,
    C_DEV_SONGLIST_RMSONG = 0X80,
    C_DEV_SCENE_NEW = 0X90,
    C_DEV_SCENE_RULE = 0X100,
    C_DEV_SONGLIST_CHANGE = 0X125,

    C_DEV_SCENE_CTRL = 0X170,
    C_DEV_SCENE_START= 0X175,
    C_DEV_SCENE_RM = 0X185,
    C_DEV_AREA_VOL = 0X195,

    C_DEV_UNBIND = 0X215,
    
    C_DEV_EVENT = 0X230,

    C_DEV_TTS = 0X250,
    C_DEV_TTS_CHECK = 0X260,
};
'''
hope_cmap = {
    0x01
}

class Hope_parse():

    def __init__(self, Mus):
        self.mus = Mus
    
    def common_reply(self, body):
        print('common reply')
        pass
    
    def heart_reply(self, body):
        print('heartbeat reply')
        pass

    def _ctrl_status(self, val):
        print('status, ', val)
        v = int(val)
        if v == 0:
            self.mus.pause()
        elif v == 1:
            self.mus.play()
        else:
            self.mus.stop()
        pass

    def _ctrl_play(self, val):
        print('play', val)
        self.mus.play(index=int(val))
        pass

    def _ctrl_music(self, val):
        print('music', val)
        self.mus.play(name=val)
        pass

    def _ctrl_cata(self, val):
        print('cata', val)
        pass
    
    def _ctrl_bell(self, val):
        print('bell contorl', val)
        pass

    def _ctrl_control(self, val):
        v = int(val)
        if v == 0:
            print('prev')
            self.mus.prev()
        elif v == 1:
            print('next')
            self.mus.next()
        else:
            print('no support control', val)
        pass

    def _ctrl_skip(self, val):
        print('skip to', val)
        self.mus.skip(int(val))
        pass

    def _ctrl_idvol(self, val):
        val = int(val)
        print('contorl volume', val)
        if val == 0:
            self.mus.dec_vol()
        else:
            self.mus.inc_vol()
        pass
    
    def _ctrl_mute(self, val):
        self.mus.setvol(0)
        print('mute!', val)
        pass
    
    def _ctrl_setvol(self, val):
        # vol = float(val) * 100
        vol = int(val)
        print('control vol', val, vol)
        self.mus.setvol(int(vol))
        pass
    
    def _ctrl_source(self, val):
        print('no support source control', val)
        pass

    def _ctrl_effect(self, val):
        print('no support effect control', val)
        pass
    
    def _ctrl_model(self, val):
        model = {
            1:'random',
            2:'repeat_all',
            3:'repeat_one',
            4:'sequence',
        }
        v = int(val)
        if v in model:
            self.mus.loop_mode(model[v])
            print('loop', v, model[v])
        pass
    
    def _ctrl_locale(self, val):
        print('locale', val)
        pass

    def ctrl(self, body):
        print('common ctrl!')
        cmd_tab = json.loads(body)
        ctrl_dict = {
            'status':self._ctrl_status,
            'play':self._ctrl_play,
            'music':self._ctrl_music,
            'cata':self._ctrl_cata,
            'bell':self._ctrl_bell,
            'control':self._ctrl_control,
            'skip':self._ctrl_skip,
            'idvol':self._ctrl_idvol,
            'mute':self._ctrl_mute,
            'setvol':self._ctrl_setvol,
            'source':self._ctrl_source,
            'effect':self._ctrl_effect,
            'model':self._ctrl_model,
            'locale':self._ctrl_locale,
        }
        print(json.dumps(cmd_tab), 'parse!!!')
        if 'profile' in cmd_tab:
            profile = cmd_tab['profile']
            print('profile', json.dumps(profile))
            for k, v in ctrl_dict.items():
                if k in profile:
                    v(profile[k])
        pass
    
    def event(self, body):
        cmd = json.loads(body)
        if 'content' not in cmd:
            print('event error without content', body)
        content = cmd['content']
        tokenid = content['tokenId']
        print('get token id ', tokenid)
            
        pass
     
    def plist(self, body):
        cmd = json.loads(body)
        # print('plist\n', json.dumps(cmd, ensure_ascii=False, indent=4))
        if 'musId' in cmd:
            index = int(cmd['musId'])
            self.mus.play(index=index)
        pass

    def batchsong(self, body):
        cmd = json.loads(body)
        print('batch song ctontrol, ', body)
        pass
    
    def info(self, body):
        print('check up info')
        pass

    def specifyplay(self, body):
        print('specify play', body)
        cmd = json.loads(body)
        if 'musIds' not in body:
            print('specify play illegal')
            return
        musIds = cmd['musIds']
        index = musIds.split(',')[0]
        self.mus.play(index=int(index))
        pass
    
    def tts(self, body):
        print('unsupport tts ctrl', body)
        pass
    
    def checkinfo(self, body):
        print('unsupport, tts check info')
        pass

    def parse(self, cmd, body):
        cmd &= 0x7fff
        mmap = {
            0x01:   self.common_reply,
            0x02:   self.heart_reply,
            0x05:   self.ctrl,
            0x110:  self.event,
            0x135:  self.plist,
            0x140:  self.batchsong,
            0x205:  self.info,
            0x235:  self.specifyplay,
            0x245:  self.tts,
            0x255:  self.checkinfo,
        }
        
        if cmd in mmap:
            print('parse, ', cmd)
            mmap[cmd](body)

    
    
    
    