import json
from multiprocessing import Process
from multiprocessing import Lock
import time


def search(i):
	with open('ticket', encoding='utf-8') as f:
		t = json.load(f)
		print('%s:剩余%s张票。' % (i, t['count']))


def buy_ticket(i):
	with open('ticket', encoding='utf-8') as f:
		t = json.load(f)
	if t['count'] > 0:
		t['count'] -= 1
		print('%s买到票了' % i)
	time.sleep(0.1)
	with open('ticket', mode='w', encoding='utf-8') as f:
		json.dump(t, f)


def lock_func(i, lock):
	# lock.acquire()  # 拿钥匙，阻塞，别人不能访问
	# print('被所起来的代码 %s ' % i)
	# time.sleep(1)
	# lock.release()  # 还钥匙，解除阻塞
	with lock:
		print('被所起来的代码 %s' % i)
	time.sleep(0.1)


def get_ticket(i, lock):
	search(i)
	with lock: #代替 acquire 和 release，且可以做一些异常处理，保证一个代码出错也会归还钥匙
		buy_ticket(i)



if __name__ == "__main__":
	# for i in range(10):
	#     Process(target=buy_ticket,args=(i,)).start()

	lock = Lock()  #互斥锁，不能在同一个进程中连续acquire多次
	for i in range(10):
		p = Process(target=get_ticket, args=(i, lock)).start()
