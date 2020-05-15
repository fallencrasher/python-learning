import time
import os
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        super().__init__()
    def run(self):  # 自定义的进程 Process 类中必须要自定义一个 run() 方法
        time.sleep(3)
        print(os.getpid(),os.getppid(),self.a,self.b,self.c)
    

if __name__ == "__main__":
    
    p = MyProcess(1,2,3)
    p.start()
    print(p.pid,p.ident) # pid 和 ident 都是进程号
    print(p.name) # 进程名
    print(p.is_alive()) # True 查看进程是否还在进行
    p.terminate() # 结束该进程，异步非阻塞方式发送的命令，不会在这个命令后立即结束，要等操作系统相应我们的指令
    print(p.is_alive()) # True
    time.sleep(0.01)
    print(p.is_alive()) # False
