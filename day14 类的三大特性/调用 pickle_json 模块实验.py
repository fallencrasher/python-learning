# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-24 22:42:25
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-24 23:11:50
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-24 22:12:19
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

# 调用作业4 模块



class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

def autosave(file,obj,kind):
	import pickle_json
	import sys
	class_name = getattr(pickle_json,kind)
	temp = class_name(file)
	temp.mydump(obj)


def autoload(file,kind):
	import pickle_json
	import sys
	class_name = getattr(pickle_json,kind)
	temp = class_name(file)
	return temp.myload()

python = Course('python', '6 moneth', 21800)
linux = Course('linux', '5 moneth', 19800)
go = Course('go', '4 moneth', 12800)

lst1 = [i for i in range(10)]
str1 = 'i love China'
dic1 = dict.fromkeys(lst1, 100)


# autosave('file_to_test_pickle_json.pickle', python, 'Mypickle')
# autosave('file_to_test_pickle_json.pickle', linux, 'Mypickle')

# autosave('file_to_test_pickle_json.json', lst1,'Myjson')
# autosave('file_to_test_pickle_json.json', str1,'Myjson')
# autosave('file_to_test_pickle_json.json', dic1, 'Myjson')

x = autoload('file_to_test_pickle_json.pickle','Mypickle')
for i in x:
	print(i.name,i.period,i.price)

y = autoload('file_to_test_pickle_json.json','Myjson')
for i in y:
	print(i)