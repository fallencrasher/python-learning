# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-19 14:36:33
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-19 15:37:29
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-18 16:59:44
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

import re
# 1、匹配整数或者小数（包括正数和负数）

'-?\d+(\.\d+)?'


# 2、匹配年月日日期 格式2018-12-6

'\d{4}([\-|\/|.])\d{1,2}\1\d{1,2}'   # 这里的  \1  是前引用，就引用前边括号里的东西

'\d{4}-\d{1,2}-\d{1,2}'

## 更精确的版本
'[1-9]\d{3}([\-|\/|.])(1[0-2]|0?[1-9])\1([12]\d|3[01]|0?[1-9])'
# 3、匹配qq号
# 首位不是0，长度为 5-10 个数字
'[1-9]\d{4,9}'

# 4、11位的电话号码
# 以 1 开头，第二位 3-9，共11位
'1[3-9]\d{9}'

# 5、长度为8-10位的用户密码 ： 包含数字字母下划线
'^\w{8,10}$'

# 6、匹配验证码：4位数字字母组成的
'[0-9a-zA-Z]{4}'

# 7、匹配邮箱地址
# 下边这俩，不对
# '\w+((-\w+)|(\.\w+))*\@[0-9a-zA-Z]+([\.-+|](0-9a-zA-Z)+)*\.[0-9a-zA-Z]+)'
# '(\w+([+.-]*\w+)*\@\w+([+.-]*\w+)*\.([+.-]*\w+)+'

# 邮箱规则
# @之前必须有内容且只能是字母（大小写）、数字、下划线(_)、减号（-）、点（.）
# @和最后一个点（.）之间必须有内容且只能是字母（大小写）、数字、点（.）、减号（-），且两个点不能挨着
# 最后一个点（.）之后必须有内容且内容只能是字母（大小写）、数字且长度为大于等于2个字节，小于等于6个字节

# [-\w.]+@([-\da-zA-Z]+\.)+[a-zA-Z\d]{2,6}


# 8、从类似

a = '<a>wahaha</a><b>banana</b><h1>qqxing</h1>'
# 这样的字符串中，
# 1）匹配出wahaha，banana，qqxing内容。
# 2）匹配出a,b,h1这样的内容

import re
ret = re.findall('<(\w+)>(\w+)</(\w+)>',a)
print(ret)

# 1)
ret = re.findall('<\w+>(\w+)</\w+>',a)
print(ret)

# 2)
ret = re.findall('<(\w+)>\w+</\w+>',a)
print(ret)




# 9、
x = '1-2*((60-30+(-40/5)(9-25/3+7/399/42998+10568/14))-(-43)/(16-3*2))'
# 1）从上面算式中匹配出最内层小括号以及小括号内的表达式
# '\(-?(\d+[+\-*/]*)*\)'
ret = re.findall('\(-?(?:\d+[+\-*/]*)*\)',x)
ret2 = re.findall('\([^()]+\)',x)  # 这个更好，逻辑就是找到内部不含括号的括号
print(ret) #['(-40/5)', '(9-25/3+7/399/42998+10568/14)', '(-43)', '(16-3*2)']
print(ret2)

# 10、从类似9-25/3+7/399/42998+10568/14的表达式中匹配出从左到右第一个乘法或除法
x = '9-25/3+7/399/42998+10568/14'
ret = re.search('[1-9]\d*[*|/]-?[1-9]\d*',x)
print(ret.group())
## 要是匹配小数呢？
'\d+(\.\d+)+[*|/]-?\d(\.\d+)+'

# 11.匹配一篇英文文章的标题 类似 The Voice Of China
'([A-Z][a-z]+ ?)+'

# 12.匹配一个网址
'(http)?s?:?(\\\\)?(www\.)?(.*?).(com|cn|net)(/.*)*'

# 13.从链家网中匹配出标题，户型和面积，结果如下：
#[('金台路交通部部委楼南北大三居带客厅 单位自持物业', '3室1厅', '91.22平米'), ('西山枫林 高楼层南向两居 户型方正 采光好', '2室1厅', '94.14平米')]


import requests

import re
import json


def getPage(url):
    response = requests.get(url)
    return response.text


def parsePage(s):
    com = re.compile(
        '<a class="title" href=.*?data-el="ershoufang">(?P<title>.*?)</a>.*?<div class="info">(?P<region>.*?)<span>/</span>(?P<style>.*?)<span>/</span>(?P<size>.*?)<span>/</span>(?P<direction>.*?)<span>/</span>(?P<decoration>.*?)</div>', re.S)
    ret = com.finditer(s)
    for i in ret:
    	print(i.group())
    	yield {"title": i.group("title"),"region": i.group("region"),"style": i.group("style"),"size": i.group("size"),"direction": i.group("direction"),"decoration": i.group("decoration"),}


def main():
    url = r'https://lf.lianjia.com/ershoufang/rs%E5%9B%BA%E5%AE%89%E5%8E%BF/' 
    response_html = getPage(url)
    ret = parsePage(response_html)
    f = open('lianjia',mode='a',encoding='utf-8')
    for obj in ret:
    	print(obj)
    	data = json.dumps(obj,ensure_ascii=False)
    	f.write(data + "\n")




if __name__ == '__main__':
    main()


# 14.从类似9-25/3+7/399/42998+10*568/14的表达式中匹配出乘法或除法
s = '9-25/3+7/399/42998+10*568/14'
ret = re.findall('([1-9]\d*[\*|\/][1-9]\d*?)[+\-*/]?',s)
print(ret) #['25/3', '7/3', '99/4', '10*5', '68/1']

