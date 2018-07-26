#!/usr/bin/env python3
#coding:utf-8

import time

def func():
    starttime = time.time()

    print("hello")
    time.sleep(1)
    print("world")
    endtime = time.time()
    mesecs = (endtime - starttime)*1000

    print("time is %d ms"%mesecs)


func()