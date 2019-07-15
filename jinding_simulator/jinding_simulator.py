#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, serial

class UART:
    def __init__(self, tty_name):
        self.ser = serial.Serial()
        self.ser.port = tty_name
        
        self.ser.open()
        self.ser.flushInput()
        self.ser.flushOutput()

        self.addr = None
        self.setAddress(0)

    def setConf(self):
        self.ser.baudrate = 9600
        self.ser.bytesize = serial.EIGHTBITS