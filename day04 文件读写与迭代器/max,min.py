#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-11 16:08:46
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$


#传入一堆数字，返回一个字典｛'max':x,'min':y｝

def max_min(*args):
	return {'max':max(args),'min':min(args)}

print(max_min(12,14,16,2,1,7,4,55))

#一个函数，传入参数n，返回n的阶乘

def func(num):
	count = 1
	for i in range(num,0,-1):
		count *= i 
	return count
print(func(5))


#返回一个扑克排列表，里边有52项，每一项是一个元祖
#例如[('红心'，2)，('草花'，2),...('黑桃','A')]

def poker():
	huase = ['红心','草花','方片','黑桃']
	shuzi = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
	pokers = []
	for i in range(4):
		for j in range(13):
			temp = (huase[i],shuzi[j])
			pokers.append(temp)
	print(pokers)
	return pokers

poker() 


#九九乘法表

def jiujiu():
	for i in range(1,10):
		for j in range(1,i+1):
			print(f"{j}*{i}={i*j}",end=' ')
			if i ==j:
				print()
jiujiu()