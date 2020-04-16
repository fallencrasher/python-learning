#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-16 14:02:34
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

'''
pickle 模块,将 python 所有数据类型都转化为字节(二进制)(串)，或者反序列化
由于对所有数据类型都有效，所以pickle可以完全保留python的数据类型
但是由于不能与其他语言公用，所以很垃圾，重点还是 json
'''
# pickle 模块的方法与 json 的操作一样
# 都是用 dumps loads  dump load
import pickle
dic = {'k1':'v1','k2':'v2','k3':'v3'}
str_dic = pickle.dumps(dic)
print(str_dic)  # bytes类型
dic2 = pickle.loads(str_dic)
print(dic2)    #字典

# 还可以序列化对象
import pickle

def func():
	print(666)
ret = pickle.dumps(func)
print(ret,type(ret)) #b'\x80\x04\x95\x15\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x04func\x94\x93\x94.' <class 'bytes'>

f1 = pickle.loads(ret)
print(f1,type(f1)) #<function func at 0x015F94A8> <class 'function'>
f1()

# 文件写入读出
dic = {(1,2):'oldboy',1:True,'set':{1,2,3}}
f = open('pickle序列化.pickle',mode='wb')
pickle.dump(dic,f)
f.close()

with open('pickle序列化.pickle',mode='rb') as f1:
	dic2 = pickle.load(f1)
	print(dic2)


# pickle 序列化可以存储多个数据到一个文件里
dic1 = {'name':'oldboy1'}
dic2 = {'name':'oldboy2'}
dic3 = {'name':'oldboy3'}
f=open('pick多数据.pickle',mode='wb')
pickle.dump(dic1,f)
pickle.dump(dic2,f)
pickle.dump(dic3,f)
f.close()
f=open('pick多数据',mode='rb')
while True:
    try:
        print(pickle.load(f))
    except EOFError:
        break
f.close()


