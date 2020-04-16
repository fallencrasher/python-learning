#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-14 21:53:47
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

#模块
#模块的的本质就是 .py 文件，是封装语句的最小单位
#模块注释，建议用多行注释 就是 '''  '''
#模块中出现的变量，for循环，if结构，函数定义等等豆角模块 成员

#模块的运行方式
##1.脚本方式：直接用解释器执行，或者pyCharm中右键执行
##2.模块方式（导入方式）：被其他模块导入，为导入它的模块提供资源(模块中的成员)

#自定义模块
##自定义模块被其他模块导入时，其中的可执行语句会立即执行

#python中，提供一种可以判断自定义模块是开发阶段还是使用阶段
#__name__方法:脚本方式运行时(在本身模块文件里运行)，固定返回 字符串 ‘__mian__’
#			  在别的模块里引用时，则会返回模块名字
print(__name__)

#所以，开发模块时，会在模块里加一个
#在 main() 函数里调用我们开发的方法
def main(): #这个叫测试函数，里边对模块里的方法进行测试
	pass

if __name__ == '__main__':
	main()
	
#自定义模块的使用 我们在外部定义了一个模块 a.py
import a #只有当 a.py 在当前路径或系统模块路径下才可以这么调用

print(a)  #这么这直接打印模块名字，会告诉你模块的存放路径
a.func1() #这个func1()是在 a.py 中有定义的，所以可以如此调用

#内置模块，系统自带
import time
print(time)
print(time.time()) #时间戳，格林威治时间

#系统导入模块的路径
## 内存里：如果已经导入了模块，直接就在内存里调用了
## 系统内置模块目录： ../python/python(版本号)/lib/
## 第三方模块(pip 下载): ../python/python(版本号)/lib/site-packages
## sys 模块，比较重要，嵌入在python中，不在模块列表

##查看 sys.path 内容
# import sys
# print(sys.path)

## 添加 我们写的模块所在路径到系统路径里
# import sys
# sys.path.append(r'自定义模块所在的路径')

##使用相对路径
import sys
import os
###获取文件的绝对路径
print(__file__)

####获取文件的父路径,这行代码，可以获取我们当前的文件所在的目录路径，如果我们的
###自定义模块在项目里的某个目录里，给加到后边就行。
### os.path.dirname(__file__) 是动态的，文件在哪就输出哪，不用记绝对路径
### 要记得区分在 linux 和 windows 下的 \\ 和 /，然而我发现，pycharm里，windows下也可以用 '/'
# print(os.path.dirname(__file__) + '\\模块所在目录')

### 所以一般操作就是
# sys.path.append(os.path.dirname(__file__) + "/模块所在目录")


#倒入模块的多种方式
## import xxx 导入一个模块的所有成员
## import aaa,bbb,ccc  可以一行语句导入多个模块，不推荐
## from xxx import yyy,zzz 导入一个模块某几个成员或方法
## from xxx import * 导入一个模块的所有成员，区别于 import xxx
## from xxx import yyy as pd  为了不出现名称冲突或者简化使用，可以定义别名
## import xxx as x  这么用也可以
## 最好用什么导入什么，要不会占用好多资源

### from xxx impoort *  与  import xxx 的区别
### 当使用 import xxx 
### 我们调用模块内方法的时候，写法是： xxx.abc()
### 当使用 from xxx import *
### 我们调用模块内方法的时候，写法是： abc(),不用加模块名



## 模块的 __all__方法，提供模块内所有可以导入的成员
print(os.__all__)
## 开发时，使用 __all__ ，可以限制可以被导入的成员
## 但是在导入时，只有使用 from xxx import * 的时候有用
## 当使用 import xxx 的时候就管用了
__all__ = ['func1','func2','fucn3']


## 相对导入
## 针对同一个项目里的不同模块之间的导入
## 这个呢及时要知道相对路径的表示方法，比如：
## 当前目录 '.'
## 父目录 '..'
## from ../aa/aa import func
## 就这样，哈哈哈哈

