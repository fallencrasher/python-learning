#!/usr/bin/env bash
# -*- coding = utf-8 -*-
# @Author: Fallen
# @Site : https://github.com/fallencrasher/python-learning
# @Time : 2020/4/9 0009 16:51
# @File : 文件 r+.py
# @Software : PyCharm

#r+ 文件
#r+ 读并追加，先读到全文再写，就是追加
f = open('文件的读.txt',encoding='utf-8',mode='r+')
content = f.read()
print(content)
f.write('人的一切痛苦，本质上都是对自己无能的愤怒')
f.close()

#先写再读，就会从写完的部分之后开始都到末尾
