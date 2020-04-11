#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-09 15:45:19
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

#文件
'''
文件操作：
1.打开文件
2.对文件句柄进行操作
3.关闭文件

报错原因：
UnicodeDecodeError: 创建文件时使用的编码方式和打开文件的解码方式对不上
SyntaxError: 一般就是windows 路径上的 '\' 没改成 '\\';文件名不能用单独的数字


'''
#绝对路径
#f1 = open(r'D:\programming_with_python\043从零开始学python\day04\文件的读.txt',encoding='utf-8',mode='r')
#相对路径

# 读打开模式
'''
r, rb, r+, r+b 
rb:非文本文件
r：文本文件
'''

# 文本文件 
# read 全读出来 **
f = open('文件的读.txt',encoding='utf-8')
content = f.read()
print(content,type(content))
f.close()

# read(n) 按照字符读取
f = open('文件的读.txt',encoding='utf-8')
content = f.read(5)
print(content)
f.close()

# readline() 按行读取
f = open('文件的读.txt',encoding='utf-8')
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

# readlines() 返回一个列表，列表中的每个元素时原文件的每一行
f = open('文件的读.txt',encoding='utf-8')
l1 = f.readlines()
print(l1)
f.close()

# for 读取 适合大文件的读取 ***
f = open('文件的读.txt',encoding='utf-8')
for line in f:
	print(line)
f.close()

# 非文本文件 rb
f = open('美女.jpg',mode='rb')
content = f.read()
print(content)
f.close()