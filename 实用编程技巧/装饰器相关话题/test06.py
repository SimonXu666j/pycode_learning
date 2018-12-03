#-*-coding:utf-8-*-
#如何实现属性可修改的函数装饰器？
'''
    解决方案：
        为包裹函数增添一个函数，用来修改闭包中使用的自由变量。
        在python3.x中：使用nonlocal访问嵌套作用域中的变量引用。
'''
from functools import wraps

import time
import logging

def warn(timeout):
    timeout = [timeout]
    def decorator(func):
        def wrapper(*args, **kargs):
            start = time.time()
            res = func(*args, **kargs)
            used = time.time() - start
            if used > timeout[0]:
                msg = '"%s": %s > %s' % (func.__name__, used, timeout[0])
                logging.warn(msg)
            return res
        def setTimeout(k):
            #nonlocal timeout  #仅在python3中支持
            timeout[0] = k
        wrapper.setTimeout = setTimeout
        return wrapper
    return decorator

from random import randint
@warn(1.5)
def test():
    print('In test')
    while randint(0, 1):
        time.sleep(0.5)

for _ in range(30):
    test()

test.setTimeout(1)
for _ in range(30):
    test()
