# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-24 16:29:45
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-24 16:29:45
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-23 11:34:39
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

#自定义队列 Queue 先进先出
class Queue(object):
	"""docstring for Queue"""
	def __init__(self,lst=[]):
		self.list = lst
	def put(self,x):
		self.list.append(x)
	def get(self):
		return self.list.pop(0)

l = Queue()
l.put(1)
l.put(2)
print(l.list) #[1,2]
l.put(5)
l.put(1)
print(l.list) #[1,2,5,1]
print(l.get()) #[1]
print(l.get()) #[2]
print(l.get()) #[5]





# 自定义栈，Stack， 后进先出
class Stack(object):
	"""docstring for Stack"""
	def __init__(self, lst=[]):
		super(Stack, self).__init__()
		self.list = lst
	def put(self,x):
		self.list.append(x)
	def get(self):
		return self.list.pop()

l = Stack()
l.put(1)
l.put(2)
print(l.list) #[1,2]
l.put(5)
l.put(1)
print(l.list) #[1,2,5,1]
print(l.get()) #1
print(l.get()) #5
print(l.get()) #2

# Queue 和 Stack 的父类继承
## 方法一
class Foo(object):
	def __init__(self,lst=[]):
		self.list = lst
	def put(self,x):
		self.list.append(x)

class Queue(Foo):
	def get(self):
		return self.list.pop(0)

class Stack(Foo):
	def get(self):
		return self.list.pop()

## 方法二
class Foo(object):
	def __init__(self,lst=[]):
		self.list = lst
	def put(self,x):
		self.list.append(x)

class Queue(Foo):
	def get(self):
		return self.list.pop(0)

class Stack(Foo):
	pass

## 方法三
class Foo(object):
	def __init__(self,lst=[]):
		self.list = lst
	def put(self,x):
		self.list.append(x)
	def get(self):
		return self.list.pop() if self.index else self.list.pop()
class Queue(Foo):
	def __init__(self):
		self.index = 0

class Stack(Foo):
	def __init__(self):
		self.index = 1



# 自定义 pickle

class Mypickle(object):
	"""docstring for Pickle"""
	def __init__(self,file=''):
		super(Mypickle, self).__init__()
		self.file = file
	def mydump(self,obj):
		import pickle
		with open(self.file,mode='ab') as f:
			pickle.dump(obj,f)
	def myload(self):
		import pickle
		with open(self.file,mode='rb') as f:
			while True:
				try:
					yield pickle.load(f)
				except EOFError:
					break
	# 另一种方法
	# def myload(self):
	# 	import pickle
	# 	l = []
	# 	with open(self.file,mode='rb') as f:
	# 		while True:
	# 			try:
	# 				l.append(pickle.load(f))
	# 			except EOFError:
	# 				break
	# 	return l	
class Course:
	def __init__(self,name,period,price):
		self.name = name
		self.period = period
		self.price = price

python = Course('python','6 moneth',21800)
linux = Course('linux','5 moneth',19800)
go = Course('go','4 moneth',12800)

ret = Mypickle('userlist')
ret.mydump(python)
ret.mydump(linux)
ret.mydump(go)

obj = ret.myload()

# print(next(obj).name)
# print(next(obj).name)
# print(next(obj).name)

for i in obj:
	print(i.name,i.period,i.price)

						