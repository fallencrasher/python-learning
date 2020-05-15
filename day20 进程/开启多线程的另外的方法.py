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
    for i in range(10):
        p = MyProcess(1,2,3)
        p.start()
    # print(p.pid,p.ident)
    # print(p.name)
    # print(p.is_alive())
    # p.terminate()
    # print(p.is_alive())
    # time.sleep(0.01)
    # print(p.is_alive())
