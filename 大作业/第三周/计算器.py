# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-19 21:15:41
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-19 21:51:03

import re
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
    while True
	    if '(' in content:
	    	brackets = re.compile('\([^()]+\)')
	    	find_brackets = brackets.findall(content)
	    	brackets_ret = []
	    	for i in find_brackets:

	    		if '\*' in i or '\/' in i:
	    			brackets_ret.append(str(mul_div(i)))
	    		if '\+' in i or '\-' in i:
	    			brackets_ret.append(str(sum_sub(i))
	    			
	    else:



    


if __name__ == "__main__":
    main()
