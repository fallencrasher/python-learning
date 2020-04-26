

#继承 -- 解决代码的重复

class Cat(object):
	"""docstring for Cat"""
	def __init__(self, name):
		super(Cat, self).__init__()
		self.name = name
	def eat(self):
		print('%s is eating.' % self.name)
	def drink(self):
		print('%s is drinking.' % self.name)
	def sleep(self):
		print('%s is sleeping.' % self.name)
	def climb_tree(self):
		print('%s is climbing a tree.' % self.name)

class Dog(object):
	"""docstring for Dog"""
	def __init__(self, name):
		super(Dog, self).__init__()
		self.name = name
	def eat(self):
		print('%s is eating.' % self.name)
	def drink(self):
		print('%s is drinking.' % self.name)
	def sleep(self):
		print('%s is sleeping.' % self.name)
	def house_keep(self):
		print('%s is doing the housekeeping.' % self.name)

小白 = Cat('小白')
小白.eat()
小白.drink()
小白.climb_tree()

小黑 = Dog('小黑')
小黑.eat()
小黑.drink()
小黑.house_keep()


# 继承语法

class A:
	pass

class B(A):
	pass

# B继承A，A是父类，B是子类
# A 是父类 基类 超类
# B 是子类
# 子类可以使用父类的静态变量和绑定方法
# 当子类和父类的方法同名，我们只会使用子类自己的方法，而不会去调用父类 了

class Animal(object):
	"""docstring for Animal"""
	def __init__(self, name,food):
		self.name = name
		self.food = food
		self.blood = 100
		self.wise = 100
	def eat(self):
		print('%s is eating %s.' % (self.name,self.food))
	def drink(self):
		print('%s is drinking.' % self.name)
	def sleep(self):
		print('%s is sleeping.' % self.name)

class Dog(Animal):
	"""docstring for Dog"""
	def eat(self):
		self.blood += 100
		Animal.eat(self)
	def house_keep(self):
		print('%s house keeping' % self.name)

class Cat(Animal):
	def eat(self):
		self.wise += 100
		Animal.eat(self)
	def climb_tree(self):
		print('%s is climbing a tree.' % self.name)

xiaobai = Cat('xiaobai','maoliang')
xiaohei = Dog('xiaohei','gouliang')
xiaobai.eat()
xiaohei.eat()
print(xiaobai.__dict__)
print(xiaohei.__dict__)