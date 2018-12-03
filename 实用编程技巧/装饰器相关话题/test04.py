#-*-coding:utf-8-*-
#如何定义带参数的装饰器?
'''
    解决方案：
        带参数的装饰器，也就是根据参数定制化一个装饰器。可以看成生产装饰器的工厂。
        每次调用typeassert，返回一个特定的装饰器，然后用它去修饰其他函数。
'''
# def typeassert(*ty_args，**ty_kargs):
#     def decorator(func):
#         def wrapper(*args,**kargs):
#             return func(*args,**kargs)
#         return wrapper
#     return decorator
from inspect import signature
def f(a,b,c=1):pass

#获取函数签名
sig=signature(f)
a=sig.parameters['a']
c=sig.parameters['c']
print(a.name,a.kind)
print(c.default)
#建立字典
bargs=sig.bind(str,int,int)
print(bargs.arguments)