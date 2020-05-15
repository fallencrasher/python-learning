from multiprocessing import Process
import os
import time

def func(name,age):
	print('发送邮件给%s岁的%s'%(age,name))
	time.sleep(1)
	print('发送完毕')

if __name__ == '__main__':
	arg_lst = [('alex',84),('太白', 40),('wusir', 73)]
	p_lst = []
	for arg in arg_lst:
		p = Process(target=func,args=arg)
		p.start()
		p_lst.append(p)
	for p in p_lst:p.join()
	print('所有的邮件已发送')



# 为什么要用 if __name__=='__main__':
# 能不能给子进程传递参数
# 能不能获取子进程的返回值
 # 不能，进程之间数据隔离，所以父进程无法获取子进程的返回值
# 能不能同时开启多个子进程
# join 的用法

# 同步阻塞
	# join
# 异步非阻塞 
	# start
# 多进程之间的数据是否隔离？
	 # 是的
# 使用多进程实现一个并发的 socket  的  server