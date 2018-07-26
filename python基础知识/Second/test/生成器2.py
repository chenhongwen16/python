#!/usr/bin/env python3
#coding:utf-8

def range2(n):

    count = 0
    while count < n:
        print ("count:",count)
        count += 1
        yield count #return  导致程序卡在这里了  yield


new_range=range2(10)
r1=next(new_range)
print(r1)
r2=next(new_range)
print(r2)

new_range.__next__()



# for i in range2:
#     print (i)
'''
yield vs return
return  返回并终止function
yield   返回数据，并冻结当前的执行过程
next 唤醒冻结的函数执行过程，继续执行，知道遇到下一个yield
'''

'''
10个G的文件 边读边返回
yield相当于一个暂停的意思
'''
'''
函数有了yield之后
 1、函数名加()就得到了一个生成器
 2、return 在生成器里，代表生成器的中止，直接报错
 
 //在一个函数中如果已经有了yield  如果还有return  这个return是不会执行的
'''
