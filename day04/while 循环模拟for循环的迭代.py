#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-09 23:16:27
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

#迭代器


l1 = [1,2,3,4,5,6,7,8]
#将可迭代对象转化为迭代器
obj = iter(l1)

while True:
	print(next(obj))
