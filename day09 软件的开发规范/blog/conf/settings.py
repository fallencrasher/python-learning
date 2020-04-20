#!/usr/bin/env bash
# -*- coding = utf-8 -*-
# @Author: Fallen
# @Site : https://github.com/fallencrasher/python-learning
# @Time : 2020/4/17 0017 20:20
# @File : settings.py
# @Software : PyCharm

import os

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
USER_MSG = os.path.join(BASE_PATH, 'db', 'user_msg.txt')
USER_NAME = os.path.join(BASE_PATH, 'db', 'user_name.txt')
print(USER_MSG,USER_NAME)

