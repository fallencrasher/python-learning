#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-16 18:22:32
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

'''
collections 模块

在内置数据类型（dict、list、set、tuple）的基础上，collections模块还提供了几个额外的数据类型：Counter、deque、defaultdict、namedtuple和OrderedDict等。

1.namedtuple: 生成可以使用名字来访问元素内容的tuple

2.deque: 双端队列，可以快速的从另外一侧追加和推出对象

3.Counter: 计数器，主要用来计数

4.OrderedDict: 有序字典

5.defaultdict: 带有默认值的字典
'''
import collections
# 1.namedtuple 生成可以使用名字来访问元素内容的tuple
# namedtuple('名称', [属性list])
'''
我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：

p = (1, 2)
但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。

这时，namedtuple就派上了用场：
'''
Point = collections.namedtuple('Point',['x','y'])
p = Point(1,2)
print(p.x,p.y)

## 也可以用坐标和半径表示一个圆：
Circle = collections.namedtuple('Circle',['x','y','r'])
cir = Circle(1,2,3)
print(cir.x,cir.y,cir.r)

# 2.deque 双端队列，可以快速的从另外一侧追加和推出对象
'''
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。

deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
'''
q = collections.deque(['a','b','c'])
q.append('x') #右边加入
q.appendleft('y') # 左边加入
print(q) #deque(['y', 'a', 'b', 'c', 'x'])
q.pop() #右边弹出
q.popleft() #左边弹出
print(q) #deque(['a', 'b', 'c'])

# 3.OrderedDict: 有序字典
'''
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。

如果要保持Key的顺序，可以用OrderedDict：
'''
d = dict([('a',1),('b',2),('c',3)])
print(d)
od = collections.OrderedDict([('a',1),('b',2),('c',3)])
print(od) #OrderedDict([('a', 1), ('b', 2), ('c', 3)])

#注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
od = collections.OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(od.keys()) #odict_keys(['z', 'y', 'x']) 按照插入的key的顺序返回

# 4.defaultdict 带有默认值的字典
# defaultdict 接受的第一个参数，这个参数将作为默认键值对的值，这个参数叫做工厂，
# 可以是数据类型转化函数名：list  tuple  dict  str  int float 等等，也可以是我们自己写的构造函数，当我们
# 引用字典中不存在的键，不会报错，会返回一个默认的值，这个默认值就是 [], (), {}, "" ,0 ,0.0
# 创建字典的几种方式
## 普通赋值建立
d = {'name':'Andy','age':18}
d = dict([('name','Andy'),('age',18)])
d = dict(name='Andy',age='18')
d = {k:v for k in range(10) for v in range(10)}
print(d)
d = collections.defaultdict(int,name='Andy',age=18)
print(d) #defaultdict(<class 'str'>, {'name': 'Andy', 'age': 18})
print(d['addr']) #0
'''
这个呢，我也不知道有啥用，可能是为了当你使用字典不存在的键值对的时候
不会报错吧，哈哈哈哈哈哈。但是这么一想，唉，还有点用。
'''
'''
有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。

即： {'k1': 大于66 , 'k2': 小于66}
'''
li = [11,22,33,44,55,77,88,99,90]

## 使用普通字典
dic = {'k1':[],'k2':[]}

for i in li:
	if i > 66:
		dic['k1'].append(i)
	elif i< 66:
		dic['k2'].append(i)

print(dic)

## 使用 defaultdict

dic2 = collections.defaultdict(list)
print(dic2)
for i in li:
	if i > 66:
		dic2['k1'].append(i)
	elif i< 66:
		dic2['k2'].append(i)

print(dic2)

## 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
dd = collections.defaultdict(lambda : 'N/A')
dd['key1'] = 'abc'
print(dd['key1']) #abc
print(dd['key2']) #N/A

# 5. Counter 类，计数
## Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）。Counter类和其他语言的bags或multisets很相似。

c = collections.Counter('abcdabcesdfsdzfdfzdfas')
print(c) #Counter({'d': 5, 'f': 4, 'a': 3, 's': 3, 'b': 2, 'c': 2, 'z': 2, 'e': 1})
print(c['a']) #3
print(c.most_common(3)) #[('d', 5), ('f', 4), ('a', 3)] 曲线次数排名前三的
