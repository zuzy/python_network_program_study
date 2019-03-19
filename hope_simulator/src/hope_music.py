#!/usr/bin/python3

# -*- coding: utf-8 -*-

import re, os, sys, pygame, eyed3, json, threading
import time
from pygame import mixer
# from hope_regist import *

loop = {
    'once':0,
    'sequence':1,
    'repeat_one':2,
    'repeat_all':3,
    'random':4,
}

status = {
    'play':0,
    'pause':1,
    'stop':2,
}

g_lock = threading.Lock()

class Music(threading.Thread):
    unknow = 'unknow'
    api = '/hopeApi/music/initial'
    state = {
        'state':status['stop'],
        'loop':loop['once'],
        'pos':-1,
        'music':{}
    }
    def __init__(self, mus_path):
        super().__init__()
        self.path = mus_path
        f = os.popen('find %s|sort' % self.path)
        playlist = f.read().split("\n")
        self.playlist = []
        index = 0
        mixer.init()
        for p in playlist:
            p = p.strip()
            m = re.match('.*(mp3|wma|ogg|ape|flac|wav|aif|aac|m4a|ram|amr)$', p, re.I)
            if m is not None:
                self.playlist.append(self.info(p, index))
                index += 1
        # print(json.dumps(self.playlist, ensure_ascii=False, indent=4))

    def run(self):
        # self.play()
        while True:
            time.sleep(0.25)
            if mixer.music.get_busy():
                pos = mixer.music.get_pos()
                if pos != self.state['pos']:
                    st = status['play']
                    self.state['pos'] = mixer.music.get_pos()
                else:
                    st = status['pause']
            else:
                st = status['stop']
            if st != self.state['state']:
                print('state changed %d' % st)
                self.state['state'] = st
            # print('busy ', mixer.music.get_busy())
            # print('pos ', mixer.music.get_pos())

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
        info['musicId'] = index
        # print(audiofile.info.time_secs)
        return info
    
    def show_list(self):
        for p in self.playlist:
            print("------%d------\n%s\nduration %d\n" % (p['musicId'], p['musicName'], p['musicTime']))

    def play(self, path=None, index=0, name=None):
        if path is None and name is None :
            length = len(self.playlist) - 1
            if index > length:
                index = index % length
            print(index, len(self.playlist))
            g_lock.acquire()
            mixer.music.load(self.playlist[index]['path'])
            g_lock.release()
        elif path is not None:
            g_lock.acquire()
            mixer.music.load(path)
            g_lock.release()
        elif name is not None:
            for p in self.playlist:
                if name == p['musicName'] or name == p['displayName']:
                    g_lock.acquire()
                    mixer.music.load(p['path'])
                    g_lock.release()
                    break
        # print(" start to play ")
        time.sleep(0.2)
        g_lock.acquire()
        mixer.music.play()
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
    

    

if __name__ == '__main__':
    mus = Music(sys.argv[1])
    mus.show_list()
    mus.play(index=7)
    # mus.play(name='新写的旧歌')
    

    mus.start()
    while True:
        time.sleep(5)
        mus.pause()
        time.sleep(2)
        mus.resume()
        time.sleep(5)
        mus.stop()
        time.sleep(5)
        mus.resume()
    # mus.update()
    # for p in mus.playlist:
    #     mus.info(p)
    # mus.info('')