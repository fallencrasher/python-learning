#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-13 23:26:51
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

#闭包：封闭的东西：保证数据的安全
#闭包是内层函数对外层函数非全局变量的引用
#被引用的外层函数变量称为自由变量，这个自由变量会与内层函数产生一个绑定关系
#自由变量不会消失
#这个自由变量就是我们要保证安全的数据
#闭包只存在于嵌套函数
#判断是不是闭包：
#1.嵌套函数
#2.内层函数必须引用外层函数的变量或者参数
#3.闭包肯定含有自由变量，可以用 .__code__.co_freevars  方法来判断是不是闭包

'''
例如：整个历史中的某个商品的平均收盘价。什么叫平局收盘价呢？就是从这个商品一出现开始，每天记录当天价格，然后计算他的平均值：平均值要考虑直至目前为止所有的价格。

比如大众推出了一款新车：小白轿车。

第一天价格为：100000元，平均收盘价：100000元

第二天价格为：110000元，平均收盘价：（100000 + 110000）/2 元

第三天价格为：120000元，平均收盘价：（100000 + 110000 + 120000）/3 元

........
'''

l1 = [] #全局变量，数据不安全

def make_average(new_value):
	l1.append(new_value)
	total = sum(l1)
	average = total/len(l1)
	return average
print(make_average(10000))
print(make_average(11000))
print(make_average(12000))

#怎么改呢？l1 不能是全局变量
def make_average2():
	l1=[]
	def averager(new_value):
		l1.append(new_value)
		total = sum(l1)
		return total/len(l1)
	return averager

avg = make_average2()
print(list(map(avg,[10000,11000,12000])))
print(avg.__code__.co_freevars)   #('l1',)
#我们可以这样，定义外层函数，在外层函数声明我们想要保护的数据
#在内层函数中对这些数据进行修改，在内层函数中返回处理结果
#然后在外层中返回内层函数名

#判断是是不是闭包的代码
def wrapper(a,b):
	def inner():
		print(a)
		print(b)
	return inner

a = 2 
b = 3 
ret = wrapper(a,b)
print(ret.__code__.co_freevars)  #('a', 'b')


