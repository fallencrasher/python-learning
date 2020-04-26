#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-23 22:03:55
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

# 自定义 json
class Myjson(object):
	"""docstring for Myjson"""
	def __init__(self, file=''):
		super(Myjson, self).__init__()
		self.file = file
	def mydump(self,obj):
		import json
		str_obj = json.dumps(obj)
		with open(self.file,encoding='utf-8',mode='a') as f:
			f.write(str_obj + '\n')
	# def myload(self):
	# 	import json
	# 	with open(self.file,encoding='utf-8',mode='r') as f:
	# 		while True:
	# 			try:
	# 				yield f.readline()
	# 			except EOFError:
	# 				break
	# def myload(self):
	# 	import json
	# 	l = []
	# 	with open(self.file,encoding='utf-8',mode='r') as f:
	# 		while True:
	# 			try:
	# 				l.append(f.readline())
	# 			except EOFError:
	# 				break	
	# 	return l
	# def myload(self):
	# 	import json
	# 	with open(self.file,encoding='utf-8',mode='r') as f:
	# 		return json.load(f)
	def myload(self):
		import json
		with open(self.file,encoding='utf-8',mode='r') as f:
			return f.readlines()
python = ('python','6 moneth',21800)
linux = ('linux','5 moneth',19800)
go = ('go','4 moneth',12800)

ret = Myjson('myjson.json')
ret.mydump(python)
ret.mydump(linux)
ret.mydump(go)

obj = ret.myload()
print(obj)
for i in obj:
	print(i)

