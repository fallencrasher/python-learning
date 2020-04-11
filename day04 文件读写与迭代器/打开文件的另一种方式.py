#!/usr/bin/env bash
# -*- coding = utf-8 -*-
# @Author: Fallen
# @Site : https://github.com/fallencrasher/python-learning
# @Time : 2020/4/9 0009 17:17
# @File : 打开文件的另一种方式.py
# @Software : PyCharm

#优点1：不用手动关闭
with open('文件的读.txt',encoding='utf-8') as f1:
    print(f1.read())

#优点2：可以一行命令打开多个文件
with open('文件的读.txt',encoding='utf-8') as f1,\
        open('主妇空姐模特联系方式.txt',encoding='utf-8',mode='w') as f2:
    print(f1.read())
    f2.write("sjfowjfoisj")

