#!/usr/bin/env python
#coding:utf-8

import jieba
import jieba.posseg as pseg
import jieba.analyse

str1 = "我来到北京清华大学"
str2 = 'python的正则表达式是好用的'
str3 = "小明硕士毕业于中国科学院计算所，后来在日本京都大学深造"

seg_list = jieba.cut(str1,cut_all = True)
result = pseg.cut(str1)
result2 = jieba.cut(str2)
result3 = jieba.analyse.extract_tags(str1,2)
result4 = jieba.cut_for_search(str3)

print " /".join(seg_list)

for w in result:
    print w.word,"/",w.flag,", ",

for t in result2:
    print t

for s in result3:
    print s

print " ,".join(result4)