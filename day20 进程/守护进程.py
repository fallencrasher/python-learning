import time
from multiprocessing import Process

def son1():
    while True:
        print('in son1')
        time.sleep(1)


def son2():
    for i in range(10):
        print('in son2')
        time.sleep(1)




if __name__ == "__main__":
    p1 = Process(target=son1)
    p1.daemon = True  # 表示设置 p1 是个守护进程,p1作为守护进程，它的结束时间是当主进程的代码执行完的瞬间，他就结束，即使 p1 进程没有自己设置结束条件也会结束
    p1.start() 
    p2 = Process(target=son2)
    p2.start()
    time.sleep(3)
    print('--> in main')
    p2.join() # 如此，p1 进程会等到 p2 结束后才结束
# 主进程会等待所有的子进程结束以回收资源
# 守护进程会等待主进程的代码执行结束后再结束,而不是等待整个主进程结束
# 主进程的代码什么时候结束，守护进程就什么时候结束，和其他的进程执行无关
# 注意是代码结束，就是运行到这一步代码，而不是要等到主进程结束
# 主进程不结束，他要等着回收子进程运行完成后回收资源呢