#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-15 09:01:45
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

# random 模块
import random

# 左闭右开，获取 [0.0,1.0) 范围内的一个浮点数,不接收参数
# random.random()
a = random.random()
print(a)

# 左闭右开， 获取 [a,b) 范围内的一个浮点数
# random.uniform()
b = random.uniform(3,5)
print(b)

# 闭区间， 获取[a,b] 范围内的一个整数
# random.randint(a,b)
c = random.randint(3,10)
print(c)


# 混洗。 把参数指定的数据元素打乱顺序，参数必须是可变类型 [] {}
# random.shuffle(x)
lst1 = list(range(10))
print(lst1)
random.shuffle(lst1)
print(lst1)

# 取样。 从 x 中随机抽取 k 个数据，组成一个列表返回
# random.sample(x,k)
tu1 = (1,2,3,4,5,6,)
lst2 = random.sample(tu1,5)
print(lst2)



