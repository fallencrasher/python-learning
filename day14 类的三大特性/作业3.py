#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-24 21:52:26
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

# 用户输入用户名密码性别
# 实例化对象
# 用户任意输入内容 : 不能用异常处理
    # 如果输入的是属性名 打印属性值
    # 如果输入的是方法名 调用fangfa
    # 如果输入的什么都不是 不做操作

class User:
    def __init__(self,name,age,sex):
        self.name = name
        self.age  = age
        self.sex  = sex
    def eat(self):
        print('eating')
    def sleep(self):
        print('sleeping')



def run():
	username = input('username:')
	age = input('age:')
	sex = input('sex:')
	temp = User(username,age,sex)
	while True:
		judge = input('operation(attribute or method of User), input "q" or "quit" to quit.\n >>>').strip()
		if judge.lower()=='q' or judge.lower()=='quit':
			break
		else:

			if hasattr(temp,judge):
				if callable(getattr(temp,judge)):
					getattr(temp,judge)()
				else:
					print(getattr(temp,judge))
			else:
				continue
	
if __name__ == '__main__':
	run()
