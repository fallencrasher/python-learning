#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-11 18:07:57
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

#用一行代码构建一个比较复杂且有规律的列表
#列表推导式分为两种：
#1.循环模式：[表达式 for i in iterable] 
#2.筛选模式：[表达式 for i in iterable if 条件]

#比如我们创建一个含有1-10的列表，原来都这么干
l1=[]

for i in range(1,11):
	l1.append(i)

print(l1)

#用列表推倒式
l1 = [i for i in range(1,11)]
print(l1)

#循环模式
##将10以内所有整数的平方写入列表
l2 = [i*i for i in range(1,11)]
print(l2)

##100以内所有的偶数写入列表
l3 = [i for i in range(1,101) if i%2==0]
print(l3)

##从'python1期'到'python100期'写入列表lst
l4 = [f'python{i}期' for i in range(1,101)]
print(l4)

#筛选模式
##30以内能被3整除的数
l5 = [i for i in range(1,31) if i%3==0]
print(l5)

#过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
l = ['wusir', 'laonanhai', 'aa', 'b', 'taibai']
l6 = [i.upper() for i in l if len(i)>=3]
print(l6)

#找到嵌套列表中名字含有两个‘e’的所有名字
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]

l7 = [name for i in names for name in i if name.count('e')==2]
print(l7)

#用列表推导式构建一个列表[2,3,4,5,6,7,8,9,10,'J','Q','k','A']
l8 = [i for i in range(2,11)]+list('JQKA')
print(l8)