# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-21 19:35:30
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-21 19:43:43
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-15 22:43:13
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

'''
os 模块：和底层操作系统相关的操作被封装在这个模块中
这里只有一部分，也不说是常用的，
当我们有啥需求，就去百度，
去菜鸟教程网站，有的是，我也只是在给自己做笔记

'''

import os

# 和文件操作相关
## 删除文件
#os.remove(r'包含文件名的文件路径')

## 重命名
#os.rename(r'包含文件名的文件路径','改后文件名')

# 目录相关
##删除目录，必须是空目录
#os.removedirs(r'路径')

# 自动遍历 一个目录下的所有目录和文件
# 返回一个生成器，每次生成一个列表，列表里的元素是一些元组，这些元组，每一个都包含三个元素
# 分别为 路径名  路径下的所有子路径  路径下的文件
g = os.walk('D:\programming_with_python\043从零开始学python')
for i in g:
	path,dir_lst,file_lst = i
	print(path,file_lst)


## 使用 shutil 模块可以删除含有内容的目录
# import shutil
# shutil.rmtree(r'路径')

## 和路径相关的操作，被封装到另一个子模块 os.path 中
### 取文件或目录的父目录名
res = os.path.dirname(r'D:\programming_with_python\043从零开始学python\day08 模块\os模块.py')
print(res) #D:\programming_with_python\043从零开始学python\day08 模块
### 用 os.path.dirname() 配合 __file__方法，可以获得文件的绝对路径,不带文件名
res = os.path.dirname(__file__)
print(res)

### 取文件名(路径的最后一部分)
res = os.path.basename(r'D:\programming_with_python\043从零开始学python\day08 模块\os模块.py')
print(res) #os模块.py

res = os.path.basename(r'D:\programming_with_python\043从零开始学python\day08 模块')
print(res) #day08 模块

### 把路径名和文件名分开(路径的最后一部分和其父目录分开)，返回一个含有两个元素的元组
res = os.path.split(r'D:\programming_with_python\043从零开始学python\day08 模块\os模块.py')
print(res) #('D:\\programming_with_python\\043从零开始学python\\day08 模块', 'os模块.py')

res = os.path.split(r'D:\programming_with_python\043从零开始学python\day08 模块')
print(res) #('D:\\programming_with_python\\043从零开始学python', 'day08 模块')

### 拼接路径,会自动加上 '\'
res = os.path.join('D:\\','aaa','bbb','ccc')
print(res) #D:\aaa\bbb\ccc


### 获取一个路径的绝对路径，
#### 如果我给的相对路径是 有个 '/' 开头的，他会默认你在盘符的根目录下，然后直接加上盘符名称返回
res = os.path.abspath(r'/day08 模块')
print(res) #D:\day08 模块
#### 如果我给的相对路径没有 '/' 开头，默认是当前目录，返回绝对路径
res = os.path.abspath(r'day08 模块')
print(res) #D:\programming_with_python\043从零开始学python\day08 模块\day08 模块

## 判断
### 判断是否是绝对路径,如果给的路径不存在就会报错
res = os.path.isabs(r'D:\programming_with_python\043从零开始学python\day08 模块\day08 模块')
res2 = os.path.isabs(r'os模块.py')
print(res) #True
print(res2) #False

### 判断是否是个文件
res = os.path.isfile(r'D:\programming_with_python\043从零开始学python\day08 模块\day08 模块')
res2 = os.path.isfile(r'os模块.py')
print(res) #False
print(res2) #True

### 判断是否是个路径
os.path.isdir(os.path.dirname(__file__)) #True

### 判断路径是否存在
res = os.path.exists(r'D:\programming_with_python\043从零开始学python\day08 模块')
print(res) #True

'''
***************************************************************
					最后，看一下os模块的总结
***************************************************************							
'''
# 当前执行这个python文件的工作目录相关的工作路径
os.getcwd() #(pwd) 获取当前工作目录，即当前python脚本工作的目录路径  ** 
os.chdir("dirname")  #(cd ) 改变当前脚本工作目录；相当于shell下cd  **
os.curdir  返回当前目录: ('.')  **
os.pardir  获取当前目录的父目录字符串名：('..') **
​
# 和文件夹相关 
os.makedirs('dirname1/dirname2') #(mkdir -p )   可生成多层递归目录  ***
os.removedirs('dirname1') #(rm -r) 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推 ***
os.mkdir('dirname')    #(mkdir) 生成单级目录；相当于shell中mkdir dirname ***
os.rmdir('dirname')    #(rmdir) 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname ***
os.listdir('dirname')  #(ls -al)  列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印 **
​os.copy('olddir','newdir/newfile') #(cp olddir newdir) #oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
# 和文件相关
os.remove()  删除一个文件  ***
os.rename("oldname","newname")  重命名文件/目录  ***
os.stat('path/filename')  获取文件/目录信息 **
​shutil.copytree("olddir","newdir")   #复制文件夹： olddir和newdir都只能是目录，且newdir必须不存在
shutil.move("oldpos","newpos")    #移动文件（目录）

# 和操作系统差异相关
os.sep    #输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/" *
os.linesep    #输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n" *
os.pathsep    #输出用于分割文件路径的字符串 win下为;,Linux下为: *
os.name    #输出字符串指示当前使用平台。win->'nt'; Linux->'posix' *和执行系统命令相关
# os.system("bash command")  #运行shell命令，直接显示  **
# os.popen("bash command").read()  # 运行shell命令，获取执行结果  **
os.environ  获取系统环境变量  **
​
#path系列，和路径相关
os.path.abspath(path) #返回path规范化的绝对路径  ***
os.path.split(path) #将path分割成目录和文件名二元组返回 ***
os.path.dirname(path) #返回path的目录。其实就是os.path.split(path)的第一个元素  **
os.path.basename(path)# 返回path最后的文件名。如何path以'/'或'\\' 结尾，那么就会返回空值，即os.path.split(path)的第二个元素。 **
os.path.exists(path)  #如果path存在，返回True；如果path不存在，返回False  ***
os.path.isabs(path)  #如果path是绝对路径，返回True  **
os.path.isfile(path) # 如果path是一个存在的文件，返回True。否则返回False  ***
os.path.isdir(path)  #如果path是一个存在的目录，则返回True。否则返回False  ***
os.path.join(path1[, path2[, ...]])  #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略 ***
os.path.getatime(path)  #返回path所指向的文件或者目录的最后访问时间  **
os.path.getmtime(path)  #返回path所指向的文件或者目录的最后修改时间  **
os.path.getsize(path) #返回path的大小 ***

# stat 结构:
# st_mode: inode 保护模式
# st_ino: inode 节点号。
# st_dev: inode 驻留的设备。
# st_nlink: inode 的链接数。
# st_uid: 所有者的用户ID。
# st_gid: 所有者的组ID。
# st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
# st_atime: 上次访问的时间。
# st_mtime: 最后一次修改的时间。
# st_ctime: 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。

