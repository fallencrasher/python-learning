#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-25 12:05:34
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

'''
文件存储格式如下：
id，name，age，phone，job
1,Alex,22,13651054608,IT
2,Egon,23,13304320533,Tearcher
3,nezha,25,1333235322,IT

现在需要对这个员工信息文件进行增删改查。
基础必做：
a.可以进行查询，支持三种语法：
select 列名1，列名2，… where 列名条件
支持：大于小于等于，还要支持模糊查找。
示例：
select name, age where age>22
select * where job=IT
select * where phone like 133
# select 查询这个文件
# select name,age where age>20
# select age,name,job where age > 20
# select age,name,job where age < 22
# select age,name,job where age = 22
# select age,name,job where name = 'alex'
# select age,name,job where job = 'IT'
# select age,name,job where phone like '133'
# select * where phone like '133'

进阶选做：

b.可创建新员工记录，id要顺序增加c.可删除指定员工记录，直接输入员工id即可
d.修改员工信息
语法：set 列名=“新的值” where 条件
#先用where查找对应人的信息，再使用set来修改列名对应的值为“新的值”

注意：要想操作员工信息表，必须先登录，登陆认证需要用装饰器完成
其他需求尽量用函数实现
'''
import sys
import re

def auth(f):
	def inner(*args,**kwargs):
		ret = f(*args,**kwargs)
		return ret
	return inner

l = []
with open('staff_info.txt',encoding='utf-8') as f:
	for i in f:
		temp = i.strip().split(',',i.strip().count(','))
		if temp[0].isdigit():
			l.append({'id':temp[0],'name':temp[1],'age':temp[2],'phone':temp[3],'job':temp[4]})
	# print(l)



def search(select,column,where,condition):
	if select=='select':
		tp = column.strip().split(',',column.strip().count(','))
		#l2 = [{age:22,name:alex,job:it},{}]
		l2 = []
		for i in l:
			for key,value in i.items():
				

		






def run():
	pass

if __name__ == '__main__':
	run()