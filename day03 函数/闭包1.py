#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-08 18:45:15
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

#闭包
#在函数中提出的概念

#当函数定义内部函数，且返回值时内部函数名，就叫闭包
#1.闭包必须是外部函数中定义了内部函数
#2.外部函数是有返回值的，且该返回值就是内部函数名，不能加括号
#3.内部函数引用外部函数的变量值
'''
闭包格式：

def 外部函数()：
	...
	def 内部函数():
		...
	return 内部函数
'''
def func():
	a = 100

	def inner_func():
		b = 99
		print(a,b)

	print(inner_func)
	return inner_func


#调用函数时，用对象接住函数返回的内部函数，那其实，这个对象x就变成了func()的内部函数，当使用 x() 是可以调用它
x = func()

x()
