# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-24 09:56:32
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-24 09:56:32
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-18 15:34:31
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

import re
# ret = re.findall('\d+','19740ash93010uru')
# print(ret)   # ['19740', '93010']

# ret = re.search('\d+','19740ash93010uru')
# print(ret)  # 变量，<re.Match object; span=(0, 5), match='19740'>
# if ret:
#     print(ret.group())  #19740

# 一个现象 - 分组()
# findall 还是按照完整的正则进行匹配,只是显示括号里匹配到的内容
ret = re.findall('9(\d)\d','19740ash93010uru')
print(ret) #['7', '3'],用 '9(\d)\d'去匹配，然后返回()里的内容

# search 还是按照完整的正则进行匹配,显示也显示匹配到的第一个内容,但是我们可以通过给group方法传参数
# 来获取具体文组中的内容
ret = re.search('9(\d)(\d)','19740ash93010uru')
print(ret)  # 变量，<re.Match object; span=(1, 4), match='974'>
if ret:
    print(ret.group())  #974
    print(ret.group(0)) #974
    print(ret.group(1))  #7
    print(ret.group(2))  #4

# findall
    # 取所有符合条件的,优先显示分组中的
    ## re.S 参数，findall 的 re.S 参数会让正则里的 '.' 匹配所有东西，包括换行符
# search 只取第一个符合条件的,没有优先显示这件事儿
    # 得到的结果是一个变量
        # 变量.group() 的结果 完全和 变量.group(0)的结果一致
        # 变量.group(n) 的形式来指定获取第n个分组中匹配到的内容

# 为什么在search中不需要分组优先 而在findall中需要?

# 加上括号 是为了对真正需要的内容进行提取
ret = re.findall('<\w+>(\w+)</\w+>','<h1>askh930s02391j192agsj</h1>')
print(ret)  #['askh930s02391j192agsj'] #去掉了两端的<h1> </h1>


# search
ret = re.search('<(\w+)>(\w+)</\w+>','<h1>askh930s02391j192agsj</h1>')
print(ret.group())  #<h1>askh930s02391j192agsj</h1>
print(ret.group(1)) #h1
print(ret.group(2)) #askh930s02391j192agsj
#print(ret.group(3)) # 这个就会报错了，没有group(3)

# 为什么要用分组,以及findall的分组优先到底有什么好处
exp = '2-3*(5+6)'
# a+b 或者是a-b 并且计算他们的结果
# ret = re.search('\d+[+]\d+',exp)
# print(ret)
# a,b = ret.split('+')
# print(int(a)+int(b))


# ret = re.search('(\d+)[+](\d+)',exp)
# print(ret)
# print(ret.group(1))
# print(ret.group(2))
# print(int(ret.group(1)) + int(ret.group(2)))


# with open('douban.html',encoding='utf-8') as f:
#     content = f.read()
# ret = re.findall('<span class="title">(.*?)</span>(?:\s*<span class="title">.*?</span>)?',content)
# print(ret)
# 如果我们要查找的内容在一个复杂的环境中
# 我们要查的内容并没有一个突出的 与众不同的特点 甚至会和不需要的杂乱的数据混合在一起
# 这个时候我们就需要把所有的数据都统计出来,然后对这个数据进行筛选,把我们真正需要的数据对应的正则表达式用()圈起来
# 这样我们就可以筛选出真正需要的数据了



# 什么是爬虫
    # 通过代码获取到一个网页的源码
    # 要的是源码中嵌着的网页上的内容   -- 正则表达式
# import requests
# ret = requests.get('https://baidu.com')
# a = ret.content.decode('utf-8')
# open('a.html',encoding='utf-8',mode='a').write(a)
# print(a,type(a))

# 分组和findall的现象
    # 为什么要用分组?
        # 把想要的内容放分组里
# 如何取消分组优先
    # 如果在写正则的时候由于不得已的原因 导致不要的内容也得写在分组里
    # (?:)  取消这个分组的优先显示



# split 匹配一个字符窜，以该字符串为分隔符，将整个字符串分成n个部分
# 并返回一个分好的列表，类似与字符串的 .split()方法
ret = re.split('\d+','hhhhhhh2222xxxxxx')
print(ret) #['hhhhhhh', 'xxxxxx']

## 用分组保留 一部分匹配到的分隔符字符串，但仍然分割整个字符串
ret = re.split('\d(\d{2})\d','hhhhhhh2222xxxxxx')
print(ret)  #['hhhhhhh', '22', 'xxxxxx']


# sub 替换，把匹配到的东西用别的东西替换
ret = re.sub('\d+','H','fojfio7423sjfwij374289sjdfo')
print(ret)  #fojfioHsjfwijHsjdfo

## re.sub() 还有个参数，可以指定替换次数，比如传入 1，就是只把第一次匹配到的替换了
## 别的都不动
ret = re.sub('\d+','H','fojfio7423sjfwij374289sjdfo',1)
print(ret)   #fojfioHsjfwij374289sjdfo


