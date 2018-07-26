# 把内存数据转成字符,叫序列化
# 把字符转成内存数据类型,叫反序列化eval
# pickle
# json
# 只是把数据类型转成字符串存在内存里的意义？
# json.dump  json.loads
# 1.把你的内存数据通过网络共享给远程的其他人
# 2.定义了不同语言之间的交互规则
#   1.纯文本，坏处，不能共享复杂的数据类型
#   2.xml,坏处  占用空间大
#   3.json 简单 可读性好
'''
json
    str int tuple list dict
pickle
    支持python里的所有数据格式
    只能在python中使用
'''


#!/usr/bin1/env python3
#coding:uft-8

import json

data = {
    'roles':[
        {'role':'monster','type':'pig','life':50},
        {'role':'hero','type':'关羽','life':80}
    ]
}



f = open("test.json","w")
json.dump(data,f)

