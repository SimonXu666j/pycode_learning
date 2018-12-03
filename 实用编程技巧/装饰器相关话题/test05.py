#-*-coding:utf-8-*-
#如何定义带参数的装饰器?
'''
    解决方案：
        带参数的装饰器，也就是根据参数定制化一个装饰器。可以看成生产装饰器的工厂。
        每次调用typeassert，返回一个特定的装饰器，然后用它去修饰其他函数。
'''
#python3环境
from inspect import signature
def typeassert(*ty_args,**ty_kargs):
    def decorator(func):
        sig=signature(func)
        btypes=sig.bind_partial(*ty_args,**ty_kargs).arguments
        # print(btypes)
        def wrapper(*args,**kargs):
            for name,obj in sig.bind_partial(*args,**kargs).arguments.items():
                # print(name,obj)
                if name in btypes:
                   if not isinstance(obj,btypes[name]):
                       raise TypeError('"%s" must be "%s"' % (name,btypes[name]))
            return func(*args,**kargs)
        return wrapper
    return decorator

@typeassert(int,str,list)
def f(a,b,c):
    print(a,b,c)

f(1,'abc',[1,2,3])
f(1,2,[3,4])