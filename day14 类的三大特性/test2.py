#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-24 16:41:39
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$
import time

class Date(object):
	"""docstring for Date"""
	def __init__(self, year,month,day):
		self.year = year
		self.month = month
		self.day = day
	@classmethod
	def today(cls):
		struct_time = time.localtime()
		print(struct_time.tm_year,'-',struct_time.tm_mon,'-',struct_time.tm_mday)
		# print(time.localtime()) 
		date = cls(struct_time.tm_year,struct_time.tm_mon,struct_time.tm_mday)
		return date
date = Date.today()
print(date.year,date.month,date.day)
