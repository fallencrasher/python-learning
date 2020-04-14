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

# 简述一下yield 与yield from的区别。
#
# 看下面代码，能否对其简化？说说你简化后的优点？
#
#
def chain(*args):
    # ('abc',(0,1,2))
    for it in args:
        for i in it:
            yield i
g = chain('abc',(0,1,2))
怎么让生成器产出值？
next ，for 循环, 转化成list
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(list(g))
print(list(g))  # 将迭代器转化成列表


def chain(*args):
    # ('abc',(0,1,2))
    for it in args:
        yield from it  # 'abc'  (0,1,2)
g = chain('abc',(0,1,2))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

