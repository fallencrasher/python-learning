#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-09 23:08:50
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

#判断对象是否是迭代器
with open('file1',encoding='utf-8',mode='w') as f1:
	print(('__iter__' in dir(f1)) and ('__next__' in dir(f1)))

#可迭代对象可以转化为迭代器
s1 = 'jofjs'
obj = iter(s1) #或者 s1.__iter__() 都可以
print(obj)

#迭代器可以一个一个取值,下边这俩都行，每写一次迭代代码，就弹出来一个值
print(next(obj)) #print(obj.__next__())
print(next(obj)) #print(obj.__next__())
print(next(obj)) #print(obj.__next__())
print(next(obj)) #print(obj.__next__())
print(next(obj)) #print(obj.__next__())
#如果迭代超出范围了，就会报错