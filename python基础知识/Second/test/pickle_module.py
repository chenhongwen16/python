#!/usr/bin/env python3
#coding:utf-8

import pickle

d = {'name':'alex','age':22}
l = [1,2,3,4,'rain']

pk = open("data.pkl","wb")
print(pickle.dump(d,pk))