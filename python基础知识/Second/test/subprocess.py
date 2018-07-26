#!/usr/bin/env python3
#coding:utf-8

'''
>>> import os
>>> a = os.system('df -h')
Filesystem      Size   Used  Avail Capacity iused               ifree %iused  Mounted on
/dev/disk1s1   233Gi   36Gi  194Gi    16%  814622 9223372036853961185    0%   /
devfs          191Ki  191Ki    0Bi   100%     662                   0  100%   /dev
/dev/disk1s4   233Gi  3.0Gi  194Gi     2%       3 9223372036854775804    0%   /private/var/vm
map -hosts       0Bi    0Bi    0Bi   100%       0                   0  100%   /net
map auto_home    0Bi    0Bi    0Bi   100%       0                   0  100%   /home
/dev/disk2s1    30Mi   15Mi   15Mi    51%     542          4294966737    0%   /Volumes/网易云音乐
>>> a
0
>>> os.popen('df -h')
<os._wrap_close object at 0x103a11198>
>>> f =os.popen('df -h')
>>> f.read()
'Filesystem      Size   Used  Avail Capacity iused               ifree %iused  Mounted on\n/dev/disk1s1   233Gi   36Gi  194Gi    16%  814622 9223372036853961185    0%   /\ndevfs          191Ki  191Ki    0Bi   100%     662                   0  100%   /dev\n/dev/disk1s4   233Gi  3.0Gi  194Gi     2%       3 9223372036854775804    0%   /private/var/vm\nmap -hosts       0Bi    0Bi    0Bi   100%       0                   0  100%   /net\nmap auto_home    0Bi    0Bi    0Bi   100%       0                   0  100%   /home\n/dev/disk2s1    30Mi   15Mi   15Mi    51%     542          4294966737    0%   /Volumes/网易云音乐\n'



PIPE 管道
'''


# terminate() 只是发送了信号
# kill()

import subprocess


subprocess.run(['df', '-h'], stderr=subprocess.PIPE, stout=subprocess.PIPE, check=True)
#check=True shell=True


# run和Popen的区别  run：主程序停滞 Popen：主程序不停止，通过poll不停的拿结果

