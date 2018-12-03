#-*-coding:utf-8-*-
#如何使用线程池？
'''
    解决方案：
        python3中有线程池实现。
        使用标准库中concurrent.futures下的ThreadPoolExecutor，对象的submit和map方法
        可以用来启动线程池中线程执行任务。
'''
import threading, time, random
 
def f(a, b):
  print(threading.current_thread().name, ":", a, b)
  time.sleep(random.randint(5, 10))
  return a*b
 
from concurrent.futures import ThreadPoolExecutor
 
executor = ThreadPoolExecutor(3)
future = executor.submit(f, 2, 3)   # 会返回future对象
 
future.reslut()  # 可以得到6，但这是一个阻塞函数，他会等待f执行完
 
 
# 让线程池中的 每个线程都执行 f函数   可以使用map 实现
 executor.map(f, range(1,6), range(2,7))  # 即1，2    2，3    3，4  。。。。。为参数
 
# map返回生成器，可以用list包裹，得到每个线程的结果
list(executor.map(f, range(1,6), range(2,7)))   # [2,6,12,20,30]
 
