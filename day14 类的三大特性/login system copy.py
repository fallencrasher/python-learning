# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-24 09:56:43
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-24 17:25:18
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-22 10:48:58
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$
import pickle

class User:
	def __init__(self, name, pwd):
		self.name = name
		self.pwd = pwd


class Account:
	def __init__(self):
		# 用户列表，数据格式：[user对象，user对象，user对象]
		self.user_list = 'userlist'

	def login(self):
		"""
		用户登录，输入用户名和密码然后去self.user_list中校验用户合法性
		:return:
		"""
	
		uid = input('username:')
		pwd = input('password:')
		ret = self.get_file_info()
		for i in ret:
			if uid == i.name and pwd == i.pwd:
				print('login successfully')
				return True
		else:
			print('login failed')
			return False
		

	
	def get_file_info(self):
		import pickle
		with open(self.user_list, mode='rb') as f:
			while True:
				try:
					yield pickle.load(f)
				except EOFError:
					break

	def register(self):
		"""
		用户注册，没注册一个用户就创建一个user对象，然后添加到self.user_list中，表示注册成功。
		:return:
		"""
		name_valid = True
		count = 0
		while count<4:
			uid = input('username:')
			pwd = input('password:').strip()
			pwd2 = input('password again:').strip()
			if pwd == pwd2:
				temp_f=self.get_file_info()
				l =[]
				for i in temp_f:
					l.append(i.name)
					if uid in l:
						print('username is invalid')
						count +=1
						name_valid = False
					# if i.name == uid:
					# 	print('username is invalid.')
					# 	name_valid = False
					# 	count += 1
					# 	continue
				if name_valid:
					import pickle
					temp = User(uid, pwd)
					with open(self.user_list,mode='ab') as f2:
						pickle.dump(temp, f2)
						print('register successfully')
					break
			else:
				count += 1
				print('the two passwords are not same.')

	

	def run(self):
		"""
		主程序
		:return:
		"""
		while True:
			judge = input('1.register or 2.login?(please input the number!):')
			if judge.isdigit() and int(judge) in (1,2):
				if int(judge)==1:
					self.register()
				elif int(judge)==2:
					self.login()
					break
		
		# # 还可以用 enumrate 来提取操作号
		# opration = ['register', 'login']
		# while True:
		# 	for index, item in enumerate(opration):
		# 		print(index+1, item)
		# 	judge = input('please input the opration number:').strip()
		# 	if judge.isdigit() and int(judge) in (1, 2):
		# 		if int(judge) == 1:
		# 			self.register()
		# 		elif int(judge) == 2:
		# 			self.login()
		# 			break


if __name__ == '__main__':
	obj = Account()
	obj.run()
