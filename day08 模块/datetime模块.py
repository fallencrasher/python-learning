#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-15 21:49:01
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

'''
datetime 模块：日期和时间模块
封装了一些和日期，时间相关的类

四大类：
date 年月日
time 时分秒
datetime
timedelta

'''
import datetime
#date 类：包含很多方法
a= datetime.date(2020,4,15)
print(a)  #2020-04-15

## 获取date对象的各个属性
## 就是分别获取年月日
print(a.year,type(a.year)) #
print(a.month)
print(a.day)

#time 类：
b = datetime.time(10,48,59)
print(b)

#time 类的属性
print(b.hour)
print(b.minute)
print(b.second)

#datetime 类
c = datetime.datetime(2011,11,11,11,11,11)
print(c)  #2011-11-11 11:11:11

#datetime 类的属性
print(c.year,type(c.year))
print(c.month)
print(c.day)
print(c.hour)
print(c.minute)
print(c.second)

#datetime 模块中的类，主要用于数学计算
#datetime 模块中的类属性返回值，一般都是 int 类型，适合计算

#timedelta 类：时间变化量
#创建一个时间的变化量，相当于时间上的步进值，用某个时间减去它，就得到之间的时间点
#用摸个时间加上他，就是未来的时间点
td = datetime.timedelta(days=1)
print(td)

#参与数学运算
#创建时间对象
# date, datetime, timedelta
# 只收上述三类才能进行时间数据运算， time 属性不能进行运算
d = datetime.date(2010,10,10)
res = d + td
res2 = d - td
print(res)
print(res2)

# 时间变化量的计算，会影响进位
# 满60秒会进位一分钟，满60分钟会进位一小时

t = datetime.datetime(2010,10,10,10,10,59)
td = datetime.timedelta(seconds=3)
res = t + td
print(res) # 2010-10-10 10:11:02

#练习：计算二月份有多少天
#普通的算法：根据年份计算是否是闰年

#用 datetime 模块
##首先创建某一年的 3月1日，然后让他往前退一天
year = 2000  # int(input('输入年份：'))

## 创建制定年份的date对象
d = datetime.date(year,3,1)

## 创建一天的时间变化量
td = datetime.timedelta(days=1)

res = d-td
print(res.day) 

#和时间变化量运算的结果类型
# 与 datetime.timedelta 运算的类型是什么类型，结果就是什么类型
# 如果是两个 datetime.timedelta 类型进行运算，结果就是 datetime.timedelta 类型
d = datetime.date(2020,10,10)
td = datetime.timedelta(days=1)
res = d - td
print(type(res))  # <class 'datetime.date'>


d = datetime.datetime(2020,11,11,11,11,11)
td = datetime.timedelta(days=1)
res = d - td
print(type(res))  #<class 'datetime.datetime'>


td1 = datetime.timedelta(seconds=20)
td2 = datetime.timedelta(days=1)
res = td1 + td2 
print(type(res)) #<class 'datetime.timedelta'>




# d1 = datetime.datetime(2020,11,11,11,11,11)
# d2 = datetime.date(2020,10,10)
# res = d1 -d2 #会报错，这俩不能互相运算，类型不同，且不含有 datetiem.timedelta 类型
# print(res,type(res))


# 同类型时间对象之间的计算
# 日期之间只能相减，相减得到的结果类型是 datetime.timedelta
# 而且，结果都包含 时分秒，即使你没定义也有
d1 = datetime.date(2020,10,10)
d2 = datetime.date(2020,11,11)
res = d2 - d1 #这个不会报错
#res2 = d2+d1 # 这个会报错，日期之间不能相加，只能相减
print(res,type(res)) #32 days, 0:00:00 <class 'datetime.timedelta'>
#print(res2,type(res2)) 

d1 = datetime.datetime(2020,11,11,11,11,11)
d2 = datetime.datetime(2019,11,11,11,11,11)
res = d1 - d2
print(res,type(res)) #366 days, 0:00:00 <class 'datetime.timedelta'>




