# -*- coding: utf-8 -*-
# @Author: Fallen
# @Date:   2020-04-19 14:58:40
# @Last Modified by:   Fallen
# @Last Modified time: 2020-04-19 21:02:52

# 15.# 带参数的装饰器
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


