#!/usr/bin/env bash
# -*- coding = utf-8 -*-
# @Author: Fallen
# @Site : https://github.com/fallencrasher/python-learning
# @Time : 2020/4/6 0006 20:47
# @File : func.py
# @Software : PyCharm

import random


def generate_random():
    for i in range(10):
        ran = random.randint(1, 20)
        print(ran)


print(generate_random)  #打印函數在内存裏的地址
print(generate_random())
