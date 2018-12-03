#-*-coding:utf-8-*-
#如何使用函数装饰器？
'''
    解决方案：
        定义装饰器函数，用它来生成一个在原函数基础添加了新功能的函数，替代原函数。
'''
def memo(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memo
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# def fibonacci2(n,cache = None):
#     if cache is None:
#         cache = {}

#     if n in cache:
#         return cache[n]

#     if n <= 1:
#         return 1

#     cache[n] = fibonacci2(n - 1,cache) + fibonacci2(n - 2,cache)
#     return cache[n]


'''
    ==>一个共有10个台阶的楼梯，从下面走到上面，一次只能迈1，2，3个台阶
    ==>  并且不能后退，走完这个楼梯共有多少中方法
'''
def climb(n,steps):
    count = 0
    if n == 0:
        count = 1

    elif n >0:
        for step in steps:
            count += climb(n-step,steps)

    return count    

# print fibonacci2(5)
# print fibonacci(50)
# fibonacci = memo(fibonacci)
print fibonacci(50)
print climb(10,(1,2,3))
