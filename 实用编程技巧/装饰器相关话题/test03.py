#-*-coding:utf-8-*-
#如何为被装饰的函数保存元数据？
'''
    解决方案：
        使用标准库functools中的装饰器wraps装饰内部包裹函数，
        可以制定将原函数的某些属性，更新到包裹函数上面。    
'''
from functools import update_wrapper,wraps,WRAPPER_ASSIGNMENTS,WRAPPER_UPDATES
def mydecoratot(func):
    #@wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper function"""
        print("In wrapper")
        func(*args, **kwargs)
    #update_wrapper(wrapper,func,('__name__','__doc__'),('__dict__',))
    #WRAPPER_ASSIGNMENTS,WRAPPER_UPDATES默认参数
    update_wrapper(wrapper,func)
    return wrapper

@mydecoratot
def example():
    """example function"""
    print('In example')
    
print(example.__name__)
print(example.__doc__)
print(WRAPPER_ASSIGNMENTS)
print(WRAPPER_UPDATES)