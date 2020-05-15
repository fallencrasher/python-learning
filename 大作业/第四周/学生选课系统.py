# 学生选课系统
import pickle
import os
import hashlib
import time
import sys

class Admin(object):
	"""docstring for Admin"""
	def __init__(self, name):
		super(Admin, self).__init__()
		self.name = name
		self.auth = 'admin'
	
	def 创建课程(self):
		with open('courses','ab') as f:
			new_course = input('请输入新课程信息(课程名称，价格，周期，老师)。用","隔开。\n:').strip().split(',',3)
			temp = Course(*new_course)
			pickle.dump(temp,f)
	def 创建学生账号(self):
		with open('students','ab') as f:
			new_student = input('请输入学生姓名及学号，用“,”隔开。\n:').strip().split(',',2)
			temp = Student(*new_student)
			pickle.dump(temp,f)
	def __loadfile(self,file):
		with open(file,mode='rb') as f:
			while True:
				try:
					yield pickle.load(f)
				except EOFError:
					break
	def 已有课程(self):
		temp2 = self.__loadfile('courses')
		for i in temp2:
			print(i.name,i.price,i.period,i.teacher)

	def 查看所有学生(self):
		temp = self.__loadfile('students')
		for i in temp:
			print(i.name,i.id,i.course)

	#def overview_all(self):


class Student(object):
	"""docstring for Student"""
	def __init__(self, name,id):
		super(Student, self).__init__()
		self.name = name
		self.id = id
		self.course = []
		self.auth = 'student'

	def __loadfile(self,file):
		with open(file, mode='rb') as f:
			while True:
				try:
					yield pickle.load(f)
				except EOFError:
					break

	def 选课(self):


		# target_dir = os.path.join(os.path.curdir , self.name)
		# if not os.path.exists(target_dir):
		# 	os.mkdir(target_dir)
		# else:
		choice = input('请输入你要选择的课程名称:').strip()
		choice = choice.split(',',choice.count(','))
		# target_file = os.path.join(target_dir,self.name + "courses")
		with open('courses.bak','wb') as f2:
			b = self.__loadfile('students')
			for i in b:
				if i.name==self.name:
					i.course.append(choice)
					pickle.dump(i,f2)
					self.course.append(choice)
				else:
					pickle.dump(i,f2)
		os.remove('courses')
		os.rename('courses.bak','courses')



	def 查看可选课程(self):
		temp = self.__loadfile('courses')
		for i in temp:
			print(i.name,i.price,i.period,i.teacher)

	def 查看已选课程(self):
		print(self.course)

class Course(object):
	"""管理员创建课程用类"""
	def __init__(self, name,price,period,teacher):
		super(Course, self).__init__()
		self.name = name
		self.price = price
		self.period = period
		self.teacher = teacher



def register():
	'''
	注册
	'''
	count = 0
	while count < 4:
		username = input('请输入用户名(不是学号)(管理员请输入 admin)：')
		password = input('请输入密码(长度要在 6~14 个字符之间)：')
		if not username.strip().isdigit():
			with open('user_msg.txt', encoding='utf-8', mode='r') as f1, open('user_msg.txt', encoding='utf-8',
																			   mode='a') as f2:
				lst1 = []
				for line in f1:
					lst1.append(line.strip().split('|')[0])
				if username.strip() not in lst1 and (len(password.strip()) >= 6 and len(password.strip()) <= 14):

					md5 = hashlib.md5()
					md5.update(username.encode('utf-8'))
					md5.update(password.encode('utf-8'))
					ret = md5.hexdigest()
					f2.write(username + '|' + ret + '\n')
					# f2.write(username + '\n')
					print(f'{username},恭喜您，注册成功！即将返回主界面！请登陆！')
					time.sleep(0.5)
					return True
				elif username.strip() in lst1:
					count += 1
					print(f'用户名已存在！请重新注册。你还有{3 - count}次注册机会。')
					time.sleep(0.5)
				elif len(password.strip()) < 6 and len(password.strip()) > 14:
					count += 1
					print(f'密码不符合要求！密码长度要在 6~14 个字符之间。请重新注册。你还有{3 - count}次注册机会。')
		else:
			count += 1
			print(f'用户名不符合要求。只能含有字母或者数字，不能含有特殊字符。请重新注册。你还有{3 - count}次注册机会。')


def login():
	'''
	登录
	'''

	count = 0
	while count < 4:
		username = input('请输入用户名：')
		password = input('请输入密码：')

		md5 = hashlib.md5()
		md5.update(username.encode('utf-8'))
		md5.update(password.encode('utf-8'))
		ret = md5.hexdigest()
		with open('user_msg.txt', encoding='utf-8', mode='r') as f2:
			for line in f2:
				if line.strip().split('|')[1] == ret:
					print('登陆成功！')
					return username
			else:
				count += 1
				print(f'用户名或密码错误！请重新登陆！你还有{3 - count}次机会。')
				time.sleep(0.6)

def loadfile(file):
	with open(file,mode='rb') as f:
		while True:
			try:
				yield pickle.load(f)
			except EOFError:
				break

def run():


	while True:
		judge = input('欢迎来到选课界面：请选择要进行的操作：\n1.注册 2.登录 3.退出：').strip()
		if judge=='1' or judge=='注册':
			register()
		elif judge=='2' or judge=='登录':
			uid = login()
			if uid=='admin':
				with open('admin','rb') as f:
					admin = pickle.load(f)
				while True:
					judge = input('管理员，您好！请选择操作：\n创建课程\n创建学生账号\n已有课程\n查看所有学生\n退出\n:').strip()
					if judge=='退出':
						print('回到初始界面！')
						time.sleep(0.5)
						break
					elif hasattr(admin,judge):
						if callable(getattr(admin,judge)):
							getattr(admin,judge)()
							time.sleep(0.5)
					else:
						print('输入错误')
						time.sleep(0.5)
			else:

				temp = loadfile('students')
				for i in temp:
					if i.name==uid:
						student = i
						break
				while True:
					judge = input(f'{student.name}同学，您好！请选择操作：\n选课\n查看可选课程\n查看已选课程\n退出\n:').strip()
					if judge == '退出':
						print('回到初始界面！')
						time.sleep(0.5)
						break
					elif hasattr(student, judge):
						if callable(getattr(student, judge)):
							getattr(student, judge)()
							time.sleep(0.5)
					else:
						print('输入错误')
						time.sleep(0.5)
		elif judge=='3' or judge=='退出':
			print('退出程序！')
			break









if __name__ == '__main__':
	run()