#-*-coding:utf-8-*-
#如何为被装饰的函数保存元数据？
'''
    解决方案：
        使用标准库functools中的装饰器wraps装饰内部包裹函数，
        可以制定将原函数的某些属性，更新到包裹函数上面。    
'''
def f(a):
    return a*2

def f1(a,b=1,c=[]):
    print(a,b,c)
print(f.__name__)
print(f.__doc__)
print(f.__module__)
print(f.__defaults__)
print(f1.__defaults__)
#默认参数中尽量不要使用可变对象，函数定义的时候这些变量就已经生成
f1.__defaults__[1].append('abc')
f1('simon')
print(f.__closure__)
#函数闭包,a存储在闭包中，不会因为函数退出以后，lambda表达式访问不到a
def f2():
    a=2
    return lambda k:a**k
g=f2()
print(g.__closure__)
c=g.__closure__[0]
#访问闭包中的a
print(c.cell_contents)