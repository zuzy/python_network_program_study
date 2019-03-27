#!/usr/bin/python3

# -*- coding: utf-8 -*-

import re, os, sys, pygame, eyed3, json, threading
import time, wave
from pygame import mixer
# from hope_regist import *

loop = {
    'none':-1,
    'once':0,
    'sequence':4,
    'repeat_one':3,
    'repeat_all':2,
    'random':1,
}

status = {
    'none':3,
    'play':1,
    'pause':0,
    'stop':2,
}

g_lock = threading.Lock()

class Music(threading.Thread):
    unknow = 'unknow'
    api = '/hopeApi/music/initial'
    state = {
        'state':status['none'],
        'loop':loop['once'],
        'pos':-1,
        'vol':0.1,
        'music':{}
    }
    enmixer = False

    def __init__(self, mus_path):
        super().__init__()
        self.path = mus_path
        self.init()
        pygame.init()
        
    def init(self):
        f = os.popen('find %s|sort' % self.path)
        playlist = f.read().split("\n")
        f.close()
        self.playlist = []
        index = 0
        mixer.init()
        self.setvol(self.state['vol'] * 100)
        self.enmixer = True
        for p in playlist:
            p = p.strip()
            m = re.match('.*(mp3|wma|ogg|ape|flac|wav|aif|aac|m4a|ram|amr)$', p, re.I)
            if m is not None:
                self.playlist.append(self._info(p, index))
                index += 1
        # print(json.dumps(self.playlist, ensure_ascii=False, indent=4))

    def _once_next_(self):
        self.stop()

    def _sequence_next_(self):
        mus = self.state['music']
        if type(mus) == str:
            pass
        else:
            if 'musicId' in mus:
                index = mus['musicId'] + 1
                print('index to', index)
                if index >= len(self.playlist):
                    self.stop()
                else:
                    self.play(index=index)
            else:
                raise Exception('play sequence error')
        pass
    
    def _one_next_(self):
        mus = self.state['music']
        if type(mus) == str:
            self.play(path=mus)
        else:
            if 'musicId' in mus:
                print("play ", mus['musicId'])
                self.play(index=mus['musicId'])
            else:
                raise Exception('play repeat one error')
        pass
    
    def _all_next_(self):
        mus = self.state['music']
        if type(mus) == str:
            pass
        else:
            if 'musicId' in mus:
                index = mus['musicId'] + 1
                if index >= len(self.playlist):
                    self.play(index=0)
                else:
                    self.play(index=index)
            else:
                raise Exception('play sequence error')
    
    def _random_next_(self):
        index = int(time.time() * 1000)
        self.play(index=index)

    def _manager_next(self, force=False):
        if force:
            handle = {
                loop['once']:self._all_next_,
                loop['sequence']:self._all_next_,
                loop['repeat_one']:self._all_next_,
                loop['repeat_all']:self._all_next_,
                loop['random']:self._random_next_,
            }
        else:
            handle = {
                loop['once']:self._once_next_,
                loop['sequence']:self._sequence_next_,
                loop['repeat_one']:self._one_next_,
                loop['repeat_all']:self._all_next_,
                loop['random']:self._random_next_,
            }
        lp = self.state['loop']
        print('loop ', lp)
        if lp in handle:
            handle[self.state['loop']]()
        pass
    
    def _manager_status(self):
        st = self.state['state']
        g_lock.acquire()
        busy = mixer.music.get_busy()
        self.state['vol'] = mixer.music.get_volume()
        g_lock.release()
        # print('state vol', self.state['vol'], 'status',st)
        if st == status['none']:
            if busy:
                pos = mixer.music.get_pos()
                if self.state['pos'] == pos:
                    self.state['state'] = status['pause']
                else:
                    self.state['state'] = status['play']
                    self.state['pos'] = pos
                print('1 change to state, ', self.state['state'])
        elif st == status['play']:
            if busy:
                pos = mixer.music.get_pos()
                if self.state['pos'] == pos:
                    self.state['state'] = status['pause']
                    print('2 change to state, ', self.state['state'])
                else:
                    self.state['pos'] = pos
            else:
                self.state['state'] = status['stop']
                print('3 change to state, ', self.state['state'])

        elif st == status['pause']:
            if busy:
                pos = mixer.music.get_pos()
                if self.state['pos'] != pos:
                    self.state['state'] = status['play']
                    self.state['pos'] = pos
                    print('4 change to state, ', self.state['state'])
            else:
                self.state['pos'] = status['stop']
                print('5 change to state, ', self.state['state'])
        else:
            if busy:
                self.state['state'] = status['play']
            else:
                pos = mixer.music.get_pos()
                if pos < 0:
                    self._manager_next()
                    print('6 change to state, ', self.state['state'])

    def run(self):
        # self.init()
        # self.play()
        while True:
            time.sleep(0.25)
            if self.enmixer:
                self._manager_status()
            # else:
            #     self.enmixer = True
            #     mixer.init()

    def name_from_path(self, path):
        return path.split('/')[-1].split('.')[0]

    def _info(self, path, index):
        # audiofile = eyed3.load("song.mp3")
        info = {
            'path':path
        }
        audiofile = eyed3.load(path)
        # print(path)
        info['authorName'] = audiofile.tag.artist or self.unknow
        info['albumName'] = audiofile.tag.album or self.unknow
        info['musicName'] = self.name_from_path(path)
        info['displayName'] = audiofile.tag.title or info['musicName']
        # info['musicTime'] = int(audiofile.info.time_secs * 1000)
        info['musicTime'] = int(audiofile.info.time_secs)
        info['musicSize'] = audiofile.info.size_bytes
        info['musicId'] = index
        info['freq'] = audiofile.info.sample_freq
        print(audiofile.info.time_secs)
        return info
    
    def show_list(self):
        for p in self.playlist:
            print("------%d------\n%s\nduration %d\n" % (p['musicId'], p['musicName'], p['musicTime']))
    
    def info(self, index=None):
        if index == None:
            return self.state
        else:
            return self.playlist[index]


    def play(self, path=None, index=None, name=None):
        
        print(path, index, name)
        if path is None and name is None and index == None :
            if self.state['state'] == status['play']:
                return
            elif self.state['state'] == status['pause']:
                self.resume()
                return
            else:
                index = 0
        
        print('play start here')
        if index != None:
            self.enmixer = False
            length = len(self.playlist) - 1
            if index > length:
                index = index % length
            # print(index, len(self.playlist))
            # print(self.playlist[index]['path'])
            # print('to set frequency', self.playlist[index]['freq'])
            freq = self.playlist[index]['freq']
            g_lock.acquire()
            # if 'freq' not in self.state['music'] or freq != self.state['music']['freq']:
                # mixer.quit()
            mixer.pre_init(frequency=self.playlist[index]['freq'], buffer=self.playlist[index]['musicSize'])
            mixer.music.load(self.playlist[index]['path'])
            g_lock.release()
            self.state['music'] = self.playlist[index]
            print('index is not none')
        elif path is not None:
            audiofile = eyed3.load(path)
            g_lock.acquire()
            # freq = audiofile.info.sample_freq
            # if 'freq' not in self.state['music'] or freq != self.state['music']['freq']:
                # mixer.quit()
                # mixer.pre_init(freq)
            mixer.pre_init(frequency=audiofile.info.sample_freq, buffer=audiofile.info.size_bytes)
            mixer.music.load(path)
            g_lock.release()
            self.state['music'] = {}
            self.state['music']['path'] = path
            self.state['music']['freq'] = freq
        elif name is not None:
            for p in self.playlist:
                if name == p['musicName'] or name == p['displayName']:
                    # freq = p['freq']
                    g_lock.acquire()
                    # if 'freq' not in self.state['music'] or freq != self.state['music']['freq']:
                        # mixer.quit()
                    mixer.pre_init(frequency=p['freq'], buffersize=p['musicSize'])
                    mixer.music.load(p['path'])
                    g_lock.release()
                    self.state['music'] = p
                    break
            else:
                print(name, 'is not in play list')
                return
        # print(" start to play ")
        self.enmixer = True
        time.sleep(0.1)
        g_lock.acquire()
        mixer.music.play()
        print('play && vol to set',self.state['vol'])
        self.setvol(self.state['vol'] * 100)
        g_lock.release()
        print('play end here')
    
    def pause(self):
        g_lock.acquire()
        mixer.music.pause()
        g_lock.release()
    
    def stop(self):
        g_lock.acquire()
        mixer.music.stop()
        g_lock.release()
    
    def resume(self):
        g_lock.acquire()
        mixer.music.unpause()
        g_lock.release()
    
    def next(self):
        self._manager_next(force=True)
        pass
    
    def skip(self, pos):
        # g_lock.acquire()
        # mixer.music.set_pos(float(pos) / 1000)
        # g_lock.release()
        print('cannot skip')

    def setvol(self, vol):
        print('setvol ', vol, vol/100)
        self.state['vol'] = float(vol)/100
        mixer.music.set_volume(self.state['vol'])

    def inc_vol(self):
        vol = self.state['vol'] * 100
        print('inc!!!')
        print(vol)
        vol += 10
        if vol > 100:
            vol = 100
        
        print('incvol', vol)
        self.setvol(vol)

    def dec_vol(self):
        vol = self.state['vol'] * 100
        vol -= 10
        vol = (vol < 0 and 0) or vol
        print('decvol', vol)
        self.setvol(vol)

    def prev(self):
        if self.state['loop'] == loop['none']:
            return
        elif self.state['loop'] == loop['random']:
            self.next()
        else:
            index = self.state['music']['musicId']
            index -= 1
            if index < 0:
                index = len(self.playlist) - 1
            self.play(index=index)
    
    def pos(self, pos):
        pass
    
    def loop_mode(self, mode):
        if mode in loop:
            print('!!!! to set mdoe ', mode)
            self.state['loop'] = loop[mode]
        pass
    

    

if __name__ == '__main__':

    mus = Music(sys.argv[1])
    mus.show_list()
    # mus.play(index=7)
    mus.play(index=0)
    mus.loop_mode('repeat_all')
    # mus.loop_mode('repeat_one')
    # mus.loop_mode('random')
    # mus.play(name='新写的旧歌')
    mus.start()
    # mus.setvol(0)
    time.sleep(1)
    # mus.prev()
    while True:
        # time.sleep(0.5)
        mus.next()
        # time.sleep(1)
        # mus.stop()

 