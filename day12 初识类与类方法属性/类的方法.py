# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-20 18:13:47
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-20 18:18:28
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-20 17:48:40
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

# 面向过程 : 想要一个结果 写代码 实现计算结果
# 面向对象开发 : 有哪些角色 角色的属性和技能 两个角色之间是如何交互的

# 复杂的 拥有开放式结局的程序 比较适合使用面向对象开发
    # 游戏
    # 购物

# 类和对象之间的关系?
    # 类 是一个大范围 是一个模子 它约束了事物有哪些属性 但是不能约束具体的值
    # 对象 是一个具体的内容 是模子的产物 它遵循了类的约束 同时给属性赋上具体的值


# class Person:
# 	"""人"""
# 	def __init__(self, name,sex,job,hp,weapon,ad):
# 		super(Person, self).__init__()
# 		self.name = name
# 		self.sex = sex
# 		self.job = job
# 		self.hp = hp
# 		self.weapon = weapon
# 		self.ad = ad
		
# 	def cuo(self,dog):
# 		dog.hp -= self.ad
# 		print(f'{self.name}给{dog.name}搓了澡，{dog.name}掉了{self.ad}点血，{dog.name}的当前血量为{dog.hp}')

# class Dog:
# 	def __init__(self, name,hp,ad,style):
# 		super(Dog, self).__init__()
# 		self.name = name
# 		self.hp = hp
# 		self.ad = ad
# 		self.style = style
# 	def 舔(self,person):
# 		person.hp -= self.ad
# 		print('{}舔了{}一口，{}掉了{}血，{}当前血量为{}.'.format(self.name,person.name,person.name,self.ad,person.name,person.hp))

# alex = Person('alex','male','搓澡工',260,'搓澡巾',1)
# print('alex : ',alex) #alex :  <__main__.Person object at 0x0033B058> 一个类对象

# 小白 = Dog('小白',5000,249,'柴狗')
# print('小白： ',小白)

# alex.cuo(小白)
# 小白.舔(alex)

# print(小白.__dict__) #{'name': '小白', 'hp': 4999, 'ad': 249, 'style': '柴狗'} 打印出全部属性
# print(alex.__dict__) #{'name': 'alex', 'sex': 'male', 'job': '搓澡工', 'hp': 11, 'weapon': '搓澡巾', 'ad': 1}

# # 定义一个圆形类,半径是这个圆形的属性,实例化一个半径为5的圆形,一个半径为10的圆形
#     # 完成方法
#     # 计算圆形面积
#     # 计算圆形周长
# import math
# class Circle(object):
# 	"""docstring for Circle"""
# 	def __init__(self, r):
# 		super(Circle, self).__init__()
# 		self.r = r
	
# 	def circumferrence(self):
# 		print('圆的周长为{}'.format(2*self.r*math.pi))
	
# 	def measure(self):
# 		print('圆的面积为{}'.format(self.r*self.r*math.pi))

# c1 = Circle(5)
# c1.circumferrence()
# c1.measure()



# # 定义一个用户类,用户名和密码是这个类的属性,实例化两个用户,分别有不同的用户名和密码
# 	# 设计一个方法 修改密码
# 	# 你得先登录才能修改密码

# import time

# dic = {'uid':'fallen','passwd':'123456'}

# def auth(f):
# 	def inner(*args,**kwargs):
# 		if login():
# 			ret = f(*args,**kwargs)
# 			return ret
# 	return inner

# def login():
# 	username = input("username:").strip()
# 	password = input("password:").strip()
# 	if username==dic['uid'] and password==dic['passwd']:
# 		print('登陆成功')
# 		return True
# 	else:
# 		print('登录失败')
# 		return False


# class user(object):
# 	"""docstring for user"""
# 	def __init__(self, username,password):
# 		super(user, self).__init__()
# 		self.username = username
# 		self.password = password
# 	@auth
# 	def fix_pass(self):
# 		count = 0
# 		while True:
# 			judge = input('要改密码吗？(yes/no):').strip()
# 			if judge.lower()=='yes': 
# 				self.password = input('new password:').strip()
# 				dic['password'] = self.password
# 				return True
# 			elif judge.lower()=='no':
# 				return False
# 				break
# 			else:
# 				print('请输入 yes 或 no.')



		

		
# xiaoming = user('xiaoming','123456')
# dacheng = user('dacheng','654321')

# print(xiaoming.__dict__,dacheng.__dict__)
# xiaoming.fix_pass()

# 算法
# 二分查找  [1,2,3,4,5,6,7,8,9,10,27,36,46,58,69] - 有序列表
# 不用in index 从列表中找到一个值的位置
# 实现上面的功能 - 用代码

lst1 = [1,2,3,4,5,6,7,8,9,10,27,36,46,58,69]

# def search(num,lst,left ,right):
	
# 	if right>left:
# 		mid = int((left+right)/2)
# 		if lst[mid]==num:
# 			return mid
# 		elif lst[mid] > num:
# 			right=mid
# 			search(num,lst,left,right)
# 		elif lst[mid] < num:
# 			left=mid
# 			search(num,lst,left,right)
# 	else:
# 		return -1



	# mid = len(lst)/2
	# if mid >=1:
	# 	mid = int(mid)
	# 	if lst[int(len(lst)/2)] > num:
	# 		return search(num,lst[range(0,len(lst)/2)])
	# 	elif lst[int(len(lst)/2)] < num:
	# 		return search(num,lst[range(len(lst)/2,len(lst))])
	# else:
	# 	mid
	# return mid
print(lst1.index(58))
print('index',search(58,lst1,0,len(lst1)-1))

# while True:
# 	if lst1[len(lst1)/2] < num:
# 		lst2=lst1[range(len(lst1/2),len(lst))]
# 		if lst2[]


## 菜鸟教程答案
# 返回 x 在 arr 中的索引，如果不存在返回 -1
def binarySearch (arr, l, r, x): 
  
    # 基本判断
    if r >= l: 
  
        mid = int(l + (r - l)/2)
  
        # 元素整好的中间位置
        if arr[mid] == x: 
            return mid 
          
        # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # 元素大于中间位置的元素，只需要再比较右边的元素
        else: 
            return binarySearch(arr, mid+1, r, x) 
  
    else: 
        # 不存在
        return -1
  
# 测试数组
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
print('index',search(10,arr,0,len(lst1)-1))
# 函数调用
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("元素在数组中的索引为 %d" % result )
else: 
    print ("元素不在数组中")