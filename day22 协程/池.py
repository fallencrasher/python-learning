from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from threading import current_thread
import time
import random
import os
# 这就是进程池和线程池的两个类
# threading 模块 没有提供池
# multiprocessing 模块是仿照 threading 写的，Pool
# py 3.x 推出了 concurrent.futures 模块，线程池和进程池都能够用相似的方式启动/使用

# pp = ProcessPoolExecutor(5) # 创建5个进程对象，放在池中
# tp = ThreadPoolExecutor(20) # 创建20个线程对象，这就创建了池

###########
# 线程池
##########


# def func(a,b):
#     print(current_thread().ident,'start',a,b)
#     time.sleep(random.randint(1,4))
#     print(current_thread().ident,'end',a,b)
#
#
# tp = ThreadPoolExecutor(4) # 创建线程池，个数为4
#
#
# for i in range(20):
#     tp.submit(func,i,b=i+1) # 把任务 func 提交给线程池 tp,后边还可以给任务函数传参数


# 实例化 创建池
# 使用 submit 传递任务，和参数
# 进程池和线程池操作一样

###########
# 进程池
##########
# def func(a,b):
#     print(os.getpid(),'start',a,b)
#     time.sleep(random.randint(1,4))
#     print(os.getpid(),'end',a,b)
#
# if __name__ == '__main__':
#
#     tp = ProcessPoolExecutor(4) # 创建线程池，个数为4
#     for i in range(20):
#         tp.submit(func,i,b=i+1) # 把任务 func 提交给进程池 tp,后边还可以给任务函数传参数


#############################################
# 获取进程/线程的返回结果
#############################################

# low版
# def func(a,b):
#     print(os.getpid(),'start',a,b)
#     #time.sleep(random.randint(1,4))
#     print(os.getpid(),'end',a,b)
#     return a*b
#
# if __name__ == '__main__':
#
#     tp = ProcessPoolExecutor(4) # 创建线程池，个数为4
#     for i in range(20):
#         ret = tp.submit(func,i,b=i+1) # ret 获得的返回结果是一个 future 对象,未来对象，为啥叫未来对象，因为我们创建的时候不用，后来才用
#         print(ret.result()) # future 对象加 result() 可以获取原来的结果
#

# 但是这么写，多线程会一个一个执行，不同时执行

# 牛逼版
# def func(a,b):
#     print(os.getpid(),'start',a,b)
#     time.sleep(random.randint(1,4))
#     print(os.getpid(),'end',a,b)
#     return a*b
#
# if __name__ == '__main__':
#
#     tp = ProcessPoolExecutor(4) # 创建线程池，个数为4
#     future_l = {}
#     for i in range(20): # 异步非阻塞
#         ret = tp.submit(func,i,b=i+1) # ret 获得的返回结果是一个 future 对象
#         future_l[i] = ret
#     for key in future_l: # 同步阻塞
#         print(key,future_l[key].result())

#############################################
# 池的 map 函数
#############################################
# def func(a):
#     b = a+1
#     # print(os.getpid(),'start',a,b)
#     # time.sleep(random.randint(1,4))
#     # print(os.getpid(),'end',a,b)
#     return a*b
#
# if __name__ == '__main__':
#
#     tp = ProcessPoolExecutor(4) # 创建线程池，个数为4
#     ret = tp.map(func,range(20)) # map 只能传递可迭代对象作为参数
#     for key in ret:
#         print(key)


#############################################
# 池的 回调 函数 add_done_callback()，效率最高，只要是想要获取线程的返回值，就用这个
#############################################

# def func(a,b):
#     print(current_thread().ident,'start',a,b)
#     time.sleep(random.randint(1,4))
#     print(current_thread().ident,'end',a,b)
#     return a*b
#
# def print_func(ret):
#     print(ret.result())
#
# if __name__ == '__main__':
#
#     tp = ThreadPoolExecutor(4) # 创建线程池，个数为4
#     for i in range(20): # 异步非阻塞
#         ret = tp.submit(func,i,b=i+1) # ret 获得的返回结果是一个 future 对象
#         ret.add_done_callback(print_func) # 异步阻塞
#         # 异步阻塞的回调函数,返回的ret对象绑定一个回调函数，等待ret对应的任务有了结果以后立即调用 print_func 函数，并且把任务的返回值
#         # 传递给print_func 作为参数
#         # 就可以对返回的结果立即进行处理，而不用按照顺序接受结果处理结果

#############################################
# 池的 回调 函数 add_done_callback() 的底层实现
#############################################

# import time
# import random
# import queue
# from threading import Thread
#
# def func(q,i):
#     print('start',i)
#     time.sleep(random.randint(1,5))
#     print('end',i)
#     q.put(i*(i+1))
#
# def print_func(q):
#     print(q.get())
#
# q = queue.Queue()
# for i in range(20):
#     Thread(target=func,args=(q,i)).start()
# for i in range(20):
#     Thread(target=print_func,args=(q,)).start()

#############################################
# 池的 回调 函数 add_done_callback() 的例子
#############################################

from concurrent.futures import ThreadPoolExecutor
import requests
import os

def get_page(url):    # 访问网页,获取网页源代码   线程池中的线程来操作
    print('<进程%s> get %s' %(os.getpid(),url))
    respone=requests.get(url)
    if respone.status_code == 200:
        return {'url':url,'text':respone.text}

def parse_page(res):   # 获取到字典结果之后,计算网页源码的长度,把https://www.baidu.com : 1929749729写到文件里   线程任务执行完毕之后绑定回调函数
    res=res.result()
    print('<进程%s> parse %s' %(os.getpid(),res['url']))
    parse_res='url:<%s> size:[%s]\n' %(res['url'],len(res['text']))
    with open('db.txt','a') as f:
        f.write(parse_res)

if __name__ == '__main__':
    urls=[
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://help.github.com/',
        'http://www.sina.com.cn/'
    ]
    tp = ThreadPoolExecutor(4) # 创建线程池
    for i in urls:
        # 得到一个futrue对象 = 把每一个url提交一个get_page任务
        ret = tp.submit(get_page,i) # 向进程池提交任务
        ret.add_done_callback(parse_page) # 绑定 回调函数 parse_page 到线程执行返回结果，谁先回来谁就先写结果进文件

    # 不用回调函数:
    # 按照顺序获取网页 百度 python openstack git sina
    # 也只能按照顺序写
    # 用上了回调函数
    # 按照顺序获取网页 百度 python openstack git sina
    # 哪一个网页先返回结果,就先执行那个网页对应的parserpage(回调函数)

    # 会起池\会提交任务
    # 会获取返回值\会用回调函数

    # 1.所有的例题 会默
    # 2.进程池(高计算的场景,没有io(没有文件操作\没有数据库操作\没有网络操作\没有input)) : >cpu_count*1  <cpu_count*2
    #   线程池(一般根据io的比例定制) : cpu_count*5
    # 5*20 = 100并发
