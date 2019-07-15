#!/usr/bin/python3
#coding: utf-8

import json

CMD = 'cmd'
COMMENT = 'comment'
PARAMS = 'params'
ARGNUM = 'argnum'

halo_cmd_tunnel = {
    'tunnel': {
        ARGNUM:3,
        CMD:json.dumps({CMD:'control',PARAMS:{ 'tunnels': { 'id':'%d', 'enable': '%s'}}}),
        COMMENT:'tunnel\n\tchange the tunnel of dev\n\tsource:[num]:[y/n]'
    },
}

halo_cmd_bool = {
    'power':{
        ARGNUM:2,
        CMD:'poweroper',
        PARAMS:'value',
        # CMD:json.dumps({CMD:'poweroper',PARAMS:{'value':'%s'}}),
        COMMENT:'power\n\tpower operation\n\tpower: [y/n]'
    },
    'mute': {
        ARGNUM:2,
        CMD:'control',
        PARAMS:'mute',
        # CMD:json.dumps({CMD:'control',PARAMS:{'mute':'%s'}}),
        COMMENT:'mute\n\tset the dev mute\n\tmute: [y/n]'
    },
}
halo_cmd = {
    'info': {
        ARGNUM:1,
        CMD: json.dumps({CMD:'info',PARAMS:{'getinfo':True}}),
        COMMENT:'info\n\tget the device info'
    },
    'songlist': {
        ARGNUM:2,
        CMD:json.dumps({CMD:'getsonglist',PARAMS:{'pageindex':'%s'}}),
        COMMENT:'songlist\n\tget the song list\n\tsonglist: [page_index]'
    },
    'querysong': {
        ARGNUM:2,
        CMD:json.dumps({CMD:'querysonginfo',PARAMS:{'songid':'%s'}}),
        COMMENT:'querysong\n\tquery the info of a song\n\tquerysong: song_index'
    },
    'exit': {
        ARGNUM:2,
        CMD:json.dumps({CMD:'exit',PARAMS:{'deviceid':'%s'}}),
        COMMENT:'exit\n\texit from the connection'
    },
    'opertunnel': {
        ARGNUM:1,
        CMD:'',
        COMMENT:'opertunnel\n\ttunnel operation, not support for now'
    },
    'specify': {
        ARGNUM:2,
        CMD:json.dumps({CMD:'specifyplay',PARAMS:{'songs':[{'id':'%s', 'type':0}]}}),
        COMMENT:'specify\n\tspecify play a local music\n\tspecify: index'
    },
    'dev_info':{
        ARGNUM:1,
        CMD:json.dumps({CMD:'deviceinfo',PARAMS:{}}),
        COMMENT:'dev_info\n\tget the device info'
    },
    'voice_oper':{
        ARGNUM:2,
        CMD:json.dumps({CMD:'voiceoper',PARAMS:{'content':'%s'}}),
        COMMENT:'voice_oper\n\tvoice operation, search musics online or control the smart devs\n\tvoice_oper: cmd_string'
    },
    'voice_speak':{
        ARGNUM:2,
        CMD:json.dumps({CMD:'voicespeak',PARAMS:{'content':'%s'}}),
        COMMENT:'voice_speak\n\tvoice speak\n\tvoice_speak: speaking_string'
    },

    'pause': {
        ARGNUM:1,
        CMD:json.dumps({CMD:'control',PARAMS:{'playstate':'pause'}}),
        COMMENT:'pause\n\tpause the music'
    },
    'play': {
        ARGNUM:1,
        CMD:json.dumps({CMD:'control',PARAMS:{'playstate':'play'}}),
        COMMENT:'start\n\tstart the loacal music'
    },
    'next': {
        ARGNUM:1,
        CMD:json.dumps({CMD:'control',PARAMS:{'playstate':'next'}}),
        COMMENT:'start\n\tstart the loacal music'
    },
    'prev': {
        ARGNUM:1,
        CMD:json.dumps({CMD:'control',PARAMS:{'playstate':'prev'}}),
        COMMENT:'start\n\tstart the loacal music'
    },
    'index': {
        ARGNUM:2,
        CMD:json.dumps({CMD:'control',PARAMS:{'songid':'%s'}}),
        COMMENT: 'index\n\tjump to the index of music\n\tindex: [number]'
    },
    'vol':{
        ARGNUM:2,
        CMD:json.dumps({CMD:'control',PARAMS:{'volume':'%s'}}),
        COMMENT:'vol\n\tcontrol the volume of dev\n\tvol:[num/inc/dec]'
    },
    'mode':{
        ARGNUM:2,
        CMD:json.dumps({CMD:'control',PARAMS:{'volume':'%s'}}),
        COMMENT:'mode\n\tthe repeation of music player\n\tmode:[random/single/cycle/list]'
    },
    'source': {
        ARGNUM:2,
        CMD:json.dumps({CMD:'control',PARAMS:{'source':'%s'}}),
        COMMENT:'source\n\tchange the source of dev\n\tsource:[local/bluetooth/linein]'
    },

}

