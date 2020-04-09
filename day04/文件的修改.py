#!/usr/bin/env bash
# -*- coding = utf-8 -*-
# @Author: Fallen
# @Site : https://github.com/fallencrasher/python-learning
# @Time : 2020/4/9 0009 17:25
# @File : 文件的修改.py
# @Software : PyCharm

'''
修改：
1.以读的方式打开原文件
2.以写的方式创建一个新文件
3.将原文件内容读出来修改成新内容，写入新文件
4.将原文件删除
5.将新文件重命名为原文件
'''

# LOW 版
import os

# 1.
# 2.
# with open('alex自述.txt',encoding='utf-8') as f1,\
#     open('alex自述back.txt',encoding='utf-8',mode='w') as f2:
#     #3.
#     old_content = f1.read()
#     new_content = old_content.replace('alex','SB')
#     f2.write(new_content)
#     #4.
# os.remove('alex自述.txt')
# os.rename('alex自述back.txt','alex自述.txt')

# 进阶版
with open('alex自述.txt', encoding='utf-8') as f1, \
        open('alex自述back.txt', encoding='utf-8', mode='w') as f2:
    # 3.
    for line in f1:
        new_line = line.replace('SB', 'alex')
        f2.write(new_line)

    # 4.
os.remove('alex自述.txt')
os.rename('alex自述back.txt', 'alex自述.txt')

# 有关清空的问题
# 关闭文件句柄，再次以 'w' 模式打开次文件，才会清空，
# 如果，没关闭文件呢，连续写入不会清空文件
with open('文件的读.txt', encoding='utf-8', mode='w') as f1:
    for i in range(9):
        f1.write("快还贷款！")
