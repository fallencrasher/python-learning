#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-11 18:32:08
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

#生成器表达式
#与列表推倒式写法几乎一模一样
#就是把列表推倒式的中括号改成小括号

#列表推导式
print([i for i in range(1,11)])

#生成器表达式，有点就是省内存
obj = (i for i in range(1,11))

for i in obj:
	print(i)



