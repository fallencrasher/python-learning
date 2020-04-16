#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-15 23:20:16
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

'''
sys 模块
和python解释器相关的操作
'''

import sys

# 获取命令行方式运行的脚本后面的参数 sys.argv
# sys.argv  这个东西是个列表，他不能调用
# sys.argv[0] 是脚本名称，往后的元素是传入脚本的参数,但是都是字符串类型的
# 这个一般应用于解释器命令行里
# 
# print('脚本名',sys.argv[0])
# print('第一个参数',sys.argv[1])
# print('第二个参数',sys.argv[2])

'''
PS D:\programming_with_python\043从零开始学python\day08 模块> python .\sys模块.py hello world
脚本名 .\sys模块.py
第一个参数 hello
第二个参数 world
'''

# arg1 = int(sys.argv[1])
# arg2 = int(sys.argv[2])
# print(arg1 + arg2)

'''
PS D:\programming_with_python\043从零开始学python\day08 模块> python .\sys模块.py 1 2
脚本名 .\sys模块.py
第一个参数 1
第二个参数 2
3
'''

# 解释器寻找模块的路径
# sys.path
## 如果，我们自己写了模块或者包，想要不通过绝对路径就调用，我们就得把模块所在的路径写入
## sys.path 寻找的那些个目录里
## 先看看 sys.path 里有啥
print(sys.path)

### 返回一个列表，包含所有可以直接调用模块的路径，第一个目录是执行命令的脚本所在目录，当我们编写程序，可以直接调用同意目录下的模块
### 但是这是临时的，我们关了文件，sys.path 里就没有这个目录了，
### 我们可以把包含我们写好的模块的目录，写入 sys.path,这样任何时候都可以直接调用了
'''
['D:\\programming_with_python\\043从零开始学python\\day08 模块', 'C:\\Program Files (x86)\\Python3.8\\python38.zip', 'C:\\Program Files (x86)\\Python3.8\\DLLs', 'C:\\Program Files (x86)\\Python3.8\\lib', 'C:\\Program Files (x86)\\Python3.8', 'C:\\Users\\Wang Yishan\\AppData\\Roaming\\Python\\Python38\\site-packages', 'C:\\Program Files (x86)\\Python3.8\\lib\\site-packages']
'''
## 将目标目录写入 sys.path
# import os
# sys.path.append(os.path.dirname(__file__))


# 返回系统已经加载的莫亏啊 sys.modules
print(sys.modules)

## 说点别的，怎么判断，这些个内置的函数方法，调用的时候要不要加括号呢？
## 如果，我们调用的内置变量，是个方法或者类，就要加()才行
## 如果，我们调用的内置变量，是一个属性，就不用了
## 那怎么判断调用的是个啥呢？ 简单的方法就是在pycharm里，如果提示里 提示这个是个 'v' 的，就是属性，不用加括号，其他的都加



sys.argv           命令行参数List，第一个元素是程序本身路径
sys.exit(n)        退出程序，正常退出时exit(0),错误退出sys.exit(1)
sys.version        获取Python解释程序的版本信息
sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值  ***
sys.platform       返回操作系统平台名称