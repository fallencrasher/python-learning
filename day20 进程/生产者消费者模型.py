# 生产者，消费者模型
    # 爬虫的时候
    # 分布式操作 ：celery
    # 本质：就是让生产数据和处理数据的效率达到平衡并且最大化效率


from multiprocessing import Queue,Process
import random
import time

def consumer(q,name): # 消费者：通常收到数据后还要进行某些操作
    while True: # 这样，保证我们消费者可以及时消费，而且当生产者不提供的时候，可以停下程序
        food = q.get() 
        if food:
            print('%s吃了%s'%(name,q.get()))
        else:
            break

def producer(q,name,food): # 生产者： 通常在提供数据之前需要先去获取数据
    for i in range(10):
        foodi = '%s%s'%(food,i)
        print('%s生产了%s'%(name,foodi))
        time.sleep(random.random())
        q.put(foodi)


if __name__ == "__main__":
    q = Queue()
    c1 = Process(target=consumer,args=(q,'alex'))
    c2 = Process(target=consumer,args=(q,'wusir'))
    p1 = Process(target=producer,args=(q,'大壮','泔水'))
    p2 = Process(target=producer,args=(q,'b哥','香蕉'))
    c1.start()
    c2.start()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    q.put(None)
    q.put(None)