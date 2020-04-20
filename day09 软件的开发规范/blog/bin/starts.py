#!/usr/bin/env bash
# -*- coding = utf-8 -*-
# @Author: Fallen
# @Site : https://github.com/fallencrasher/python-learning
# @Time : 2020/4/17 0017 19:47
# @File : starts.py
# @Software : PyCharm

#需要先将 core 目录加入到 sys.path

'''
这么做可以但是不完美，绝对路径引用会出问题，需要用相对路径的引用
1.项目中的 .py 文件肯定会互相引用
2.在添加引用的时候，最好不要用绝对路径引用，不便于转移，别人就不能用你的程序了
3.要动态得获取路径，这样在哪都可以执行

import sys
sys.path.append(r'D:\programming_with_python\043从零开始学python\day09 软件的开发规范\core')
import src
src.run()
'''

# 接下来，完美做法
# 我们直接把最一开始的目录，大家共同的父目录加入到 sys.path
# import sys
# import os
# __file__ 方法可以动态的获取本文件的路径
# print(__file__)
# print(os.path.dirname(__file__)) #动态的获取父级目录
# print(os.path.dirname(os.path.dirname(__file__))) #那这个获取爷爷级目录
# 以上时思路


import sys

import os

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from core import src

if __name__=='__main__':
    src.run()