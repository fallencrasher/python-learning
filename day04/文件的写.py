#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-09 16:23:05
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

'''
文件的写
四种模式
w wb w+ w+b
'''

#文件不存在，就可以新建
f = open('文件的写',encoding='utf-8',mode='w')
f.write('随便写点啥')
f.close()

#如果文件存在，先清空源文件内容，再写入新内容
f = open('文件的写',encoding='utf-8',mode='w')
f.write('一山最帅')
f.close()

#wb 非文本
f = open('美女.jpg',mode='rb')
content = f.read()
f.close()

f1 = open('美女2.jpg',mode='wb')
f1.write(content)
f1.close()