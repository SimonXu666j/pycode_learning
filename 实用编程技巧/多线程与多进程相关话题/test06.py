#-*-coding:utf-8-*-
#如何使用多进程？
'''
由于python中全局解释器锁GIL的存在， 在任意时刻只允许一个线程在解释器中运行。
因此python的多线程不适合处理cpu密集型的任务。想要处理cpu密集型的任务， 可以使用多进程模型。
'''
'''
    解决方案：
        使用标准库中的'multiprocessing.Process', 它可以启动子进程执行任务。
        操作接口， 进程间通信， 进程间同步等都与'Threading.Thread'类似。
'''
from threading import Thread
from multiprocessing import Process
from Queue import Queue as Thread_Queue   # 线程的queue
from multiprocessing import Queue as Process_Queue   # 进程的queue
 
def is_armstrong(n):
    a, t = [], n
    while t:
        a.append(t % 10)
        t //= 10
    k = len(a)
    return sum(x ** k for x in a) == n
 
def find_armstrong(a, b, q=None):
    res = [x for x in range(a, b) if is_armstrong(x)]
    if q:
        q.put(res)
    return res
 
def find_by_thread(*ranges):
    q = Thread_Queue()
    workers = []
    for r in ranges:
        a, b = r
        t = Thread(target=find_armstrong, args=(a, b, q))
        t.start()
        workers.append(t)
 
    res = []
    for _ in range(len(ranges)):
        res.extend(q.get())
 
    return res
 
def find_by_process(*ranges):
    q = Process_Queue()
    workers = []
    for r in ranges:
        a, b = r
        t = Process(target=find_armstrong, args=(a, b, q))
        t.start()
        workers.append(t)
 
    res = []
    for _ in range(len(ranges)):
        res.extend(q.get())
 
    return res
 
 
    
if __name__ == '__main__':
    import time
    t0 = time.time()
    #res = find_by_thread([10000000, 15000000], [15000000, 20000000], 
    #                     [20000000, 25000000], [25000000, 30000000]) 
    res = find_by_process([10000000, 15000000], [15000000, 20000000], 
                         [20000000, 25000000], [25000000, 30000000]) 
    print(res)
    print(time.time() - t0)
