#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-11 20:00:32
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

#内置函数 68个
#这个文件里边的，了解就好
#次重要的内置函数

# eval() 剥去字符串外衣，把字符串当代码运行,这个东西很危险据说，
# 在网络传输的 str input 输入的时候，sql注入的时候绝对不用
# eval()是有返回值的
s1 = '1 + 3'
print(s1)
print(eval(s1))

s = '{"name":"alex"}'
print(s,type(s))
#print(dict(s)) #会报错
print(eval(s),type(eval(s)))

# exec() 与eval()几乎一样，处理代码流的
msg = '''
for i in range(10):
	print(i)
'''
print(msg)
exec(msg)

#hash() 获取一个对象的哈希值
# 不可变对象才具有哈希值

print(hash('owfjfosjfio'))

# help() 获取方法对象的使用方法
print(help(str))
print(help(str.upper))

# callable() 判断一个对象是否可调用,就是能不能加括号()
s1 = 'jsofjiofjio'
print(callable(s1))
def func():
	pass
print(callable(func))

# int() 将一个字符串或数字转换为整型

# float() 将整数或字符串转换成浮点数

# complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数
print(complex(1,2))

# bin() 将十进制转化为二进制字符串并返回
print(bin(10),type(bin(10)))  # 0b1010 <class 'str'>

# oct() 将十进制转化为八进制字符串并返回
print(oct(10),type(oct(10)))  # 0o12 <class 'str'>

# hex() 将十进制转换为十六进制字符串并返回
print(hex(10),type(hex(10)))  # 0xa <class 'str'>

# divmod() 计算除数与被除数的结果，返回一个包含商和余数的元组(a // b, a % b)
print(divmod(7,2))  # (3, 1)

# round() 保留浮点数的小数位数，默认保留整数
print(round(7/3,2))
print(round(7/3))
print(round(3.1415926,3))

# pow() 求x**y次幂，三个参数为 x**y 的结果对 z 取余(取对数)
print(pow(2,3))
print(pow(2,3,3))

# bytes() 用于不同编码之间的转化
s = '你好'
bs = s.encode('utf-8')
print(bs)
s1 = bs.decode('utf-8')
print(s1)
bs = bytes(s,encoding='utf-8')
print(bs)
b = '你好'.encode('gbk')
b1 = b.decode('gbk')
print(b1.encode('utf-8'))

# ord() 输入字符找该字符的编码的位置
print(ord('a'))
print(ord('中'))

# chr 输入位置数字找出其相对应的字符
print(chr(97))
print(chr(20013))

# repr() 返回一个对象的 string 形式，原形毕露
#%r  原封不动的写出来
name = 'taibai'
print('我叫%r'%name)

# repr 原形毕露
print(repr('{"name":"alex"}'))
print('{"name":"alex"}')

# all() 可迭代对象中全是 True 才是 True
print(all([1,2,True,0]))

# any() 可迭代对象中，有一个True 就是 True
print(any([1,'',0]))

