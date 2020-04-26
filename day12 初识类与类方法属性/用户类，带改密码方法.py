# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-21 21:58:18
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-21 22:22:49

# # 定义一个用户类,用户名和密码是这个类的属性,实例化两个用户,分别有不同的用户名和密码
# 	# 设计一个方法 修改密码
# 	# 你得先登录才能修改密码

import time
import os

def auth(f):
	def inner(*args,**kwargs):
		if login():
			ret = f(*args,**kwargs)
			return ret
	return inner

def login():
	username = input("username:").strip()
	password = input("password:").strip()
	with open('userinfo',encoding='utf-8') as f1:
		for i in f1:
			uid,pwd = i.strip().split('|')
			if username==uid and password==pwd:
				print('login successfully')
				return True
		else:
			print('login failed')
			return False

	   

class User(object):
	"""docstring for user"""
	def __init__(self, username,password):
		super(User, self).__init__()
		self.username = username
		self.password = password

	@auth
	def fix_pass(self):
		oldpwd = input('please input your old password:') 
		if oldpwd == self.password:
			newpwd = input('please input your new password:')
			with open('userinfo',encoding='utf-8',mode='r') as f2,open('userinfo.bak',encoding='utf-8',mode='w') as f3:
				for line in f2:
					uid,pwd = line.strip().split('|')
					if uid == self.username:
						self.password = newpwd.strip()
						pwd = newpwd.strip()
						f3.write("{}|{}\n".format(uid,pwd))
					else:
						f3.write('{}\n'.format(line))
			os.remove('userinfo')
			os.rename('userinfo.bak','userinfo')
			return True
		else:
			return False

		

		
fallen = User('fallen','123456')

#print(fallen.__dict__)
fallen.fix_pass()