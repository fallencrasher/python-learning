#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-15 23:54:21
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

'''
序列化模块：
序列化模块就是将一个常见的数据结构转化成一个特殊的序列，并且这个特殊的序列还可以反解回去。它的主要用途：文件读写数据，网络传输数据。

Python中这种序列化模块有三种：

    1.json模块 ： （重点）

不同语言都遵循的一种数据转化格式，即不同语言都使用的特殊字符串。（比如Python的一个列表[1, 2, 3]利用json转化成特殊的字符串，然后在编码成bytes发送给php的开发者，php的开发者就可以解码成特殊的字符串，然后在反解成原数组(列表): [1, 2, 3]）

json序列化只支持部分Python数据结构：dict,list, tuple,str,int, float,True,False,None

  

    2.pickle模块：

只能是Python语言遵循的一种数据转化格式，只能在python语言中使用。

支持Python所有的数据类型包括实例化对象。

 

    3.shelve模块：类似于字典的操作方式去操作特殊的字符串（不重要）。

当然序列化模块中使用最多的的就是json模块
'''
import json
# json模块
# JavaScript Object Notation 模块
# json 格式 是重要的数据交换格式
# 在 python 中，只有 set 类型的数据不支持 json 序列化

# python 中的数据，都是结构化数据，也就是可以利用好多方法的数据，数据之间有引用关系
# json 格式的数据，是线性的，他就是最基本的字符串，没有方法可以用，数据之间没有引用关系
# 序列化就是把结构化的数据转化为线性的数据，方便存储和网络传输
# 线性化数据转化为结构化数据的过程就叫反序列化，方便操作

# json: 将数据转换成字符串，用于存储和网络传输
# json模块是将满足条件的数据结构转化成特殊的字符串，并且也可以反序列化还原回去。

#上面介绍我已经说过了，序列化模块总共只有两种用法，要不就是用于网络传输的中间环节，要不就是文件存储的中间环节，所以json模块总共就有两对四个方法：

#    用于网络传输：dumps、loads
#    用于文件写读：dump、load

# 用于网络传输: dumps(序列化)  loads(反序列化)
dic = {'k1':'v1','k2':'v2','k3':'v3'}
str_dic = json.dumps(dic)
print(str_dic,type(str_dic)) #{"k1": "v1", "k2": "v2", "k3": "v3"} <class 'str'>

##注意：json 格式的字符串，字典里的键值对，都是 "" 包裹的
##		由json转过来的字典 ，键值对都是由 '' 包裹的

dic2 = json.loads(str_dic)
print(dic2,type(dic2)) #{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'} <class 'dict'>

## 当然也可以处理嵌套数据类型

lst1 = [1,['a','b','c'],3,{'k1':'v1','k2':'v2'}]

str_lst1 = json.dumps(lst1)
print(str_lst1,type(str_lst1)) #[1, ["a", "b", "c"], 3, {"k1": "v1", "k2": "v2"}] <class 'str'>

lst2 = json.loads(str_lst1)
print(lst2,type(lst2)) #[1, ['a', 'b', 'c'], 3, {'k1': 'v1', 'k2': 'v2'}] <class 'list'>

## 当被处理数据类型是 tuple 时，tuple 会被强制转化成 list

t1 = (1,2,3)
str_t1 = json.dumps(t1)
print(str_t1,type(str_t1)) #[1, 2, 3] <class 'str'>

t2 = json.loads(str_t1)
print(t2,type(t2)) #[1, 2, 3] <class 'list'>

## 当处理数据类型是 set 时，就会报错。。。

# t1 = {1,2,3}
# str_t1 = json.dumps(t1)
# print(str_t1,type(str_t1)) 
# t2 = json.loads(str_t1)
# print(t2,type(t2)) 


# 用于文件读写的： dump(以json格式写入文件)  load(把文件里的json格式字符串读取)
## 通常json 文件就是一次性的写入，一次性的读出，像下边
f = open('json_file.json',encoding='utf-8',mode='w')
dic = {'k1':'v1','k2':'v2','k3':'v3'}
json.dump(dic,f) ##dump方法接收一个文件句柄，直接将字典转换成json字符串写入文件
f.close() ## json文件也是文件，就是专门存储json字符串的文件。


f = open('json_file.json',encoding='utf-8',mode='r')
dic2 = json.load(f)
print(dic2) #{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}


## 如果我们多次的写入或读出，就会报错，就像下边这个

# dic1 = {'name':'oldboy1'}
# dic2 = {'name':'oldboy2'}
# dic3 = {'name':'oldboy3'}
# f = open('序列化',encoding='utf-8',mode='a')
# json.dump(dic1,f)
# json.dump(dic2,f)
# json.dump(dic3,f)
# f.close()
# ​
# f = open('序列化',encoding='utf-8')
# ret = json.load(f)
# ret1 = json.load(f)
# ret2 = json.load(f)
# print(ret)

## 那我们就香一次性写入多个，一次性读出多个怎么办
## 可以借助便于网路传输的json字符串来写入，用for循环读出

dic1 = {'name':'oldboy1'}
dic2 = {'name':'oldboy2'}
dic3 = {'name':'oldboy3'}
f = open('序列化.json',encoding='utf-8',mode='a')
str1 = json.dumps(dic1)
f.write(str1+'\n') # 这样就是把 json格式字符串写入 json 文件
str2 = json.dumps(dic2)
f.write(str2+'\n')
str3 = json.dumps(dic3)
f.write(str3+'\n')
f.close() # 如此做三次就可以多次写入不报错

f = open('序列化.json',encoding='utf-8',mode='r')
lst1 = []
for line in f:
	print(line)
	lst1.append(json.loads(line.strip()))
print(lst1) #[{'name': 'oldboy1'}, {'name': 'oldboy2'}, {'name': 'oldboy3'}]




