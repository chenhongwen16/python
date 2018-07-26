#!/usr/bin/env python3
#coding:utf-8

#输入用户密码，正确后登陆系统，打印
#1、修改个人信息
#2、打印个人信息
#3、修改密码
#每个选项写一个方法
#登陆时输出3次退出


'''
登陆，三次登陆不成功就自动退出程序。
'''

person_info = "./account_info.txt"
f = open(person_info,"r+")
raw_data = f.readlines()
accounts = {}

menu = '''
1.修改个人信息
2.打印个人信息
3.修改密码
'''
count = 0

while count < 3:
    user_name = input("请输入用户名:").strip()
    user_password = input("请输入用户密码:").strip()
    if user_name in accounts:
        if user_password == accounts[user_name][1]:
            while True:
                print menu
                user_choice = input("请输入你选择的序号>>")
                if user_choice.isdigit():
                    user_choice = int(user_choice)
                    if user_choice == 1:
                        change_person_info()
                    elif user_choice == 2:
                        print_info()
                    elif user_choice == 3:
                        change_password()
                else:
                    pass




def change_person_info():
    pass

def print_info():
    pass

def change_password():
    pass