# subn 功能与sub 类似，但是返回一个元组，('替换后的字符串',替换次数)
ret = re.subn('\d+','H','fojfio7423sjfwij374289sjdfo')
print(ret) #('fojfioHsjfwijHsjdfo', 2)

# match 匹配以。。。开头的字符串，其他的功能跟 search 一样
# match 用来规定，你输入的字符串必须是这样的
ret = re.match('\d+','sfoejw12332533sfojw32435')
print(ret) #None

ret =  re.match('\d+','123sfoejw12332533sfojw32435')
print(ret) #<re.Match object; span=(0, 3), match='123'>
print(ret.group())  #123

# compile
# 如果一个正则表达式要被使用多次
# 我们可以先用 ret =re.compile('\d+') 来预编译正则
# 这样不仅可以节省写代码时间，也节省程序重复识别正则表达式的时间
# 但是如果一个正则，就用一次，那 compile 就不能帮助节省时间
ret = re.compile('\d+')  # 这个就类似 hashlib.md5() 的使用方法
res1 = ret.search('23425jdfsjfo')
res2 = ret.findall('23408dsjfos')
print(res1.group())
print(res2)

# finditer -- 节省空间
#
ret = re.finditer('\d+','3234dsjfoj4234')
for i in ret:
    print(i.group())


# compile 与 finditer 的配合使用，既节省时间又节省空间（内存）

ret = re.compile('\d+')
res = ret.finditer('284293djsfsjl239048sdfjkj')
for i in res:
    print(i.group())


# 分组命名 (?P<名字>正则)   (?P=名字)    (\1)(前引用)
# ret.group('名字')

# import re
# ret = re.search('\d(\d)\d(\w+?)(\d)(\w)\d(\d)\d(?P<name1>\w+?)(\d)(\w)\d(\d)\d(?P<name2>\w+?)(\d)(\w)',
#           '123abc45678agsf_123abc45678agsf123abc45678agsf')
#
# print(ret.group('name1'))
# print(ret.group('name2'))

# (?P<名字>正则表达式)
# ret.group('名字')

# 分组命名的引用
# import re
# exp= '<abc>akd7008&(&*)hgdwuih</abb>008&(&*)hgdwuih</abd>'
# ret= re.search('<(?P<tag>\w+)>.*?</(?P=tag)>',exp)
# print(ret)

import re
# exp= '<abc>akd7008&(&*)hgdwuih</abc>008&(&*)hgdwuih</abd>'
# ret= re.search(r'<(\w+)>.*?</\1>',exp)
# ret= re.search('<(\w+)>.*?</\\1>',exp)
# print(ret)

import re
# ret=re.findall(r"\d+\.\d+|(\d+)","1-2*(60+(-40.35/5)-(-4*3))")
# print(ret)
# ret = ['1', '2', '60', '', '5', '4', '3','','']
# ret.remove('')
# print(ret)
# ret = filter(lambda n:n,ret)
# print(list(ret))

# 分组命名(?P<组名>正则) (?P=组名)
# 有的时候我们要匹配的内容是包含在不想要的内容之中的,
    # 只能先把不想要的内容匹配出来,然后再想办法从结果中去掉


# 功能
# 性能
    # 时间 ：你要完成一个代码所需要的执行的代码行数
    #        你在执行代码的过程中，底层程序是如何工作的
    # 比如 for i in range(1000):
    #           print(i)
    # 这是1000行代码
    # 空间 ：程序内数据都存储在内存里
        # 占用了宝贵的内存条资源
        # 影响程序的执行效率




##规范性总结 来自 Eva-J 的博客

import re

ret = re.findall('a', 'eva egon yuan')  # 返回所有满足匹配条件的结果,放在列表里
print(ret) #结果 : ['a', 'a']

ret = re.search('a', 'eva egon yuan').group()
print(ret) #结果 : 'a'
# 函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以
# 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。

ret = re.match('a', 'abc').group()  # 同search,不过尽在字符串开始处进行匹配
print(ret)
#结果 : 'a'

ret = re.split('[ab]', 'abcd')  # 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
print(ret)  # ['', '', 'cd']

ret = re.sub('\d', 'H', 'eva3egon4yuan4', 1)#将数字替换成'H'，参数1表示只替换1个
print(ret) #evaHegon4yuan4

ret = re.subn('\d', 'H', 'eva3egon4yuan4')#将数字替换成'H'，返回元组(替换的结果,替换了多少次)
print(ret)

obj = re.compile('\d{3}')  #将正则表达式编译成为一个 正则表达式对象，规则要匹配的是3个数字
ret = obj.search('abc123eeee') #正则表达式对象调用search，参数为待匹配的字符串
print(ret.group())  #结果 ： 123

import re
ret = re.finditer('\d', 'ds3sy4784a')   #finditer返回一个存放匹配结果的迭代器
print(ret)  # <callable_iterator object at 0x10195f940>
print(next(ret).group())  #查看第一个结果
print(next(ret).group())  #查看第二个结果
print([i.group() for i in ret])  #查看剩余的左右结果