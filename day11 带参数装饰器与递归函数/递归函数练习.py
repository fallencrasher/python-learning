# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-19 14:57:32
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-19 18:25:50

# 煞笔递归，卧槽，发明这个的人真的牛逼，我智商太低
# 第一次学，真的看不懂




# 16.# 递归相关 练习
# 1.计算阶乘 100! = 100*99*98*97*96....*1
# 循环
# 递归
# import os


# def fin(n):
#     if n == 1:
#         return n
#     else:
#         return n*fin(n-1)


# ret = fin(10)
# print(ret)

# 2.os模块:查看一个文件夹下的所有文件,这个文件夹下面还有文件夹,不能用walk



def show_dir(path):
    name_list = os.listdir(path)
    for name in name_list:
        abs_path = os.path.join(path,name)
        if os.path.isfile(abs_path):
            print(name)
        elif os.path.isdir(abs_path):
            print('-->',name)
            show_dir(abs_path)

# show_dir(r'D:\programming_with_python\043从零开始学python')
# 3.os模块:计算一个文件夹下所有文件的大小.这个文件夹下面还有文件夹,不能用walk\
import os

def every_file_size(path):
    sum = 0
    name_list = os.listdir(path)
    for name in name_list:
        abs_path = os.path.join(path,name)
        if os.path.isfile(abs_path):
            ret = os.path.getsize(abs_path)
            sum += ret
            print(abs_path,ret)
        elif os.path.isdir(abs_path):
            print('-->',name)
            ret = every_file_size(abs_path)
            sum += ret
    return sum

s = every_file_size(r'D:\programming_with_python\043从零开始学python')        
print(s)




# 4.计算斐波那契数列
def fib(num):
    if num == 1 or num == 2: return 1
    else: 
        return fib(num-2)+fib(num-1)
fib(10)

# 用循环
def fib2(n):
    a = 1
    b = 1
    while n>2:
        a,b=b,a+b
        n -= 1
    return b
ret = fib2(3)
print(ret)

# 由上边的循环来看，我们可以优化递归
def fib3(n,a=1,b=1):
    if n==1 or n==2:
        return b
    else:
        a,b = b,a+b
        return fib3(n-1,a,b)
print(fib3(100))

# 或者
# 这个方法，跟上边的这个一样，就是起点，从1=1+0开始
def fib4(n,a=1,b=0):
    if n==1:
        return a+b
    return fib4(n-1,b,a+b)

print(fib4(100))

# 也可用生成器来做
def fib5(n):
    if n==1:
        yield 1
    else:
        yield from (1,1)
        a,b=1,1
        while n>2:
            a,b = b,a+b
            yield b
            n -= 1
a = fib5(100)
for i in a:
    print(i)
# 找第100个数
# 1 1 2 3 5
# 5.访问三级菜单 可能是n级
# 递归 循环 
# https://www.cnblogs.com/Eva-J/articles/7205734.html#_label4
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

def menu_func(menu):
    flag = True
    while flag:
        for name in menu:
            print(name)
        key = input('想看那个城市>>>').strip()  #北京        
        if key.lower() =='q':
            print('再见')
            return False
        elif key.lower() == 'b':
            return True
        elif menu.get(key):
            flag = menu_func(menu[key])

# 下边这个也对，但是我看不懂，以后再看把        
# def menu_func(menu):
#     while True:
#         for name in menu:
#             print(name)
#         key = input('想看那个城市>>>').strip()  #北京        
#         if key.lower() =='q':
#             print('再见')
#             return False
#         elif key.lower() == 'b':
#             return True
#         elif menu.get(key):
#             flag = menu_func(menu[key])
#             if not flag: return False

menu_func(menu)
print('wahaha')