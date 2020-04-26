# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-25 11:43:07
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-25 12:07:00
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-25 10:54:11
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

# 计算器 fallen 默写版本
# 原版本为 张珵20行版


import re


def calculator(s):
	def two_num_cal(s):  # 这个函数，识别只有俩数的一个表达式，燃火把它算出来
		if re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(2) == '*':
			return float(re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(1)) * float(re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(3))

		if re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(2) == '/':
			return float(re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(1)) / float(re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(3))

		if re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(2) == '+':
			return float(re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(1)) + float(re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(3))

		if re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(2) == '-':
			return float(re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(1)) - float(re.search(r'([+-]?\d+(?:\.\d+)?)([*/+-])([+-]?\d+(?:\.\d+)?)', s).group(3))

	# 这个正则，匹配的是一个单独的数，如果最后只剩一个单独的数，就算完了。不是一个单独的数，又不是俩数的表达式，那就是有括号，要先处理括号
	while not re.search(r'^[+-]?\d+(\.\d+)?$', s):
		while re.search(r'[+-]{2,}', s):
			s.replace(r'++', '+').replace('+-', '-').replace('--',
															'+').replace('-+', '-')  # 去除傻子似的连续加减
		if re.search(r'[(][^()][)]', s):  # 这里找括号，最小括号，循环找，直到找不到括号，找到括号里边的表达式就用递归来算
			s = s[:s.search(r'[(][^()][)]', s).span()[0]] + str(calculator(re.search(r'[(][^()][)]', s).group()[
				1:len(re.search(r'[(][^()][)]', s).group())-1])) + s[s.search(r'[(][^()][)]', s).span(1):]
		if re.search(r'\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?', s):  # 匹配连乘的第一个乘法(除法也是乘法)
			s = s[:re.search(r'\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?', s).span()[0]] + str(two_num_cal(re.search(
				r'\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?', s).group())) + s[re.search(r'\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?', s).span()[1]:]
		if not re.search(r'\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?', s) and re.search(r'[+-]?(\d+(\.\d+)?[+-]\d+(\.\d+)?)', s):  # 匹配连加表达式
			s = s[:re.search(r'[+-]?(\d+(\.\d+)?[+-]\d+(\.\d+)?)', s).span()[0]] + str(two_num_cal(re.search(
				r'[+-]?(\d+(\.\d+)?[+-]\d+(\.\d+)?)', s).group())) + s[re.search(r'[+-]?(\d+(\.\d+)?[+-]\d+(\.\d+)?)', s).span()[1]:]

	return float(s)


print(calculator('1+2'))
