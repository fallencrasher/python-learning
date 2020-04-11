#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-11 19:50:08
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$


#字典推导式
#
lst1 = ['jay','jj','meet']
lst2 = ['周杰伦','林俊杰','郭宝元']

dict1 = {lst2[i]:lst1[i] for i in range(len(lst1))}
print(dict1)

#集合推导式
s1 = {i for i in range(1,11)}
print(s1)