#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-11 15:49:07
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

data_list = []

def func(arg):
	return data_list.insert(0,arg)

data = func("hhhh")

print(data)
print(data_list)


def func2(a,list1=[]):
	list1.append(a)
	return list1

list2 = func2(10)
list3 = func2(123,[])
list4 = func2('a')

#print(list1) # 会报错
print(list2)
print(list3)
print(list4)

