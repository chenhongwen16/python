#!/usr/bin/env python
#coding:utf-8


def recur_fibo(n):
   """递归函数
   输出斐波那契数列"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

print(recur_fibo(3))