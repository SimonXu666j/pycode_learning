#coding=utf-8
'''
    python多线程总结：
    python提供了两个模块来实现多线程thread和threading ，thread有一些缺点。
    创建线程t,使用threading.Thread(target=方法名,args=(参数1,))方法。
    t.start()     --线程启动
    t.join()      --子线程调用join()方法，作用是子线程阻塞主线程，子线程执行完成之后，再执行主线程。
    t.setDaemon(True)      --只要主线程完成了，不管子线程是否完成，都要和主线程一起退出,放在线程启动之前，即t.start()之前。
                           --如果不加，那么执行一个主线程，如果主线程又创建一个子线程，主线程和子线程就分兵两路，
                            分别运行，那么当主线程完成想退出时，会检验子线程是否完成，如果子线程未完成，则主线程会等待子线程完成后再退出。
'''
import threading
from time import ctime,sleep


def music(func):
    for i in range(2):
        print "I was listening to %s. %s" %(func,ctime())
        sleep(4)

def move(func):
    for i in range(2):
        print "I was at the %s! %s" %(func,ctime())
        sleep(5)

threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print "all over %s" %ctime()