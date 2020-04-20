#!/usr/bin/env bash
# -*- coding = utf-8 -*-
# @Author: Fallen
# @Site : https://github.com/fallencrasher/python-learning
# @Time : 2020/4/17 0017 21:08
# @File : set_json.py
# @Software : PyCharm

import json


status_dic = {
    'username': None,
    'status': False
}

f = open('login_status.json',encoding='utf-8',mode='a')

json.dump(status_dic,f) ##dump方法接收一个文件句柄，直接将字典转换成json字符串写入文件
f.close() ## json文件也是文件，就是专门存储json字符串的文件。

