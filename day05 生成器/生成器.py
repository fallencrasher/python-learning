#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-11 16:30:31
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$


#生成器
#生成器的本质就是迭代器。他与迭代器的区别是，生成器是我么自己用py#thon代码构建的数据结构，迭代器是他提供的，或者转化来的

#获取生成器的三种方式：
##生成器函数
##生成器表达式
##python内部提供的一些

#生成器函数获取生成器

def func():
	print(111)
	print(222)
	yield 3
	yield 4
ret = func() 
#ret就变成了生成器对象，因为生成器本质上是个迭代器，所以这个ret就是个迭代器对象，普通打印只能打印内存地址
print(ret)  #<generator object func at 0x01DA83E0>
#要想打印ret，要用到 next() 函数 或 __next__ 方法
print(next(ret))  #或 print(ret.__next__())
print(ret.__next__())


#return yield
#return : 函数中只存在一个return结束函数，并且给函数执行者返回值
#yield  : 只要函数中有 yield ，函数就是生成器函数，yield 不结束
# 函数，一个yield对应一个next()

#吃包子
#用可迭代对象
def func3():
	l1 = []
	for i in range(1,5001):
		l1.append(f"{i}号包子")
	return l1
ret = func3()
print(ret)

#用生成器
def func2():
	for i in range(1,5001):
		yield f"{i}号包子"

ret = func2()

for i in range(200):
	print(next(ret))


#yield from ： 将一个可迭代对象变成一个生成器
def func4():
	l1 = [1,2,3,4,5]	
	yield from l1
	#将列表变成迭代器返回
ret =  func4()
print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))

#如果使用多个 yield from,那就会先把第一个 yield from 迭代完了再执行第二个

def func():
    lst1 = ['卫龙','老冰棍','北冰洋','牛羊配']
    lst2 = ['馒头','花卷','豆包','大饼']
    yield from lst1
    yield from lst2
    
g = func()
#因为，g是个迭代器了，就可以直接用for 循环去遍历他，然后打印，for循环内
#本来就是要把可迭代对象转换为迭代器然后一个一个执行的
for i in g:
    print(i)
    