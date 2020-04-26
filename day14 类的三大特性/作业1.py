# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-24 16:09:54
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-24 16:09:54
# 人狗大战(继承来完成)
    # 人
    # 狗

class Person:
	"""人"""
	def __init__(self, name,sex,job,hp,weapon,ad):
		super(Person, self).__init__()
		self.name = name
		self.sex = sex
		self.job = job
		self.hp = hp
		self.weapon = weapon
		self.ad = ad
		
	def cuo(self,dog):
		dog.hp -= self.ad
		print(f'{self.name}给{dog.name}搓了澡，{dog.name}掉了{self.ad}点血，{dog.name}的当前血量为{dog.hp}')

class Animal(object):
	def __init__(self,name,hp,ad):
		self.name = name
		self.hp = hp
		self.ad = ad
		
	
class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self,name,hp,ad,style):
		Animal.__init__(self,name,hp,ad)
		self.style = style
	def 舔(self,person):
		person.hp -= self.ad
		print('{}舔了{}一口，{}掉了{}血，{}当前血量为{}.'.format(self.name,person.name,person.name,self.ad,person.name,person.hp))

xiaobai = Dog('xiaobai',1000,100,'tidy')
print(xiaobai.__dict__)
alex = Person('alex','male','job',1000,'刀子',150)
print(alex.__dict__)
alex.cuo(xiaobai)

# 计算器

# 进阶
# 员工信息表
# select 查询这个文件
# select name,age where age>20
# select age,name,job where age > 20
# select age,name,job where age < 22
# select age,name,job where age = 22
# select age,name,job where name = 'alex'
# select age,name,job where job = 'IT'
# select age,name,job where phone like '133'
# select * where phone like '133'

# 文件处理 + input
# https://www.cnblogs.com/Eva-J/articles/7776508.html