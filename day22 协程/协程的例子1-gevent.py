# from gevent import monkey
# monkey.patch_all()
# import time # 必须在这之前 进行 gevent 的引入的 monkey
# import requests
# import socket
# import gevent

# def func():  # 带有 io 操作的内容都写在函数里，然后提交func给 gevent
#     print('start func')
#     time.sleep(1)
#     print('end func')
#
# g1 = gevent.spawn(func) # 创建 gevent 协程，开启任务
# g2 = gevent.spawn(func)
# g3 = gevent.spawn(func)
# # g1.join() # 阻塞直到 g1 任务执行结束
# # g2.join() # 阻塞直到 g2 任务执行结束
# # g3.join() # 阻塞直到 g3 任务执行结束
# gevent.joinall([g1,g2,g3]) # 这个等价于上边那三行



#############################################
# 如何判断 monkey.patch_all()是否成功呢
#############################################

# 1.可以去源码里看
# socket=True, dns=True, time=True, select=True, thread=True, os=True, ssl=True,
#               subprocess=True, sys=False, aggressive=True, Event=True,
#               builtins=True, signal=True,
#               queue=True, contextvars=True
# 这里 True 的，就能 patch 成功

# 2. 在 monkey.patch_all() 之前打印一次，在 monkey.patch_all() 之后打印一次
# 如果两次结果不一样，那么就说明 monkey.patch_all() 可以成功规避 io

import socket
print(socket.socket) # <class 'socket.socket'>
from gevent import monkey
monkey.patch_all()
import socket
print(socket.socket) # <class 'gevent._socket3.socket'>