#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-09 08:18:53
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

#递归

def calc(n):
	print(n)
	if int(n/2)==0:
		return n
	res = calc(int(n/2))
	return res

calc(10)
a = calc(10)
print(a)