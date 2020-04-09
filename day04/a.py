#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-09 18:03:12
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

#a.txt 作业
#将文件内容构建成[{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......]的样子，并计算出总价钱

l = []
l2 = []
l3 = ['name','price','amount']
with open('a.txt',encoding='utf-8',mode='r') as f1:
	for line in f1:
		line.strip().split(" ",2)
		if line.strip().split(" ",2) != ['']:
			dict1=dict.fromkeys(l3)
			dict1['name']=line.strip().split(" ",2)[0]
			dict1['price']=line.strip().split(" ",2)[1]
			dict1['amount']=line.strip().split(" ",2)[2]
			temp = int(dict1['price'])*int(dict1['amount'])
			l2.append(temp)
			l.append(dict1)
	print(l)
	print('总价是{}'.format(sum(l2)))

	