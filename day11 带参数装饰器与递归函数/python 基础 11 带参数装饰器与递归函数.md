# python 基础 11 带参数装饰器与递归函数

## 1.递归函数

递归函数就是在函数体里调用自己的函数。这个听着很邪乎。

其实，说是在调用自己，其实就是在掉用函数内部的，调用自身函数命令之前的代码部分。举个例子。

```python

count = 0
def func():
     global count
     count += 1
     print(count)
     if count == 10:return count  # 跳出机制
     #在这一层代码，调用了自己，那么就会开始执行下一个自身代码，也就是这一行之前的部分，直到符合跳出机制
     func()   
     print(456)
func()  
```



```python

# RecursionError
# 递归的最大深度1000层 : 为了节省内存空间,不要让用户无限使用内存空间
# 1.递归要尽量控制次数,如果需要很多层递归才能解决问题,不适合用递归解决
# 2.循环和递归的关系
# 递归不是万能的
# 递归比起循环来说更占用内存
# 修改递归的最大深度
# import sys
# sys.setrecursionlimit(1000000000)

# 你的递归函数 必须要停下来
# 递归函数是怎么停下来的?递归3次结束整个函数
# count = 0
# def func():        # func1
#     global count
#     count += 1     # 1
#     print(count)
#     if count == 3: return
#     func()
#     print(456)
# func()
#
# def func():        # func2
#     global count
#     count += 1     # 2
#     print(count)
#     if count == 3: return
#     func()
#     print(456)
#
#
# def func():        # func3
#     global count
#     count += 1     # 3
#     print(count)
#     if count == 3:return
#     func()
#     print(456)

# 函数的调用
# 函数的参数
# 函数的返回值

# 一个递归函数要想结束,必须在函数内写一个return,并且return的条件必须是一个可达到的条件
# 并不是函数中有return,return的结果就一定能够在调用函数的外层接收到
# def func(count):
#     count += 1
#     print(count)
#     if count == 5 : return 5
#     ret = func(count)
#     print(count ,':',ret)
#     return ret
# print('-->',func(1))

# def func(1):
#     1 += 1
#     print(2)
#     if 2 == 5 : return 5
#     ret = func(2)
#     print(ret)
#     return ret
#
# def func(2):
#     2 += 1
#     print(3)
#     if 3 == 5 : return 5
#     ret = func(3)
#     print(ret)
#     return ret
#
# def func(3):
#     3 += 1
#     print(4)
#     if 4 == 5 : return 5
#     ret = func(4)
#     print(ret)
#     return ret
#
# def func(4):
#     4 += 1
#     print(5)
#     if 5 == 5 : return 5
#     func(count)
#

# def func(count):
#     count += 1
#     print(count)
#     if count == 5 : return 5
#     return func(count)
# print('-->',func(1))


# 递归相关 练习
# 1.计算阶乘 100! = 100*99*98*97*96....*1
# 循环
# 递归
def fin(n):
    if n == 1:
        return n
    else:
        return n*fin(n-1)


ret = fin(7)
print(ret)

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
            
# 3.os模块:计算一个文件夹下所有文件的大小.这个文件夹下面还有文件夹,不能用walk
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
# 找第100个数
# 1 1 2 3 5

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

# 5.三级菜单 可能是n级
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
```

## 2.带参数装饰器

```python
# 什么是装饰器?
# 为什么要有装饰器
# 为什么不能改变原函数的调用方式
    # 开放封闭原则
    # 我们提前写好一个功能,让别人使用的时候能够直接使用就能完成相应的功能

# 登录
# 计算函数的执行时间

# 写了很多的函数
# 添加日志 : 在 时间 调用了什么函数
import time
def logger(path):
    def log(func):
        def inner(*args,**kwargs):
            ret = func(*args,**kwargs)
            with open(path,mode='a',encoding='utf-8') as f:
                msg = '%s 执行了%s'%(time.strftime('%Y-%m-%d %H:%M:%S'),func.__name__)
                f.write(msg)
            return ret
        return inner
    return log

@logger('auth.log')
def login():
    print('登录的逻辑')

@logger('auth.log')
def register():
    print('注册的逻辑')

@logger('auth.log')     # ret = log('auth.log')   show_goods = ret(show_goods)
def show_goods():
    print('查看所有商品信息')

@logger('buy.log')
def add_goods():
    print('商品加入购物车')

# 登录和注册的信息 写到auth.log文件里
# 所有的购物信息 写到operate.log文件里

login()
add_goods()
show_goods()

# @logger('asfg')   # logger('asfg') = log
# @log
# @logger
# def show_goods():
#     print('查看所有商品信息')

# def xxx(*args):
#     def wrapper(func):
#         def inner(*args,**kwargs):
#             ret = func(*args,**kwargs)
#             return ret
#         return inner
#     return wrapper

# 原本有一个装饰器wrapper
# @wrapper
# def func():
#     pass

# @xxx('参数')    == @wrapper
# def func():
#     pass

# 带参数的装饰器
# 有100个函数,分别添加一个计算函数执行时间的装饰器
# 有的时候需要计算时间,有的时候不需要
# 希望能通过修改一个变量,能控制这100个函数的装饰器是否执行
def log():
    judge = True
    if judge==True:
        def timmer(f):
            def inner(*args,**kwargs):
                a = time.time()
                ret = f(*args,**kwargs)
                b = time.time()
                print(f'{f}执行时间为{b-a}秒。')
                return ret
            return inner
        return timmer
    else:
        pass
```

