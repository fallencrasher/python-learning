from threading import Thread,Lock
import time
import dis

n = []
def add():
	for i in range(220000):
		n.append(i)

def pop(lock):
	for i in range(220000):
		with lock:
			if not n:
				time.sleep(1E-7)
			n.pop()

if __name__ == '__main__':
	lock = Lock()
	tl = []
	#dis.dis(pop)
	for i in range(2):
		t1 = Thread(target=add)
		t1.start()
		t2 = Thread(target=pop,args=(lock,))
		t2.start()
		tl.append(t1)
		tl.append(t2)
	for t in tl:
		t.join()
	print(n)

# 这里打印出来的 n 应该是 []
# 但是，有时候，里边也会有值(可能是由于GIL锁的轮转，造成 pop 空列表的现象)，造成数据的不安定
# 但是我们加了线程锁，就不会出现 pop 空列表现象了
# += -= *= /=  while  if  等语句，会造造成数据的不安全
# 所以当使用到这些语句的时候，我们要加锁


# += -=  *= /= while if 数据不安全   + 和 赋值是分开的两个操作
# append pop strip数据安全 列表中的方法或者字典中的方法去操作全局变量的时候 数据安全的
# 线程之间也存在数据不安全


# 不要操作全局变量，不要在类里操作静态变量，
# 这样的话，你就不用锁了，是不会出现线程间数据安全问题的
# 哈哈

# Queue  logging 是线程数据安全的

# dis 模块研究一波
# dis.dis(func) 打印出来的东西里，没有 GLOBAL 变量的操作，那就是数据安全的
