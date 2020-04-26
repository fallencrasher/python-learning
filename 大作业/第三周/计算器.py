# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-19 21:15:41
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-24 12:32:29

import re
from functools import reduce
def sum_sub(exp):
	if '+' in exp:
		return float(exp.strip()[0]) + float(exp.strip()[2])
	if "-" in exp:
		return float(exp.strip()[0]) - float(exp.strip()[2])

def mul_div(exp):
	if '*' in exp:
		return float(exp.strip()[0]) * float(exp.strip()[2])
	if "/" in exp:
		return float(exp.strip()[0]) / float(exp.strip()[2])




def main():

	content = input('输入表达式：').strip()
	while '(' in content:
		
		brackets = re.compile('\([^()]+\)')
		find_brackets = brackets.findall(content)
		
		for i in find_brackets:
			while '\*' in i or '\/'  in i:
				#i = i.replace(re.search('\d+(\.\d+)?[*/]\d+(\.\d+)?',i).group(),str(mul_div(re.search('\d+(\.\d+)?[*/]\d+(\.\d+)?',i).group())))
				content = content.replace(i,i.replace(re.search('\d+(\.\d+)?[*/]\d+(\.\d+)?',i).group(),str(mul_div(re.search('\d+(\.\d+)?[*/]\d+(\.\d+)?',i).group()))))

			while '\+' in i or '\-' in i:
				#plus_min = re.compile('')
				#i = i.replace(re.search('\d+(\.\d+)?[+-]\d+(\.\d+)?',i).group(),str(mul_div(re.search('\d+(\.\d+)?[+-]\d+(\.\d+)?',i).group())))
				content = content.replace(i,i.replace(re.search('\d+(\.\d+)?[+-]\d+(\.\d+)?',i).group(),str(mul_div(re.search('\d+(\.\d+)?[+-]\d+(\.\d+)?',i).group()))))
	
	while '\*' in content or '\/'  in content:
		#ret = re.findall('[+-]?\d+(?:\.\d+)?',content)
		content = content.replace(i,i.replace(re.search('\d+(\.\d+)?[*/]\d+(\.\d+)?',i).group(),str(mul_div(re.search('\d+(\.\d+)?[*/]\d+(\.\d+)?',i).group()))))

	while re.search('[+-]?\d+(?:\.\d+)?',content):
		ret = re.search('[+-]?\d+(?:\.\d+)?',content).group()
		content = reduce(lambda a,b:float(a)+float(b),ret)
	
	print(content)
	
	


if __name__ == "__main__":
	main()
