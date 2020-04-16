#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-14 16:20:53
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

#装饰器：在不改变原被装饰的函数的源代码以及调用方式下，为其添加额外的功能。

#开放封闭原则：
#开放：对代码的扩展是开放的
#封闭：对源码的修改是封闭的

#装饰器：完全遵守开放封闭原则
#装饰器就是一个函数，他的功能就是为另一个函数添加新的功能，但是不能改变
#那个函数的调用方式
#装饰器的本质就是闭包

#版本一：写一些代码测试 index 函数的执行效率
#但是，如果想要测试另一个函数，就得再写一个一遍，不好
def index():
	'''省略一堆代码''' #模拟网路延迟
	time.sleep(2)
	print('欢迎登陆博客园')

def dairy():
	time.sleep(2)
	print('欢迎来到b站')
import time
print(time.time()) #这一刻的格林威治时间

start_time=time.time()
index()
end_time = time.time()
print(end_time-start_time) #这个就测出了函数执行的时间

start_time=time.time()
dairy()
end_time = time.time()
print(end_time-start_time) #这个就测出了函数执行的时间


#版本二:利用函数解决代码重复使用问题
#这个版本的问题：这么写，确实没改变源码，而且给 原函数增加了新功能，
#但是我们改变了原函数的调用方式
def timmer(f):
	start_time = time.time()
	f()
	end_time = time.time()
	print(f'测试函数执行效率：{end_time - start_time}')
timmer(index)

#版本三：不能改变原函数的调用方式
def timmer2(f):  # 这个函数就是装饰器了，但是不是终极形态
	def inner():
		start_time = time.time()
		f() #index()
		end_time = time.time()
		print(f'测试函数执行效率：{end_time - start_time}')
	return inner

# ret = timmer2(index) #inner
# ret() #inner()

index = timmer2(index) #inner
index() #inner() 这就按照原来的方式调用了原函数，而且为其增加了执行效率功能


#版本四：装饰器，python做优化，叫做语法糖
import time
def timmer2(f): #装饰器函数一定要写在被装饰函数前边
	def inner():  
		start_time = time.time()
		f() #index()
		end_time = time.time()
		print(f'测试函数执行效率：{end_time - start_time}')
	return inner

@timmer2 #在被装饰函数前边，写个这个，就可为下边函数增加功能了
def index():
	'''省略一堆代码''' #模拟网路延迟
	time.sleep(0.6)
	print('欢迎登陆博客园')
index()

def dairy(): #这个函数定义的时候没有在前边写装饰器的语法糖，所以没有附加功能
	time.sleep(0.6)
	print('欢迎来到b站')

dairy()

#版本六：被装饰函数带返回值.装饰器不应该改变原函数的返回值
import time
def timmer2(f): #装饰器函数一定要写在被装饰函数前边
	def inner():  
		start_time = time.time()
		print(f'真正的index()返回值位置:{f()}') #index()
		end_time = time.time()
		print(f'测试函数执行效率：{end_time - start_time}')
	return inner

@timmer2 #在被装饰函数前边，写个这个，就可为下边函数增加功能了
def index():
	'''省略一堆代码''' #模拟网路延迟
	time.sleep(0.6)
	print('欢迎登陆博客园')
	return 666
ret=index() 
#这里，index()实际上就是 timmer2装饰器里的inner()
#当真正的 index() 函数有返回值的时候，这个返回值其实
#没有被返回给 ret ，而是停留在 inner() 函数里边的 f()上
#所以要想把 index() 函数的返回值正经赋给 ret,还得在装饰器里
#加上一步返回值步骤
#上一步给 ret 的赋值，实际上是赋值的 inner()的返回值，但是
#inner()没有返回值。所以就啥都没有赋值
print(ret) #None ，赋值没成功，所以这里打印就是none

#版本七：解决装饰器会改变被装饰函数返回值的问题

import time
def timmer2(f): #装饰器函数一定要写在被装饰函数前边
	def inner():  
		start_time = time.time()
		r = f() #index()
		end_time = time.time()
		print(f'测试函数执行效率：{end_time - start_time}')
		return r
	return inner

@timmer2 #在被装饰函数前边，写个这个，就可为下边函数增加功能了
def index():
	'''省略一堆代码''' #模拟网路延迟
	time.sleep(0.6)
	print('欢迎登陆博客园')
	return 666
ret=index() 
print(ret)

#版本八：当被装饰函数有参数
import time
def timmer2(f): #装饰器函数一定要写在被装饰函数前边
	def inner(*args,**kwargs):  
		#函数定义时，*args,**kwargs，将参数聚合
		start_time = time.time()
		r = f(*args,**kwargs) #index()
		#函数调用h时，*args,**kwargs,将参数打散
		end_time = time.time()
		print(f'测试函数执行效率：{end_time - start_time}')
		return r
	return inner

@timmer2 #在被装饰函数前边，写个这个，就可为下边函数增加功能了
def index(name):
	'''省略一堆代码''' #模拟网路延迟
	time.sleep(0.6)
	print(f'欢迎{name}登陆博客园')
	return 666
ret=index('fallen') 
print(ret)

@timmer2
def dairy(name,age):
	time.sleep(0.5)
	print(f'欢迎{age}岁{name}来到b站')
dairy('fallen',18)


'''
********************
		重要
********************
'''
#标准的装饰器函数定义

def wrapper(f):
	def inner(*args,**kwargs):
		'''
		在这里添加额外的功能
		执行被装饰函数之前的操作
		'''
		ret = f(*args,**kwargs)
		'''
		在这里添加额外的功能
		执行被装饰函数之后的操作
		'''
		return ret
	return inner
