#!/usr/bin/env bash
# -*- coding = utf-8 -*-
# @Author: Fallen
# @Site : https://github.com/fallencrasher/python-learning
# @Time : 2020/4/6 0006 21:10
# @File : func02.py
# @Software : PyCharm

# 函數：帶參數的
"""
def 函數名(參數，參數，。。。):
    函數體

调用：
函数名（）
"""

# 求随机数的函数
# Alt + Enter 快速提示
import random


def generate_random(count):  # 形参
    for i in range(count):
        ran = random.randint(1, 20)
        print(ran)


print(generate_random)

# 调用
generate_random(4)


# 求加法的函数
def add(a, b):
    result = a + b
    print(('和：', result))


add(1,2)
