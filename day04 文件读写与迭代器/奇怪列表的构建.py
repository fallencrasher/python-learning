#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-09 17:47:02
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

'''
用代码构建一个列表
[['-','-','-'],['-','-','-'],['-','-','-']]
'''
l = []
l2 = []
# for i in range(3):
# 	for j in range(3):
# 		l2.append("-")
# 	l.append(l2)	

# print(l)


for i in range(3):
	l2.append("-")
print(l2)

for i in range(3):
	l.append(l2)
print(l)