def help(cmd_list):
    if len(cmd_list) == 1 or len(cmd_list[1]) < 1:
        print('All the cmd:')
        l = []
        for cmd in halo_cmd:
            l.append(cmd)
        for cmd in halo_cmd_bool:
            l.append(cmd)
        l.sort()
        for cmd in l:
            print('\t', cmd)
    else:
        cmd = cmd_list[1]
        cmd = cmd.strip()

        if cmd in halo_cmd:
            print(halo_cmd[cmd][COMMENT])
        elif cmd in halo_cmd_bool:
            print(halo_cmd_bool[cmd][COMMENT])
        elif cmd in halo_cmd_tunnel:
            print(halo_cmd_tunnel[cmd][COMMENT])
        else:
            print('cmd[%s] is not support' % cmd)
    return None

def parse_str(cmd_list, data):
    try:
        length = len(cmd_list)
        cmd = cmd_list[0]
        if length != halo_cmd[cmd][ARGNUM]:
            raise Exception('cmd[%s] is illeagal\n%s' %(data, halo_cmd[cmd][COMMENT]))
        if length == 1:
            return halo_cmd[cmd][CMD] + '\n'
        else:
            arg = cmd_list[1].strip()
            return (halo_cmd[cmd][CMD] % arg) + '\n'

    except Exception as e:
        print(e)
        return None

def parse_bool(cmd_list, data):
    try:
        length = len(cmd_list)
        cmd = cmd_list[0]
        if length != halo_cmd_bool[cmd][ARGNUM]:
            raise Exception('cmd[%s] is illeagal\n%s' %(data, halo_cmd[cmd][COMMENT]))

        arg = cmd_list[1].strip()
        if len(arg):
            b = False
            if arg == 'y' or arg == 'Y':
                b = True
            elif arg == 'n' or arg == 'N':
                b = False
            else:
                raise Exception('cmd[%s] is illeagal\n%s' %(data, halo_cmd[cmd][COMMENT]))
            return json.dumps({CMD:halo_cmd_bool[cmd][CMD], PARAMS:{halo_cmd_bool[cmd][PARAMS]:b}}) + '\n'
        else:
            raise Exception('cmd[%s] is illeagal\n%s' %(cmd, halo_cmd[cmd][COMMENT]))
    except Exception as e:
        print(e)
        return None

def parse_tunnel(cmd_list, data) :
    try:
        length = len(cmd_list)
        print(cmd_list)
        cmd = cmd_list[0]
        if length != halo_cmd_tunnel[cmd][ARGNUM]:
            raise Exception('cmd[%s] is illeagal\n%s' %(data, halo_cmd[cmd][COMMENT]))
        
        arg1 = int(cmd_list[1].strip())
        arg2 = cmd_list[2].strip()
        print(arg2)
        b = False
        if arg2 == 'y' or arg2 == 'Y':
            b = True
        elif arg2 == 'n' or arg2 == 'N':
            b = False
        else:
            raise Exception("tunnel is illegal\n")
        print('111231', arg1, arg2, b)
        return json.dumps({CMD:'control', PARAMS:{'tunnels': [{'id':arg1, 'enable':b},]}}) + '\n'
    except Exception as e:
        print(e)
        return None


def parse_cmd(data):
    # data = str(data).encode()
    try:
        cmd_list = data.split(':')
        cmd = cmd_list[0]
        if cmd == 'help':
            return help(cmd_list)
        
        if cmd in halo_cmd :
            return parse_str(cmd_list, data)
        elif cmd in halo_cmd_bool:
            return parse_bool(cmd_list, data)
        elif cmd in halo_cmd_tunnel:
            print("parse tunnel!")
            return parse_tunnel(cmd_list, data)
        else:
            raise Exception('cmd[%s] is not support' % data)


        
        if not cmd in halo_cmd and not cmd in halo_cmd_bool:
        # if not cmd in halo_cmd :
            print(cmd)
            raise Exception('cmd[%s] is not support' % data)


        # if length != halo_cmd[cmd][ARGNUM]:
        #     raise Exception('cmd[%s] is illeagal\n%s' %(data, halo_cmd[cmd][COMMENT]))
        # if length == 1:
        #     return halo_cmd[cmd][CMD] + '\n'
        # else:
        #     arg = cmd_list[1].strip()
        #     if len(arg):
        #         if halo_cmd_bool[cmd]:
        #             if arg == 'y':
        #                 return json.dumps({CMD:halo_cmd_bool[cmd][CMD], PARAMS:{halo_cmd_bool[cmd][PARAMS]:True}}) + '\n'
        #             elif arg == 'n':
        #                 return json.dumps({CMD:halo_cmd_bool[cmd][CMD], PARAMS:{halo_cmd_bool[cmd][PARAMS]:False}}) + '\n'
        #             else:
        #                 raise Exception('cmd[%s] is illeagal\n%s' %(data, halo_cmd[cmd][COMMENT]))
        #         else:
        #             return (halo_cmd[cmd][CMD] % arg) + '\n'
        #     else:
        #         raise Exception('cmd[%s] is illeagal\n%s' %(data, halo_cmd[cmd][COMMENT]))
        
    except Exception as e:
        print(e)
        return None

