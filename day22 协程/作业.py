# 1、什么是协程？常用的协程模块有哪些？
    # 协程的本质是一个线程，不同任务在同一线程上来回切换，以此来规避io阻塞
    # 常用的 协程模块有 gevent  asyncio
# 2、协程中的join是用来做什么用的？它是如何发挥作用的？
    # 协程中的join 用来阻塞线程直到任务结束
# 3、使用协程实现并发的tcp server端
#server
from gevent import monkey
monkey.patch_all()
import socket
import gevent

sk = socket.socket()
sk.bind(('127.0.0.1',43))
sk.listen()

def chat(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8')
        MSG = msg.upper()
        conn.send(MSG.encode('utf-8'))

while True:
    conn,_ = sk.accept()
    gevent.spawn(chat,conn)

# client
import socket
from threading import Thread


def client():
    sk = socket.socket()
    sk.connect(('127.0.0.1', 43))

    while True:
        sk.send(b'hello')
        msg = sk.recv(1024).decode('utf-8')
        print(msg)
for i in range(100):
    Thread(target=client).start()



# 4、进程池、线程池的优势和特点
    # 在执行任务之前就开好进程和线程，当真正执行任务的时候就可以直接用了
    # 池中的进程/线程是被重复利用的，这样减少了操作系统开启/关闭/调度进程/线程所需要的时间成本
# 5、线程和协程的异同?
    # 线程是可被执行的最小单位，数据共享，数据不安全，时间开销比协程大，是操作系统级别的时间片轮转，不能利用多核
    # 协程本质上是个线程，数据共享，数据安全，时间开销比线程小，是用户级别的时间片轮转，不能利用多核
# 6、请列举一个python中数据安全的数据类型？
    # 队列
# 7、Python中如何使用线程池和进程池
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor

def func(a,b):
    return a*b

def print_func(ret):
    print(ret.result())

if __name__ == '__main__':

    pp = ProcessPoolExecutor(4)
    #tp = ThreadPoolExecutor(20)
    for i in range(20):
        ret = pp.submit(func,i,i+1)
        ret.add_done_callback(print_func())

# 8、什么是并行，什么是并发？
    # 并行：在多个CPU上同时执行多个进程
    # 并发：在一个CPU上轮流执行多个进程
# 9、请解释同步和异步这两个概念？
    # 同步：在执行中开一个任务需要等待结果
    # 异步：在执行中开一个任务不需要等待结果自己接着执行
# 10、请谈谈对异步非阻塞的了解？
    # 异步非阻塞就是多个任务同时执行而且CPU一直在工作没有停止的时候，比如在开进程线程时的start（）
# 11、用async关键字写一个最简单的协程函数
import asyncio

async def func(name):
    print('123',name)
    await asyncio.sleep(1)
    print('456')

loop = asyncio.get_event_loop()
loop.run_until_complete(func(name))
loop.run_until_complete(asyncio.wait([func('alex'),func('taibai')]))
# 12、async和await这两个关键字是什么意思？
    # await后面需要跟一个可能会发生阻塞的方法
    # await必须放在一个async函数里，所以async需要加在定义函数前面