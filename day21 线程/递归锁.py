from threading import Lock,RLock,Thread

# Lock 互斥锁
	# 同一个线程中不可以被 acquire 多次，效率比递归锁要高
# RLock 递归锁 recursion lock
	# 在同一线程中可以被 acquire 多次,但是这个 acquire 多次是针对同一个线程的

# lock = Lock()
#
# lock.acquire()
# print('locked by Lock')
# lock.release()


def func(i,lock):
	lock.acquire()
	lock.acquire()
	print(i,'start')
	lock.release()
	lock.release()
	print(i,'end')

lock = RLock()
for i in range(5):
	Thread(target=func,args=(i,lock)).start()



