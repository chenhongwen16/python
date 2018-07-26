#/usr/bin/env python
#coding:utf-8

age = 26


n = 0
while(n<3):
    n += 1
    user_gusee = int(input("your guess:"))
    if user_gusee == 26:
        print "Yes!"
        break
    else:
        print "No"