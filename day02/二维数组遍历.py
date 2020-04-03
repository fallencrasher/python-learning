# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-03 22:47:20
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-03 23:04:45
l = [(1,2),(3,4),(5,6),(7,8),(9,10)]
for i in l:
    for j in i:
    	print(j)

###升级一下，打印个小时候的九九乘法表
for i in range(1,10):
	for j in range(1,i+1):
		print("{}*{}={}".format(j,i,i*j),end=" ")
		if i == j:
			print()

#5.	[[6,2],[8,4,2],[5,6,1]] 转存到一个新的列表中并排序。
#  结果为[1,2,3,4,5,6,6,8]

l1 = [[6,2],[8,4,2],[5,6,1]]

l2 = []
for i in l1:
	for j in i:
		l2.append(j)

l2.sort()

print(l2)