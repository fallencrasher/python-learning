#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-08 17:23:47
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$


# 内部函数
# 1.内部函数可以访问外部函数的变量
# 2.内部函数可以修改外部函数可变类型的变量
# 3.内部函数在无声明情况下不可修改外部函数的不可变类型变量
# 4.这个声明 是 nonlocal,要加在内部函数里
# 5.内部函数修改全局的不可变类型变量，需要在内部函数内部声明 global
# locals()函数返回一个字典，包含当前函数内声明的内容有什么
# globals()函数返回一个字典，包含当前的全局变量有什么
# 调用外部函数


m = 2020


def func():
    # 声明变量,都是局部变量
    n = 100
    list1 = [1, 2, 3, 4]

    # 内部函数
    # 在函数内部声明另外一个函数
    def inner_func():
        # 声明要对全局变量m进行修改
        global m
        # 声明要对外部函数不可变类型变量n进行修改
        nonlocal n
        # 对list1里面的元素进行加5操作
        for index, i in enumerate(list1):
            list1[index] = i+n

        list1.sort()
        n += 1
        m += 1
    # 调用内部函数
    inner_func()
    print(list1)
    print(n)
    print(m)
    print(locals())  # locals()函数返回一个字典，包含当前函数内声明的内容有什么
    print(globals())  # globals()函数返回一个字典，包含当前的全局变量有什么


# 调用外部函数
func()
