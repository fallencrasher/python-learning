#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-07 21:11:56
# @Author  : Fallen (xdd043@qq.com)
# @Link    : https://github.com/fallencrasher/python-learning
# @Version : $Id$

'''
可变参数 ： 这个传入到函数后，是个元组
可变关键字参数  ： 这个传入到函数后是个字典
'''


def add(name, age, *args):  # 可变参数要写在正常形参的后边，而且传入实参的时候，必须最少有一个参数
    sum = 0
    if len(args) > 0:
        for i in args:
            sum += i
            print("{},{}岁，算的累加和是：{}".format(name, age, sum))

    else:
        print('没有元素可计算.累加和是：', sum)


# 调用,可变参数传入实参要在后边，而实际上，*args接受到实参后，就把他们打包成一个元组了 args = (1,2,3,4)

add("菲菲", 10, 1, 2, 3, 4)
t = (1,2,3,4)
l = [1,2,3,4]
add("feifei",10,*t)
add('feifei',10,*l)

# 关键字参数
# 当定义函数的时候，函数的参数可以设置默认值，这个就是关键字参数
# 当传入多个实参，关键字参数可以被传入实参覆盖


def add1(a, b=10, c=4):
    print(a, b, c)
    result = a+b+c
    print(result)


# 调用 add1
add1(1)
add1(1, 2)

add1(1, 2, 3)

add1(1, c=7)  # 可以指定关键字来进行传入实参
add1(1, b=2, c=9)


#定义函数，计算同学年龄
students={'001':('蔡徐坤',20),'002':('王源',19),'003':('王俊凯',20),'004':('易烊千玺',18)}

def print_boy(who,**persons):
	if isinstance(persons,dict):
		for name,age in persons.values():
			print('{}的年龄是：{}'.format(name,age))


#调用
print_boy("Anna",**students)


def func(**kwargs):  # key word argument
    print(kwargs)


func(a=1, b=2, c=3)  # 可变关键字参数要传参数，就得指名传，传进去的是个字典

#这个时候，我们就会想，哎，你直接传进去个字典行不行啊，都不用它再打包了
#不行！！因为字典是一个封装好的类型，可变关键字参数识别不了他，它不是关键字啊！
#那是不是就不能用了？可以！我们先把字典解包，就行了。
#解包后，传入的是一个个键值对组成的元组(key,value),然后 **kwargs 再打包他们，
#就又成了字典

dict1 = {"001":"phton","002":"java","003":"c","004":"go"}
func(**dict1)

# 定义函数参数时，用*args 和 **keargs 就是在装包
# 调用函数时，传输入参数，用 *args 和 **kwargs 就是在解包