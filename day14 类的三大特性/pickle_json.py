# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-24 22:39:27
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-24 23:13:57
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-24 22:05:24
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

#写一个自定义模块,里面有你自己实现的mypickle和myjson,我只需要给你传递一个参数 'pickle'还是'json'


class Mypickle(object):
	"""docstring for Mypickle"""
	def __init__(self,file=''):
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

class Myjson(object):
	"""docstring for Myjson"""
	def __init__(self, file=''):
		self.file = file
	def mydump(self,obj):
		import json
		str_obj = json.dumps(obj)
		with open(self.file,encoding='utf-8',mode='a') as f:
			f.write(str_obj + '\n')
	def myload(self):
		import json
		with open(self.file,encoding='utf-8',mode='r') as f:
			return f.readlines()



# ahhhhhh = 5
# import sys
# print(getattr(sys.modules['__main__'],'ahhhhhh'))
# print(getattr(sys.modules['__main__'],'Mypickle'))

# if __name__=='__main__':
# 	autosave()
# 	autoload()