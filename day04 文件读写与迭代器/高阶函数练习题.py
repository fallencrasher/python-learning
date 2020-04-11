#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-11 16:06:49
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

def func2(a,list1=[]):
	list1.append(a)
	return list1


#print(list1) # 会报错
print(func2(10))
print(func2(123,[]))
print(func2('a'))

