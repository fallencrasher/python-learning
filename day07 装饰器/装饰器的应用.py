#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-14 17:58:38
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

#装饰器的应用

#登陆认证

def get_user_pwd():
    usr_dict = {}
    with open('register.txt',encoding='utf-8',mode='r') as f:
        for i in f:
            i = i.strip().split('|',1)
            usr_dict[i[0]]=i[1]
    return usr_dict


def login():
    count = 0
    dict1=get_user_pwd()
    while count<4:
        username = 'fallen' #input('username:')
        password = 'wangyishan043000' #input('password:')                
        if username not in list(dict1.keys()):
            print('您还没有注册！') 
        else:
            if dict1[username]!=password:
                print('username or password error!')
            else:
                print('login successfully!')
                return True
        count += 1

def register():
    while True:
        username =  input('username:')
        password =  input('password:')
        with open('register.txt',encoding='utf-8') as f, open('register.txt',encoding='utf-8',mode='a') as f1:
            dict1 = {}
            for i in f:
                i = i.strip().split('|',1)
                dict1[i[0]]=i[1]
            if username in list(dict1.keys()):
                print('you already have a accout!Please login.')
                login()
                return False
            else:
                f1.write('\n'+username+'|'+password)
                return True

status_dict = {
	'username' : None,
	'status': False,
}

def auth(f):
	'''
	你的装饰器完成：访问被装饰函数之前，写一个三次登陆认证的功能。
	登录成功，让其访问被装饰的函数；登陆不成功，不让访问
	'''
	def inner(*args,**kwargs):
		'''访问之前的操作'''
		if status_dict['status']:
			ret = f(*args,**kwargs)
			return ret
		else:
			username=input('username:')
			password = input('password:')
			if username=='fallen' and password == '123456':
				print('登录成功')
				status_dict['username']=username
				status_dict['status']=True
				ret = f(*args,**kwargs)
				return ret
			else:
				print('登录失败')
	return inner 

@auth
def article():
	print('欢迎访问文章页面！')
article()

@auth
def comment():
	print('欢迎访问评论页面')
comment()

@auth
def dariy():
	print('欢迎访问日记页面')
dariy()

