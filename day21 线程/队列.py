import queue  # 线程之间数据安全的容器 队列

# q = queue.Queue(4)  # 设置队列的固定长度
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# print('4 done')
# #q.put(5) # 因为已经设置了队列的固定长度，所以这个就会加入不进去了，就会等着
# print(q.get())

# from queue import LifoQueue # 这个是栈
# lq = LifoQueue()
# lq.put(1)
# lq.put(2)
# lq.put(3)
# print(lq.get())
# print(lq.get())
# print(lq.get())

from queue import PriorityQueue # 优先级队列

priq = PriorityQueue()
priq.put((2,'alex')) # 这里的 0，1，2就是优先级，实际上是askii的pailie
priq.put((1,'wusir'))
priq.put((0,'taibai'))
print(priq.get()) #
print(priq.get())
print(priq.get())

#(0, 'taibai')
#(1, 'wusir')
#(2, 'alex')

