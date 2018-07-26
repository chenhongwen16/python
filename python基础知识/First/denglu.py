#/usr/local/bin/env python3
#coding:utf-8

user= [['mm','123'],['tt','456'],['MM','789']]
count = 0
error_count = 0

while count < 3:
    user_name = input("请输入用户名：").strip()
    pass_word = input("请输入密码：").strip()

    f = open(file = "localfile.txt",mode ='r',encoding="utf-8")
    data = f.read()
    if user_name in data:
        print("对不起！用户%s被锁定！请使用其他用户名登录！" % user_name)
    else:
        for i,v in enumerate(user):
            if user_name == v[0] and pass_word == v[1]:
                print("欢迎登录！")
                # count = 3
                exit()
            else:
                f = open(file = "localfile.txt",mode ='a+',encoding="utf-8")
                error_count += 1
                if error_count == 9:
                    f.write("%s状态：锁定" % user_name)
        print("您的用户名密码输入有误！")
    count += 1
    f.close()