#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-08 16:03:08
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

a = "外部定义的变量"
list1 = ['外部定义的变量']
def func():
    print(a)
    print(list1)
def func1():
    global a 
    #我们在函数里声明将要修改全局变量，那我们在函数内的修改不需要返回值就可以改变外部变量
    a = a + "hhhhh"
    list1.append(a)
    print(a)
    print(list1)

def func2():
    #如果我们声明要使用全局变量，我们函数里用的各种变量都随便是什么名字，跟外边都没关系
    a = "莫哈哈"
    list1 = [1,2,3,4]
    print(a)
    print(list1)
 

func()  # 这个打印出来的是 "外部定义的变量"
func1() # 这个打印出来的是 "外部定义的变量hhhhh"
func2()  # 这个打印出来的是 "莫哈哈"
