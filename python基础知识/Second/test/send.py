#!/usr/bin/env python3
#coding:utf-8

def range2(n):
    count = 0
    while count < n:
        print ("count:",count)
        count += 1
        sign = yield count
        print ("----sign",sign)

new_range = range2(3)

n1 = next(new_range)

print('do sth else ...')
new_range.send("stop")


'''
next
    唤醒生成器并继续执行
send("stop")
1. 唤醒并继续执行
2. 发送一个信息到生成器内部
next发送了一个none
send可以发送别的
'''
