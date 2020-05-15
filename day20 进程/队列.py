# 进程之间数据隔离
# 进程之间通信 Inter Process Communication(IPC)
    # 基于文件：同一台机器的多个进程通信
        # Queue
        # 基于 socket 的
    # 基于网路：同一台机器或多台机器的进程间通信
        # 第三方工具（消息中间件）
            # redis
            # rabbitmq
            # kafka
            # memcache

from multiprocessing import Queue,Process

def son1(q):
    for i in range(10):
        q.put('hello %s'%i)

def pro(q):
    for i in range(10):
        print(q.get())

if __name__ == "__main__":
    q = Queue()
    Process(target=son1,args=(q,)).start()
    # print(q.get()) # 在主进程里得到了子进程中的数据
    Process(target=pro,args=(q,)).start()


