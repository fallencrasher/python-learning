#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-09 08:31:15
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

import time

person_list = ['alex','wupeiqi','yuanhao','linhaifeng','zsc']

def ask(person_list):
	print("-"*30)
	if len(person_list)==0:
		return 'no one knows'

	person=person_list.pop(0)
	if person == "linhaifeng":
		return 'linhaifeng says, i know'

	print('hey,{},where is...'.format(person))
	print("{}说我不知道，我帮你问问{}".format(person,person_list))
	res = ask(person_list)
	print("{}问的见过是 {}".format(person,res))
	return res

result = ask(person_list)
print(result)