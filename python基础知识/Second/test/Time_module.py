#!/usr/bin/env python3
#coding:utf-8

'''
1.在Python中，通常有这几种方式来表示时间：1）时间戳 2）格式化的时间字符串 3）元组（struct_time）共九个元素。由于Python的time模块实现主要调用C库，所以各个平台可能有所不同。
2.UTC（Coordinated Universal Time，世界协调时）亦即格林威治天文时间，世界标准时间。在中国为UTC+8。DST（Daylight Saving Time）即夏令时。
3.时间戳（timestamp）的方式：通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。我们运行“type(time.time())”，返回的是float类型。返回时间戳方式的函数主要有time()，clock()等。
4.元组（struct_time）方式：struct_time元组共有9个元素，返回struct_time的函数主要有gmtime()，localtime()，strptime()。下面列出这种方式元组中的几个元素：
索引（Index）	属性（Attribute）	值（Values）
0	tm_year（年）	比如2011
1	tm_mon（月）	1 - 12
2	tm_mday（日）	1 - 31
3	tm_hour（时）	0 - 23
4	tm_min（分）	0 - 59
5	tm_sec（秒）	0 - 61
6	tm_wday（weekday）	0 - 6（0表示周日）
7	tm_yday（一年中的第几天）	1 - 366
8	tm_isdst（是否是夏令时）	默认为-1

接着介绍time模块中常用的几个函数：
1）time.localtime([secs])：将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。
复制代码 代码如下:

>>> time.localtime()
time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=14, tm_min=14, tm_sec=50, tm_wday=3, tm_yday=125, tm_isdst=0)
>>> time.localtime(1304575584.1361799)
time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=14, tm_min=6, tm_sec=24, tm_wday=3, tm_yday=125, tm_isdst=0)

2）time.gmtime([secs])：和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time。
复制代码 代码如下:

>>>time.gmtime()
time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=6, tm_min=19, tm_sec=48, tm_wday=3, tm_yday=125, tm_isdst=0)

3）time.time()：返回当前时间的时间戳。
复制代码 代码如下:

>>> time.time()
1304575584.1361799

4）time.mktime(t)：将一个struct_time转化为时间戳。
复制代码 代码如下:

>>> time.mktime(time.localtime())
1304576839.0

5）time.sleep(secs)：线程推迟指定的时间运行。单位为秒。
6）time.clock()：这个需要注意，在不同的系统上含义不同。在UNIX系统上，它返回的是“进程时间”，它是用秒表示的浮点数（时间戳）。而在WINDOWS中，第一次调用，返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行时间。（实际上是以WIN32上QueryPerformanceCounter()为基础，它比毫秒表示更为精确）
复制代码 代码如下:

import time
if __name__ == '__main__':
    time.sleep(1)
    print "clock1:%s" % time.clock()
    time.sleep(1)
    print "clock2:%s" % time.clock()
    time.sleep(1)
    print "clock3:%s" % time.clock()

运行结果：
clock1:3.35238137808e-006
clock2:1.00004944763
clock3:2.00012040636
其中第一个clock()输出的是程序运行时间
第二、三个clock()输出的都是与第一个clock的时间间隔
7）time.asctime([t])：把一个表示时间的元组或者struct_time表示为这种形式：'Sun Jun 20 23:21:05 1993'。如果没有参数，将会将time.localtime()作为参数传入。
复制代码 代码如下:

>>> time.asctime()
'Thu May 5 14:55:43 2011'

8）time.ctime([secs])：把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。如果参数未给或者为None的时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))。
复制代码 代码如下:

>>> time.ctime()
'Thu May 5 14:58:09 2011'
>>> time.ctime(time.time())
'Thu May 5 14:58:39 2011'
>>> time.ctime(1304579615)
'Thu May 5 15:13:35 2011'

9）time.strftime(format[, t])：把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传入time.localtime()。如果元组中任何一个元素越界，ValueError的错误将会被抛出。
格式	含义	备注
%a	本地（locale）简化星期名称
%A	本地完整星期名称
%b	本地简化月份名称
%B	本地完整月份名称
%c	本地相应的日期和时间表示
%d	一个月中的第几天（01 - 31）
%H	一天中的第几个小时（24小时制，00 - 23）
%I	第几个小时（12小时制，01 - 12）
%j	一年中的第几天（001 - 366）
%m	月份（01 - 12）
%M	分钟数（00 - 59）
%p	本地am或者pm的相应符	一
%S	秒（01 - 61）	二
%U	一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。	三
%w	一个星期中的第几天（0 - 6，0是星期天）	三
%W	和%U基本相同，不同的是%W以星期一为一个星期的开始。
%x	本地相应日期
%X	本地相应时间
%y	去掉世纪的年份（00 - 99）
%Y	完整的年份
%Z	时区的名字（如果不存在为空字符）
%%	‘%'字符
备注：
“%p”只有与“%I”配合使用才有效果。
文档中强调确实是0 - 61，而不是59，闰年秒占两秒（汗一个）。
当使用strptime()函数时，只有当在这年中的周数和天数被确定的时候%U和%W才会被计算。
举个例子：
复制代码 代码如下:

>>> time.strftime("%Y-%m-%d %X", time.localtime())
'2011-05-05 16:37:06'
10）time.strptime(string[, format])：把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。
复制代码 代码如下:

>>> time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X')
time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=16, tm_min=37, tm_sec=6, tm_wday=3, tm_yday=125, tm_isdst=-1)

在这个函数中，format默认为："%a %b %d %H:%M:%S %Y"。
最后，我们来对time模块进行一个总结。根据之前描述，在Python中共有三种表达方式：1）timestamp 2）tuple或者struct_time 3）格式化字符串。
'''

