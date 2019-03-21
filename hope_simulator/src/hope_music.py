#!/usr/bin/python3

# -*- coding: utf-8 -*-

import re, os, sys, pygame, eyed3, json, threading
import time, wave
from pygame import mixer
# from hope_regist import *

loop = {
    'none':-1,
    'once':0,
    'sequence':1,
    'repeat_one':2,
    'repeat_all':3,
    'random':4,
}

status = {
    'none':-1,
    'play':0,
    'pause':1,
    'stop':2,
}

g_lock = threading.Lock()

class Music(threading.Thread):
    unknow = 'unknow'
    api = '/hopeApi/music/initial'
    state = {
        'state':status['none'],
        'loop':loop['none'],
        'pos':-1,
        'vol':50,
        'music':{}
    }
    enmixer = False

    def __init__(self, mus_path):
        super().__init__()
        self.path = mus_path
        self.init()
        
    def init(self):
        f = os.popen('find %s|sort' % self.path)
        playlist = f.read().split("\n")
        f.close()
        self.playlist = []
        index = 0
        mixer.init()
        self.enmixer = True
        for p in playlist:
            p = p.strip()
            m = re.match('.*(mp3|wma|ogg|ape|flac|wav|aif|aac|m4a|ram|amr)$', p, re.I)
            if m is not None:
                self.playlist.append(self.info(p, index))
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
        busy = mixer.music.get_busy()
        self.state['vol'] = int(mixer.music.get_volume() * 100)
        print('state vol', self.state['vol'])
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
            time.sleep(0.5)
            if self.enmixer:
                self._manager_status()
            # else:
            #     self.enmixer = True
            #     mixer.init()

    def update(self, auth, ref):
        pass

    def name_from_path(self, path):
        return path.split('/')[-1].split('.')[0]

    def info(self, path, index):
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
        info['musicTime'] = int(audiofile.info.time_secs * 1000)
        info['musicSize'] = audiofile.info.size_bytes
        info['musicId'] = index
        info['freq'] = audiofile.info.sample_freq
        # print(audiofile.info.time_secs)
        return info
    
    def show_list(self):
        for p in self.playlist:
            print("------%d------\n%s\nduration %d\n" % (p['musicId'], p['musicName'], p['musicTime']))

    def play(self, path=None, index=0, name=None):
    
        mixer.quit()
        self.enmixer = False
        print(path, index, name)
        if path is None and name is None :
            length = len(self.playlist) - 1
            if index > length:
                index = index % length
            print(index, len(self.playlist))
            print(self.playlist[index]['path'])
            print('to set frequency', self.playlist[index]['freq'])
            g_lock.acquire()
            mixer.init(frequency=self.playlist[index]['freq'])
            mixer.music.load(self.playlist[index]['path'])
            self.state['music'] = self.playlist[index]
            g_lock.release()
        elif path is not None:
            audiofile = eyed3.load(path)
            g_lock.acquire()
            mixer.init(frequency=audiofile.info.sample_freq) 
            mixer.music.load(path)
            self.state['music'] = path
            g_lock.release()
        elif name is not None:
            for p in self.playlist:
                if name == p['musicName'] or name == p['displayName']:
                    g_lock.acquire()
                    mixer.init(frequency=p['freq'])             
                    mixer.music.load(p['path'])
                    self.state['music'] = p
                    g_lock.release()
                    break
        # print(" start to play ")
        self.enmixer = True
        g_lock.acquire()
        mixer.music.play()
        self.setvol(self.state['vol'])
        g_lock.release()
    
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
        self._manager_next(True)
        pass

    def setvol(self, vol):
        print('setvol ', vol, vol/100)
        self.state['vol'] = vol
        mixer.music.set_volume(float(vol)/100)

    def inc_vol(self):
        vol = self.state['vol']
        print('inc!!!')
        print(vol)
        vol += 10
        if vol > 100:
            vol = 100
        
        print('incvol', vol)
        self.setvol(vol)

    def dec_vol(self):
        vol = self.state['vol']
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
            self.state['loop'] = loop[mode]
        pass
    

    

if __name__ == '__main__':
    if True:
        mus = Music(sys.argv[1])
        mus.show_list()
        # mus.play(index=7)
        mus.play(index=1)
        mus.loop_mode('repeat_all')
        # mus.play(name='新写的旧歌')
        mus.start()
        # mus.setvol(0)
    else:
        mixer.init()
        mixer.music.load(sys.argv[1])
        mixer.music.play()
    time.sleep(5)
    # mus.next()
    while True:
        # mus.dec_vol()
        # mus.inc_vol()
        # mus.setvol(10)
        mus.prev()
        time.sleep(5)
        # mus.setvol(100)
        # time.sleep(5)
        # mus.stop()
        # mus.next()
        # time.sleep(2)
        # mus.resume()
        # time.sleep(5)
        # mus.stop()
        # time.sleep(5)
        # mus.pause()
        # mus.resume()
    # mus.update()
    # for p in mus.playlist:
    #     mus.info(p)
    # mus.info('')