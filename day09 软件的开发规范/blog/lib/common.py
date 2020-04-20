#!/usr/bin/env bash
# -*- coding = utf-8 -*-
# @Author: Fallen
# @Site : https://github.com/fallencrasher/python-learning
# @Time : 2020/4/17 0017 21:12
# @File : common.py
# @Software : PyCharm

from core import src
import time



def auth(f):
    global status_dic

    def inner(*args, **kwargs):
        if src.status_dic['status']:
            ret = f(*args, **kwargs)
            return ret
        else:
            print('要使用此功能请先登录！')
            time.sleep(1)
            if src.login():
                ret = f(*args, **kwargs)
                return ret
            else:
                print("登陆失败！")

    return inner

