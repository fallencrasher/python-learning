#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-15 18:01:32
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

# time 模块
# time 模块封装了获取时间戳和字符串形式的时间的一些方法
import time

# 获取时间戳
# 返回的是格林威治时间，是从时间元年(1970/01/01/00:00:00)到现在经过的秒数或毫秒数
# python 里是秒数 
print(time.time())
a = int(time.time()/86400/365)
print(a)

# 获取格式化时间对象
# 获取的是格林威治时间,结构化时间对象
# 默认参数是当前时间的时间戳
b = time.gmtime()
print(b)

# 获取当地的格式化时间，结构化时间对象
# 默认参数是当前时间的时间戳
c = time.localtime()
print(c)

# 给参数，就是时间元年后的 参数 秒后的结构化时间对象
# 一般，就默认参数就好
print(time.localtime(1))  

# 格式化时间对象和字符串之间的转换
# 格式化时间对象-->字符串，方便人阅读
# 字符串 --> 格式化时间对象，方便计算机传输
# time.strftime('格式化字符串',时间对象) 首先传格式化字符串，然后传结构化时间
# 如果不传结构化时间参数，就默认当前时间戳
d = time.strftime('%Y/%m/%d %H:%M:%S',)
print(d)

# 可以把时间按转换为格式化时间对象
# time.strptime('时间表示','格式化字符串' )
e = time.strptime('2020/04/15','%Y/%m/%d')
print(e)

# 可以把格式化时间对象转化为时间戳,这个没啥用，完全可以直接用 time.time()生成时间戳
t1 = time.localtime()
print(t1)
t2 = time.mktime(t1)
print(t2)

# 暂停当前的程序，睡眠 xxx 秒
# time.sleep(x)
for i in range(5):
	print(time.strftime('%Y/%m/%d %H:%M:%S'))
	time.sleep(1)

# time 模块的三大对象  相互转化
# 1.格式化时间对象： time.struct_time
# 2.时间字符串 
# 3.时间戳 time.time()

# 相互转化
# 时间戳 --> 格式化时间对象
time.gmtime()
time.localtime()

# 格式化时间对象 --> 时间戳
# time.mktime()

# 格式化时间对象 --> 时间字符串
time.strftime('%Y/%m/%d %H:%M:%S')

# 时间字符串 --> 格式化时间对象
time.strptime('2020/04/15','%Y/%m/%d')


