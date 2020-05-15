#1、看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】

class Foo(object):
	a1 = 1
	__a2 = 2
	
	def __init__(self,num):
		self.num = num
		self.__salary = 1000
		
	def show_data(self):
		 print(self.num+self.a1)
	
obj = Foo(666)

print(obj.num) #666
print(obj.a1) #1
#print(obj.__salary) #报错
#print(obj.__a2) #报错
print(Foo.a1) #1
#print(Foo.__a2) #报错
#2、看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】

class Foo(object):
	a1 = 1
	
	def __init__(self,num):
		self.num = num
	def show_data(self):
		print(self.num+self.a1)
	
obj1 = Foo(666)
obj2 = Foo(999)
print(obj1.num) #666
print(obj1.a1) #999

obj1.num = 18
obj1.a1 = 99

print(obj1.num) #18
print(obj1.a1) #99

print(obj2.a1) #1
print(obj2.num) #999
print(obj2.num) #999
print(Foo.a1) #1
print(obj1.a1) #99
#3、看代码写结果，注意返回值。

class Foo(object):
	
	def f1(self):
		return 999
	
	def f2(self):
		v = self.f1()
		print('f2')
		return v
	
	def f3(self):
		print('f3')
		return self.f2()
	
	def run(self):
		result = self.f3()
		print(result)

obj = Foo() 
v1 = obj.run() # f3 f2 999
print(v1) # None
#4、看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】

class Foo(object):
	
	def f1(self):
		print('f1')

	@staticmethod
	def f2():
		print('f2')
obj = Foo()
obj.f1() # f1
obj.f2() # f2

#Foo.f1() # 报错，类不直接调用普通方法，只调用 静态方法和类方法
Foo.f2() #f2

#5、看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】

class Foo(object):
	
	def f1(self):
		print('f1')

	@classmethod
	def f2(cls):
		print('f2')

obj = Foo() #
obj.f1() #f1
obj.f2() #f2

#Foo.f1() # 报错，类不直接调用普通方法，只调用 静态方法和类方法
Foo.f2() #f2

#6、看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】

class Foo(object):
	
	def f1(self):
		print('f1')
		self.f2()
		self.f3()

	@classmethod
	def f2(cls):
		  print('f2')

	@staticmethod
	def f3():
		  print('f3')


obj = Foo() 
obj.f1() # f1 f2 f3

#7、看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】

class Base(object):
	@classmethod
	def f2(cls):
		  print('f2')

	@staticmethod
	def f3():
		  print('f3')

class Foo(Base):
	def f1(self):
		print('f1')
		self.f2()
		self.f3()

obj = Foo() 
obj.f1() # f1 f2 f3

#8、看代码写结果

class Foo(object):
	def __init__(self, num):
		self.num = num
		
v1 = [Foo for i in range(10)]
v2 = [Foo(5) for i in range(10)]
v3 = [Foo(i) for i in range(10)]

print(v1) # 10个 Foo类 组成的列表，都相同
print(v2) # 10个 Foo(5) 对象内存地址组成的列表，都不同，虽然内容相同，但是他们是不同的对象
print(v3) # 10个Foo类对象内存地址组成的列表，都不同
#9、看代码写结果

class StarkConfig(object):

	def __init__(self, num):
		self.num = num

	def changelist(self, request):
		print(self.num, request)


config_obj_list = [StarkConfig(1), StarkConfig(2), StarkConfig(3)]

for item in config_obj_list:
	print(item.num) # 1 2 3
#10、看代码写结果

class StarkConfig(object):

	def __init__(self, num):
		self.num = num

	def changelist(self, request):
		print(self.num, request)


config_obj_list = [StarkConfig(1), StarkConfig(2), StarkConfig(3)]
for item in config_obj_list:
	item.changelist(666) #1 666 2 666 3 666
# 11、看代码写结果

class Department(object):
	def __init__(self,title):
		self.title = title

class Person(object):
	def __init__(self,name,age,depart):
		self.name = name
		self.age = age 
		self.depart = depart
		
		
d1 = Department('人事部') #
d2 = Department('销售部')

p1 = Person('武沛齐',18,d1)
p2 = Person('alex',18,d1)
p3 = Person('安安',19,d2)

print(p1.name) #武沛齐
print(p2.age) #18
print(p3.depart) # d2 对象的内存地址
print(p3.depart.title) # 销售部
# 12、看代码写结果

class Department(object):
	def __init__(self,title):
		self.title = title

class Person(object):
	def __init__(self,name,age,depart):
		self.name = name
		self.age = age 
		self.depart = depart
	
	def message(self):
		msg = "我是%s,年龄%s,属于%s" %(self.name,self.age,self.depart.title)
		print(msg)
	
	
d1 = Department('人事部') #
d2 = Department('销售部')

p1 = Person('武沛齐',18,d1)
p2 = Person('alex',18,d1)
p1.message() # 我是吴佩琦，年龄18，属于人事部
p2.message() # 我是alex，年龄18，属于销售部