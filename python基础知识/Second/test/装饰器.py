#!/usr/bin/env python3
#coding:utf-8
user_status = False
def login(func):
    def inner():
        user_name = "zch"
        password = "love"
        global user_status
        if user_status == False:
            name = input("user:")
            psd = input("psd:")
            if name == user_name and psd == password:
                print ("welcom login")
                user_status = True
            else:
                print ("wrong name or wrong psd")
        else:
            print ("Already login")
        if user_status:
            func()
    return inner
@login
def sichuan():
    print("四川人爱吃辣")

sichuan()