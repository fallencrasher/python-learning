# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-24 09:56:40
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-24 11:12:24
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-24 09:31:18
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

1.面向对象中为什么要有继承?
为了提高代码的重用性
为了提高代码的可读性
为了规范开发过程

2.Python继承时，查找成员的顺序遵循什么规则?
新式类--广度优先
经典类--深度优先
3.看代码写结果

class Base1:
    def f1(self):
        print('base1.f1')

    def f2(self):
        print('base1.f2')

    def f3(self):
        print('base1.f3')
        self.f1()


class Base2:
    def f1(self):
        print('base2.f1')


class Foo(Base1, Base2):
    def f0(self):
        print('foo.f0')
        self.f3()


obj = Foo()
obj.f0()
# foo.f0
# base1.f3
# base1.f1

4.看代码写结果

class Base:
    def f1(self):
        print('base.f1')

    def f3(self):
        self.f1()
        print('base.f3')


class Foo(Base):
    def f1(self):
        print('foo.f1')

    def f2(self):
        print('foo.f2')
        self.f3()


obj = Foo()
obj.f2()
# foo.f2
# base.f1
# bsee.f3

5.补充代码实现下列需求
import re
class User(object):
	"""docstring for User"""
	def __init__(self, name,pwd,email):
		super(User, self).__init__()
		self.name = name
		self.pwd = pwd
		self.email = email

user_list = []  
count = 0
while True: 
	user = input(“请输入用户名:”)  
	pwd = input(“请输入密码:”)  
	email = input(“请输入邮箱:”) 
    if re.match('(?:\w+[+-*/\|.]?)+\@(?:\w+\.)+\w+',email):
    	temp = User(name,pwd,email)
    	user_list += temp
    	count +=1

    else:
    	print('邮箱格式错误！')

    if count <4:
    	continue
    else:
    	for i in user_list:
    		print(i.name,i.email)
    	breakimport re
class User(object):
	"""docstring for User"""
	def __init__(self, name,pwd,email):
		super(User, self).__init__()
		self.name = name
		self.pwd = pwd
		self.email = email

user_list = []  
count = 0
while True: 
	if count <4:	
		user = input("请输入用户名:")  
		pwd = input("请输入密码:")  
		email = input("请输入邮箱:") 
		if re.match('(?:\w+[\+\-\*\/\\\|\.]?)+\@(?:\w+\.)+\w+',email):
			temp = User(user,pwd,email)
			user_list.append(temp)
			count +=1

		else:
			print('邮箱格式错误！')	
	else:
		for i in user_list:
			print(i.name,i.email)
		break
"""
# 需求
1. while循环提示 户输 : 户名、密码、邮箱(正则满 邮箱格式)
2. 为每个 户创建 个对象，并添加到 表中。
3. 当 表中的添加 3个对象后，跳出循环并以此循环打印所有 户的姓名和邮箱
"""

		



6.补充代码，实现用户登录和注册

class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


class Account:
    def __init__(self):
        # 用户列表，数据格式：[user对象，user对象，user对象]
        self.user_list = '.\userlist'

    def login(self):
        """
        用户登录，输入用户名和密码然后去self.user_list中校验用户合法性
        :return:
        """
        import pickle
        uid = input('username:')
        pwd = input('password:')
        with open(self.user_list,'rb') as f:
            ret = pickle.load(f)
            for i in ret:
                if uid==i.name and pwd==i.pwd:
                    print('login successfully')
                    return True
            else:
                print('login failed')
                return False
            pass

    def register(self):
        """
        用户注册，没注册一个用户就创建一个user对象，然后添加到self.user_list中，表示注册成功。
        :return:
        """
        import pickle
        uid = input('username:')
        pwd = input('password:')
        pwd2 = input('password again:')
        if pwd==pwd2:
            for i in self.user_list:
                if i.name == uid
                print('username is invalid.')
            else:
                temp = User(uid,pwd)
                with open(self.user_list,mode='ab'):
                    pickle.dump(temp,f)
                print('register successfully')
        else:
            print('the two passwords are not same.')

    def run(self):
        """
        主程序
        :return:
        """
        # while True:
        #     judge = input('1.register or 2.login?(please input the number!):')
            # if judge.isdigit() and int(judge) in (1,2):
            #     if int(judge)==1:
            #         self.register()
            #     elif int(judge)==2:
            #         self.login()
            #         break
            # pass
        #还可以用 enumrate 来提取操作号
        opration = ['register','login']
        while True:
            for index,item in enumerate(opration):
                print(index,item)
            judge = input('please input the opration number:').strip()
            if judge.isdigit() and int(judge) in (1,2):
            if int(judge)==1:
                self.register()
            elif int(judge)==2:
                self.login()
                break
        


if __name__ == '__main__':
    obj = Account()
    obj.run()
7.读代码写结果

class Base:
    x = 1
    
obj = Base()


print(obj.x)  #1
obj.y = 123
print(obj.y) #123
obj.x = 123
print(obj.x) # 123
print(Base.x) #1
8.读代码写结果

class Parent:
    x = 1
    
class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x,Child1.x,Child2.x) #1 1 1
Child2.x = 2
print(Parent.x,Child1.x,Child2.x) #1 1 2
Child1.x = 3
print(Parent.x,Child1.x,Child2.x) #1 3 2
9.看代码写结果

class Foo(object):
    n1 = '武沛齐'
    n2 = '金老板'
    def __init__(self):
        self.n1 = 'eva'

obj = Foo()
print(obj.n1) # eva
print(obj.n2) # 金老板
10.看代码写结果，【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】

class Foo(object):
    n1 = '武沛齐'
    def __init__(self,name):
        self.n2 = name
obj = Foo('太白')
print(obj.n1) # 武沛齐
print(obj.n2) # 太白

print(Foo.n1) #武沛齐
print(Foo.n2) # 报错
