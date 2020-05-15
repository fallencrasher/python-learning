import requests
from multiprocessing import Process,Queue

url_dic = {
    'cnblogs':'https://www.cnblogs.com/Eva-J/articles/8253549.html',
    'douban':'https://www.douban.com/doulist/1596699/',
    'baidu':'https://www.baidu.com',
    'gitee':'https://gitee.com/old_boy_python_stack__22/teaching_plan/issues/IXSRZ',
}

def producer(name,url,q):
    ret = requests.get(url)
    q.put((name,ret.text))

def consumer(q):
    while True:
        tup = q.get()
        if tup is None:break
        with open('%s.html'%tup[0],encoding='utf-8',mode='w') as f:
            f.write(tup[1])


if __name__ == "__main__":
    q = Queue()
    pl = []
    for key in url_dic:
        p = Process(target=producer,args=(key,url_dic[key],q))
        p.start()
        pl.append(p)
    Process(target=consumer,args=(q,)).start()
    Process(target=consumer,args=(q,)).start()
    for p in pl:p.join()
    q.put(None)
    q.put(None) # 两个消费者，都要结束，当一个消费者取到一个 None 就结束了，但是另一个消费者也要取到一个None才能结束