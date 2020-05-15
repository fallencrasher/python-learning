# Manager() 模块，了解就好，一般不用

from multiprocessing import Process,Manager,Lock

def change_dic(dic,lock):
    with lock:
        dic['count'] -= 1


if __name__ == "__main__":
    m = Manager()
    lock = Lock()
    dic = m.dict({'count':100})
    p_l = []
    for i in range(100):
        p = Process(target=change_dic,args=(dic,lock))
        p.start()
        p_l.append(p)
    for p in p_l:p.join()
    print(dic)