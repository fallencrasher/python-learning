#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-08 14:32:03
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

'''
判断用户是否能登录
要是登录了就把选择的物品加入购物车
登录要验证码
'''
import random

#define function
def generage_checkcode(n):
	s = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	code = ""
	for i in range(n):
		ran = random.randint(0,len(s)-1)
		code += s[ran]
	return code
		

def login():
	username = input("Input your username:")
	password = input('Input your password:')
	#得到一个验证码
	code = generage_checkcode(4)
	print('checkcode is :',code)
	code1 = input("Input checkcode:")
	#验证
	if code.lower() == code1.lower():
		if username==uname and password==pwd:
			print("Login successfully")
		else:
			print("username or password error.")
	else:
		print("checkout input error.")



#use the function
uname = 'fallen'
pwd = '123456'
login()















