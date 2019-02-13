#!/usr/bin/python3
# coding: utf-8
import psutil
info = psutil.net_io_counters()
print(info)
print('bytes_sent = ', info.bytes_sent)