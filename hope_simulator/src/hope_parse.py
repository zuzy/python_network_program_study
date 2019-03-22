#!/usr/bin/python3
# -*- coding: utf-8 -*-

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

    def ctrl(self, body):
        pass
    
    def event(self, body):
        pass
     
    def plist(self, body):
        pass

    def batchsong(self, body):
        pass
    
    def info(self, body):
        pass

    def specifyplay(self, body):
        pass
    
    def tts(self, body):
        pass
    
    def checkinfo(self, body):
        pass

    def parse(self, cmd, body):
        cmd &= 0x7f
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

    
    
    
    