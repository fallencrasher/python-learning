#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-12 21:24:13
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

# lambda function
# lambda 参数1，参数2：表达式
#语法:

# 　　函数名 = lambda 参数:返回值

#     1）此函数不是没有名字，他是有名字的，他的名字就是你给其设置的变量，比如func.

#     2）lambda 是定义匿名函数的关键字，相当于函数的def.

#     3）lambda 后面直接加形参，形参加多少都可以，只要用逗号隔开就行。

func1 = lambda a,b:a+b 
print(func1(1,2))

#写匿名函数：接收一个可切片的数据，返回索引为0与2的对应的元素（元组形式）。
func2 = lambda a:(a[0],a[2])
print(func2([1,2,3,4]))

#写匿名函数：接收两个int参数，将较大的数据返回。
func3 = lambda a,b:a if a>b else b
print(func3(1,4))
