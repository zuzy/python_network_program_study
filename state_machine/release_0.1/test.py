#!/usr/bin/python3
# coding:utf-8
import os, sys
from build import Build

class R():
    def __init__(self):
        pass
    @staticmethod
    def exit():
        os.system("kill -9 " + str(os.getpid())) #杀掉进程

def main(argv):

    try:
        b = Build().build()
        print(b)
    except Exception as e:
        print('error! ', e)
        R.exit()

if __name__ == "__main__":
    main(sys.argv)