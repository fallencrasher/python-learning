# 进程
# 1、进程间内存是否共享？如何实现通讯？
## 进程之间内存不共享。ipc通过：队列（安全），管道（不安全）；第三方工具（数据库）
# 2、请聊聊进程队列的特点和实现原理？
## 进程之间通信，先进先出
## 数据安全
## 基于管道 + 锁
## 管道 是基于文件级别 socket + pickle 实现的
## 进程队列基于文件（socket,pickle,Lock）实现.先进先出，放几个取几个，若取值次数超过放值次数就会阻塞
# 3、请画出进程的三状态转换图
##
# 4、你了解生产者模型消费者模型么？如何实现？什么时候用？
## 创建n个生产者来生产数据，再建立m个消费者进程来操作数据，通过调整 n m 的数量来保持效率平衡
## 你为什么知道生产者消费者模型？
    ### 工作经历/采集图片/爬取音乐：由于要爬取大量的数据，想提高爬取效率，有用过一个生产者消费者模型，这个模型是我自己写的，消息中间件用的是 redis
## 什么时候用？
    ###
from multiprocessing import Process


# 5、从你的角度说说进程在计算机中扮演什么角色？
## 一个软件，或一个软件下的多元操作
# 线程
# 1、GIL锁是怎么回事?
## GIL 锁是全局解释器为了 GC 机制方便计算引用计数，所以在一定的条数的代码内或者不碰到io操作的情况下一个进程同时只运行一个线程
# 2、在python中是否线程安全？
## 不安全
# 3、什么叫死锁？
## 多个锁在多个线程下交叉使用所导致的线程无法继续运行
# 4、logging模块是否是线程安全的？
## 是
# 5、queue是否线程安全？
## 是
# 6、程序从flag a执行到falg b的时间大致是多少秒？
## 0s # 只是开启了一个其他线程，并未阻碍主线程代码的继续

import threading
import time
def _wait():
    time.sleep(60)
# flag a
t = threading.Thread(target=_wait,daemon = False)
t.start()
# flag b
7、程序从flag a执行到falg b的时间大致是多少秒？
## 0s
import threading
import time
def _wait():
    time.sleep(60)
# flag a
t = threading.Thread(target=_wait,daemon = True)
t.start()
# flag b
8、程序从flag a执行到falg b的时间大致是多少秒？
## 60s
import threading
import time
def _wait():
    time.sleep(60)
# flag a
t = threading.Thread(target=_wait,daemon = True)
t.start()
t.join()
# flag b
9、读程序，请确认执行到最后number是否一定为0
## 不一定 += 和 -= 都是数据不安全的操作，上个锁就可以了
import threading
loop = int(1E7)
def _add(loop:int = 1):
    global number
    for _ in range(loop):
        number += 1
def _sub(loop:int = 1,lock):
    global number
    with lock:
        for _ in range(loop):
            number -= 1

lock = threading.Lock()
number = 0
ta = threading.Thread(target=_add,args=(loop,))
ts = threading.Thread(target=_sub,args=(loop,lock))
ta.start()
ts.start()
ta.join()
ts.join()
10、读程序，请确认执行到最后number是否一定为0
##  是
import threading
loop = int(1E7)
def _add(loop:int = 1):
    global number
    for _ in range(loop):
        number += 1
def _sub(loop:int = 1):
    global number
    for _ in range(loop):
        number -= 1
number = 0
ta = threading.Thread(target=_add,args=(loop,))
ts = threading.Thread(target=_sub,args=(loop,))
ta.start()
ta.join()
ts.start()
ts.join()
11、读程序，请确认执行到最后number的长度是否一定为1
## 是
import time
import threading
loop = int(1E7)
def _add(loop:int = 1):
    global numbers
    for _ in range(loop):
        numbers.append(0)
def _sub(loop:int = 1):
    global numbers
        for _ in range(loop):
            while not numbers:
                time.sleep(1E-8)
            numbers.pop()
numbers = [0]
ta = threading.Thread(target=_add,args=(loop,))
ts = threading.Thread(target=_sub,args=(loop,))
ta.start()
ta.join()
ts.start()
ts.join()
12、读程序，请确认执行到最后number的长度是否一定为1
## 是
import threading
import time
loop = int(1E7)
def _add(loop:int = 1):
    global numbers
    for _ in range(loop):
        numbers.append(0)
def _sub(loop:int = 1):
    global number
    for _ in range(loop):
        while not numbers:
            time.sleep(1E-8)
        numbers.pop()
numbers = [0]
ta = threading.Thread(target=_add,args=(loop,))
ts = threading.Thread(target=_sub,args=(loop,))
ta.start()
ts.start()
ta.join()
ts.join()