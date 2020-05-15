from threading import Thread
import time


class A(object):
	from threading import Lock
	__flag = None
	lock = Lock()

	def __new__(cls, *args, **kwargs):
		with cls.lock:
			if not cls.__flag:
				time.sleep(0.000001)
				cls.__flag = super().__new__(cls)
		return cls.__flag


def func():
	a = A()
	print(a)


for i in range(10):
	Thread(target=func).start()
