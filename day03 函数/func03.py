#!/usr/bin/env bash
# -*- coding = utf-8 -*-
# @Author: Fallen
# @Site : https://github.com/fallencrasher/python-learning
# @Time : 2020/4/6 0006 21:35
# @File : func03.py
# @Software : PyCharm

"""
登录函数
"""

def login(username,password):
    uname = 'admin123'
    pwd = '112233'
    for i in range(3):
        if username == uname and password == pwd:
            print("登录成功！")
            break
        else:
            print('用户名或密码错误！')
            username = input("用户名：")
            password = input("密码：")
    else:
        print("account locked!")
        break

username = input("用户名：")
password = input("密码：")
# 调用函数
login(username,password)