#!/usr/bin/env bash
# -*- coding = utf-8 -*-
# @Author: Fallen
# @Site : https://github.com/fallencrasher/python-learning
# @Time : 2020/4/9 0009 17:04
# @File : 文件操作其他功能.py
# @Software : PyCharm

'''
对文件句柄操作的功能
read() readline() readlines() write()
'''

#tell() 告诉你光标的位置，代为字节
f = open('文件的读.txt',encoding='utf-8')
print(f.tell())
content = f.read()
print(f.tell())
f.close()

#seek() 调整光标位置
f = open('文件的读.txt',encoding='utf-8')
print(f.seek(7))
content = f.read()
print(f.tell())
f.close()

#flush() 强制刷新,保存
f = open('文件的其他功能.txt',encoding='utf-8',mode='w')
f.write('sdfsfjsofjsdfj')
f.flush()
f.close()
